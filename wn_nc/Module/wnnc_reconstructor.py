import os
import torch
import numpy as np
import torch.nn.functional as F
from tqdm import tqdm, trange

from wn_nc.Data.wn_treecode_func import WindingNumberTreecode
from wn_nc.Method.width import getWidthRange
from wn_nc.Method.io import loadPoints
from wn_nc.Method.pcd import toNormalizedPoints
from wn_nc.Method.path import removeFile, createFileFolder
from wn_nc.Method.cmd import runCMD

class WNNCReconstructor(object):
    def __init__(self) -> None:
        return

    def estimateNormal(self,
                       pcd_file_path: str,
                       save_pcd_file_path: str,
                       width_tag: str = 'l0',
                       wsmin: float = 0.01,
                       wsmax: float = 0.04,
                       iters: int = 40,
                       use_gpu: bool = True,
                       print_progress: bool = True,
                       overwrite: bool = False) -> bool:
        if not os.path.exists(pcd_file_path):
            print('[ERROR][WNNCReconstructor::estimateNormal]')
            print('\t pcd file not exist!')
            print('\t pcd_file_path:', pcd_file_path)
            return False

        if not overwrite:
            if os.path.exists(save_pcd_file_path):
                return True

            removeFile(save_pcd_file_path)

        save_pcd_folder_path = os.path.dirname(save_pcd_file_path)
        os.makedirs(save_pcd_folder_path, exist_ok=True)

        points_unnormalized = loadPoints(pcd_file_path)
        if points_unnormalized is None:
            print('[ERROR][WNNCReconstructor::esimateNormal]')
            print('\t loadPoints failed!')

            return False

        points_normalized = toNormalizedPoints(points_unnormalized)
        points_normalized = torch.from_numpy(points_normalized).contiguous().float()
        normals = torch.zeros_like(points_normalized).contiguous().float()
        b = torch.ones(points_normalized.shape[0], 1) * 0.5
        widths = torch.ones_like(points_normalized[:, 0])

        if use_gpu:
            points_normalized = points_normalized.cuda()
            normals = normals.cuda()
            b = b.cuda()
            widths = widths.cuda()

        wn_func = WindingNumberTreecode(points_normalized)

        wsmin, wsmax = getWidthRange(width_tag)
        assert wsmin <= wsmax

        # print(f'[LOG] You are using width tag {width_tag} width wsmin = {wsmin}, wsmax = {wsmax}')

        if wn_func.is_cuda:
            torch.cuda.synchronize(device=None)

        with torch.no_grad():
            bar = trange(iters) if print_progress else range(iters)
            if print_progress:
                print('[INFO][WNNCReconstructor::estimateNormal]')
                print('\t start estimate normal for pointcloud...')
            for i in bar:
                width_scale = wsmin + ((iters-1-i) / ((iters-1))) * (wsmax - wsmin)
                # width_scale = args.wsmin + 0.5 * (args.wsmax - args.wsmin) * (1 + math.cos(i/(iters-1) * math.pi))

                # grad step
                A_mu = wn_func.forward_A(normals, widths * width_scale)
                AT_A_mu = wn_func.forward_AT(A_mu, widths * width_scale)
                r = wn_func.forward_AT(b, widths * width_scale) - AT_A_mu
                A_r = wn_func.forward_A(r, widths * width_scale)
                alpha = (r * r).sum() / (A_r * A_r).sum()
                normals = normals + alpha * r

                # WNNC step
                out_normals = wn_func.forward_G(normals, widths * width_scale)

                # rescale
                out_normals = F.normalize(out_normals, dim=-1).contiguous()
                normals_len = torch.linalg.norm(normals, dim=-1, keepdim=True)
                normals = out_normals.clone() * normals_len

        if wn_func.is_cuda:
            torch.cuda.synchronize(device=None)

        with torch.no_grad():
            out_points_normals = np.concatenate([points_unnormalized, normals.detach().cpu().numpy()], -1)
            createFileFolder(save_pcd_file_path)
            np.savetxt(save_pcd_file_path, out_points_normals)

        return True

    def reconstructSurface(self,
                           pcd_file_path: str,
                           save_mesh_file_path: str,
                           use_gpu: bool = True,
                           overwrite: bool = False) -> bool:
        if not os.path.exists(pcd_file_path):
            print('[ERROR][WNNCReconstructor::reconstructSurface]')
            print('\t pcd file not exist!')
            print('\t pcd_file_path:', pcd_file_path)

            return False

        if not overwrite:
            if os.path.exists(save_mesh_file_path):
                return True

            removeFile(save_mesh_file_path)

        if use_gpu:
            exec_file_path = '../wn-nc/bin/main_GaussRecon_cuda'
        else:
            exec_file_path = '../wn-nc/bin/main_GaussRecon_cpu'

        command = exec_file_path + \
            ' -i ' + pcd_file_path + \
            ' -o ' + save_mesh_file_path

        createFileFolder(save_mesh_file_path)

        if not runCMD(command):
            print('[ERROR][WNNCReconstructor::reconstructSurface]')
            print('\t runCMD failed!')
            print('\t command:', command)

            return False

        return True

    def autoReconstructSurface(self,
                       pcd_file_path: str,
                       save_pcd_file_path: str,
                       save_mesh_file_path: str,
                       width_tag: str = 'l0',
                       wsmin: float = 0.01,
                       wsmax: float = 0.04,
                       iters: int = 40,
                       use_gpu: bool = True,
                       print_progress: bool = True,
                       overwrite: bool = False) -> bool:
        if not self.estimateNormal(
            pcd_file_path,
            save_pcd_file_path,
            width_tag,
            wsmin,
            wsmax,
            iters,
            use_gpu,
            print_progress,
            overwrite):
            print('[ERROR][WNNCReconstructor::autoReconstructSurface]')
            print('\t estimateNormal failed!')

            return False

        if not self.reconstructSurface(
            save_pcd_file_path,
            save_mesh_file_path,
            use_gpu,
            overwrite):
            print('[ERROR][WNNCReconstructor::autoReconstructSurface]')
            print('\t reconstructSurface failed!')

            return False

        return True

    def autoReconstructSurfaceFolder(self,
                       pcd_folder_path: str,
                       save_pcd_folder_path: str,
                       save_mesh_folder_path: str,
                       width_tag: str = 'l0',
                       wsmin: float = 0.01,
                       wsmax: float = 0.04,
                       iters: int = 40,
                       use_gpu: bool = True,
                       print_progress: bool = True,
                       overwrite: bool = False) -> bool:
        rel_pcd_file_path_list = []
        for root, _, files in os.walk(pcd_folder_path):
            for file in files:
                file_extension = os.path.splitext(file)[-1]
                if file_extension not in ['.xyz', '.ply', '.obj']:
                    continue

                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, pcd_folder_path)

                rel_pcd_file_path_list.append(relative_path)

        print('[INFO][WNNCReconstructor::autoReconstructSurfaceFolder]')
        print('\t start auto recon surface for shapes in folder...')
        bar = tqdm(rel_pcd_file_path_list) if print_progress else rel_pcd_file_path_list
        for rel_pcd_file_path in bar:
            pcd_file_path = pcd_folder_path + rel_pcd_file_path
            save_pcd_file_path = save_pcd_folder_path + rel_pcd_file_path[:-4] + '.xyz'
            save_mesh_file_path = save_mesh_folder_path + rel_pcd_file_path[:-4] + '.ply'

            if not self.autoReconstructSurface(
                pcd_file_path,
                save_pcd_file_path,
                save_mesh_file_path,
                width_tag,
                wsmin,
                wsmax,
                iters,
                use_gpu,
                False,
                overwrite
            ):
                print('[ERROR][WNNCReconstructor::autoReconstructSurfaceFolder]')
                print('\t autoReconstructSurface failed!')

                continue

        return True
