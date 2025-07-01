import os
import pyvista as pv
from tqdm import tqdm
from multiprocessing import Pool

from wn_nc.Method.path import createFileFolder, removeFile


class MeshSmoother(object):
    def __init__(self) -> None:
        return

    @staticmethod
    def smoothMesh(
        mesh_file_path: str,
        save_mesh_file_path: str,
        n_iter: int = 100,
        pass_band: float = 0.01,
        edge_angle: float = 15.0,
        feature_angle: float = 45.0,
        overwrite: bool = False,
    ) -> bool:
        if not os.path.exists(mesh_file_path):
            print("[ERROR][MeshSmoother::smoothMesh]")
            print("\t mesh file not exist!")
            print("\t mesh_file_path:", mesh_file_path)

            return False

        if os.path.exists(save_mesh_file_path):
            if not overwrite:
                return True

            removeFile(save_mesh_file_path)

        mesh = pv.read(mesh_file_path)

        smoothed_mesh = mesh.smooth_taubin(
            n_iter=n_iter,
            pass_band=pass_band,
            edge_angle=edge_angle,
            feature_angle=feature_angle,
            normalize_coordinates=True,
        )

        createFileFolder(save_mesh_file_path)

        smoothed_mesh.save(save_mesh_file_path)

        return True

    @staticmethod
    def smoothMeshWithInputs(inputs: list) -> bool:
        mesh_file_path = inputs[0]
        save_mesh_file_path = inputs[1]
        n_iter = inputs[2]
        pass_band = inputs[3]
        edge_angle = inputs[4]
        feature_angle = inputs[5]
        overwrite = inputs[6]

        if not MeshSmoother.smoothMesh(
            mesh_file_path,
            save_mesh_file_path,
            n_iter,
            pass_band,
            edge_angle,
            feature_angle,
            overwrite,
        ):
            print("[ERROR][MeshSmoother::smoothMeshWithInputs]")
            print("\t smoothMesh failed!")

            return False

        return True

    @staticmethod
    def smoothMeshFolder(
        mesh_folder_path: str,
        save_mesh_folder_path: str,
        n_iter: int = 100,
        pass_band: float = 0.01,
        edge_angle: float = 15.0,
        feature_angle: float = 45.0,
        num_workers: int = 12,
        overwrite: bool = False,
    ) -> bool:
        inputs_list = []
        for root, _, files in os.walk(mesh_folder_path):
            for file in files:
                file_extension = os.path.splitext(file)[-1]
                if file_extension not in [".ply", ".obj"]:
                    continue

                rel_mesh_folder_path = os.path.relpath(root, mesh_folder_path) + "/"

                mesh_file_path = root + "/" + file
                save_mesh_file_path = (
                    save_mesh_folder_path + rel_mesh_folder_path + file
                )

                inputs = [
                    mesh_file_path,
                    save_mesh_file_path,
                    n_iter,
                    pass_band,
                    edge_angle,
                    feature_angle,
                    overwrite,
                ]

                inputs_list.append(inputs)

        print("[INFO][MeshSmoother::smoothMeshFolder]")
        print("\t start smooth mesh for shapes in folder...")
        with Pool(num_workers) as pool:
            results = list(
                tqdm(
                    pool.imap(MeshSmoother.smoothMeshWithInputs, inputs_list),
                    total=len(inputs_list),
                    desc="Processing",
                )
            )

        return True
