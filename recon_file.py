import os
from time import sleep

from wn_nc.Module.wnnc_reconstructor import WNNCReconstructor
from wn_nc.Module.mesh_smoother import MeshSmoother


def reconAndSmoothFile():
    root_folder_path = "/home/chli/chLi/Dataset/TRELLIS/mash_gen_process/"
    save_pcd_folder_path = "/home/chli/chLi/Dataset/TRELLIS/normal_mash_gen/"
    save_mesh_folder_path = "/home/chli/chLi/Dataset/TRELLIS/recon_mash_gen/"
    save_smooth_mesh_folder_path = (
        "/home/chli/chLi/Dataset/TRELLIS/recon_smooth_mash_gen/"
    )
    shape_id_list = os.listdir(root_folder_path)
    for shape_id in shape_id_list:
        pcd_file_path = root_folder_path + shape_id + "/100_train_pcd.ply"
        save_pcd_file_path = save_pcd_folder_path + shape_id + "_pcd.ply"
        save_mesh_file_path = save_mesh_folder_path + shape_id + "_recon.ply"
        save_smooth_mesh_file_path = (
            save_smooth_mesh_folder_path + shape_id + "_recon_smooth.ply"
        )

        width_tag = "l0"
        wsmin = 0.01
        wsmax = 0.04
        iters = 40
        use_gpu = True

        n_iter = 100
        pass_band = 0.01
        edge_angle = 15.0
        feature_angle = 45.0

        print_progress = True
        overwrite = False

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
            overwrite,
        )

        MeshSmoother.smoothMesh(
            save_mesh_file_path,
            save_smooth_mesh_file_path,
            n_iter,
            pass_band,
            edge_angle,
            feature_angle,
            overwrite,
        )
    return True


if __name__ == "__main__":
    while True:
        reconAndSmoothFile()
        break
        sleep(10)
