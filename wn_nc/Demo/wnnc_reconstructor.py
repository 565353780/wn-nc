import os

from wn_nc.Module.wnnc_reconstructor import WNNCReconstructor
from wn_nc.Method.sample import samplePcdFile

# To pin these demos to a specific GPU, launch with:
#   CUDA_VISIBLE_DEVICES=7 python -m wn_nc.Demo.wnnc_reconstructor

# shared test mesh and sampled point cloud for all three algorithms (g3r / agr / wn-nc)
MESH_FILE_PATH = os.path.expanduser(
    "~/chLi/COS/mm-users-data-1303205185/lichanghao/chLi/Dataset/"
    "final_postprocess_collected/000.png.glb"
)
SAMPLE_POINT_NUM = 3000000
SHARED_PCD_FILE_PATH = os.path.expanduser(
    "~/chLi/COS/mm-users-data-1303205185/lichanghao/chLi/Dataset/"
    "final_postprocess_collected/000_3M.xyz"
)


def demo_shared_mesh_recon():
    pcd_file_path = SHARED_PCD_FILE_PATH
    save_pcd_file_path = './output/000_wnnc.xyz'
    save_mesh_file_path = './output/000_wnnc_gauss.ply'
    width_tag = 'l0'
    wsmin = 0.01
    wsmax = 0.04
    iters = 40
    use_gpu = True
    print_progress = True
    overwrite = True

    samplePcdFile(MESH_FILE_PATH, SAMPLE_POINT_NUM, pcd_file_path, False)

    WNNCReconstructor.autoReconstructSurface(
        pcd_file_path,
        save_pcd_file_path,
        save_mesh_file_path,
        width_tag,
        wsmin,
        wsmax,
        iters,
        use_gpu,
        print_progress,
        overwrite)
    return True


def demo_normal_recon():
    pcd_file_path = '/home/chli/Downloads/sample_9.xyz'
    save_pcd_file_path = './output/sample_9_wnnc.xyz'
    save_mesh_file_path = './output/sample_9_wnnc_gauss.ply'
    width_tag = 'l0'
    wsmin = 0.01
    wsmax = 0.04
    iters = 40
    use_gpu = True
    print_progress = True
    overwrite = True

    WNNCReconstructor.estimateNormal(
        pcd_file_path,
        save_pcd_file_path,
        width_tag,
        wsmin,
        wsmax,
        iters,
        use_gpu,
        print_progress,
        overwrite)

    WNNCReconstructor.reconstructSurface(
        save_pcd_file_path,
        save_mesh_file_path,
        use_gpu,
        overwrite
    )
    return True

def demo_auto_recon():
    pcd_file_path = '/home/chli/Downloads/sample_9.xyz'
    save_pcd_file_path = './output/sample_9_wnnc.xyz'
    save_mesh_file_path = './output/sample_9_wnnc_gauss.ply'
    width_tag = 'l0'
    wsmin = 0.01
    wsmax = 0.04
    iters = 40
    use_gpu = True
    print_progress = True
    overwrite = True

    WNNCReconstructor.autoReconstructSurface(
        pcd_file_path,
        save_pcd_file_path,
        save_mesh_file_path,
        width_tag,
        wsmin,
        wsmax,
        iters,
        use_gpu,
        print_progress,
        overwrite)
    return True

def demo_auto_recon_folder():
    timestamp = '20241202_18:30:59'
    pcd_folder_path = '/home/chli/github/ASDF/conditional-flow-matching/output/sample/' + timestamp + '/'
    save_pcd_folder_path = '/home/chli/github/ASDF/conditional-flow-matching/output/normal/' + timestamp + '/'
    save_mesh_folder_path = '/home/chli/github/ASDF/conditional-flow-matching/output/recon/' + timestamp + '/'
    width_tag = 'l0'
    wsmin = 0.01
    wsmax = 0.04
    iters = 40
    use_gpu = True
    num_workers = 12
    overwrite = False

    WNNCReconstructor.autoReconstructSurfaceFolder(
        pcd_folder_path,
        save_pcd_folder_path,
        save_mesh_folder_path,
        width_tag,
        wsmin,
        wsmax,
        iters,
        use_gpu,
        num_workers,
        overwrite)
    return True
