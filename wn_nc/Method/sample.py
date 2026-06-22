import os
import trimesh
import numpy as np

from wn_nc.Method.io import loadMeshFile
from wn_nc.Method.path import createFileFolder, removeFile


def sampleOrientPoints(
    mesh: trimesh.Trimesh,
    sample_point_num: int,
) -> np.ndarray:
    samples, face_indices = trimesh.sample.sample_surface(mesh, sample_point_num)
    normals = mesh.face_normals[face_indices]

    orient_points = np.column_stack((samples, normals))
    return orient_points

def samplePoints(
    mesh: trimesh.Trimesh,
    sample_point_num: int,
) -> np.ndarray:
    samples, _ = trimesh.sample.sample_surface(mesh, sample_point_num)
    return np.array(samples)

def samplePcdFile(
    mesh_file_path: str,
    sample_point_num: int,
    save_pcd_file_path: str,
    overwrite: bool = False,
) -> bool:
    if os.path.exists(save_pcd_file_path):
        if not overwrite:
            return True

        removeFile(save_pcd_file_path)

    assert os.path.exists(mesh_file_path)

    mesh = loadMeshFile(mesh_file_path)

    points = samplePoints(mesh, sample_point_num)

    createFileFolder(save_pcd_file_path)

    np.savetxt(save_pcd_file_path, points, fmt='%.6f', delimiter=' ')
    return True

def sampleOrientPcdFile(
    mesh_file_path: str,
    sample_point_num: int,
    save_pcd_file_path: str,
    overwrite: bool=False,
) -> bool:
    if os.path.exists(save_pcd_file_path):
        if not overwrite:
            return True

        removeFile(save_pcd_file_path)

    assert os.path.exists(mesh_file_path)

    mesh = loadMeshFile(mesh_file_path)

    orient_points = sampleOrientPoints(mesh, sample_point_num)

    createFileFolder(save_pcd_file_path)

    np.savetxt(save_pcd_file_path, orient_points, fmt='%.6f', delimiter=' ')
    return True
