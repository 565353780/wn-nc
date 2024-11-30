import os
import trimesh
import numpy as np
from typing import Union

def loadPoints(pcd_file_path: str) -> Union[np.ndarray, None]:
    pcd_file_format = os.path.splitext(pcd_file_path)[-1]
    if pcd_file_format == '.xyz':
        points_normals = np.loadtxt(pcd_file_path)
        return points_normals[:, :3]

    if pcd_file_format in ['.ply', '.obj']:
        pcd = trimesh.load(pcd_file_path, process=False)
        return np.array(pcd.vertices)

    if pcd_file_format == '.npy':
        pcd = np.load(pcd_file_path)
        return pcd[:, :3]

    print('[ERROR][io::loadPoints]')
    print('\t the pcd file must be have extension xyz/ply/obj/npy!')
    print('\t pcd_file_path:', pcd_file_path)

    return None
