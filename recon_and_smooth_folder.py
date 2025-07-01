from time import sleep

from wn_nc.Module.wnnc_reconstructor import WNNCReconstructor
from wn_nc.Module.mesh_smoother import MeshSmoother


def reconAndSmoothFolder():
    timestamp = "20241218_15:08:27"
    iter_idx = 1
    pcd_folder_path = (
        "../conditional-flow-matching/output/sample/"
        + timestamp
        + "/iter_"
        + str(iter_idx)
        + "/"
    )
    save_pcd_folder_path = (
        "../conditional-flow-matching/output/normal/"
        + timestamp
        + "/iter_"
        + str(iter_idx)
        + "/"
    )
    save_mesh_folder_path = (
        "../conditional-flow-matching/output/recon/"
        + timestamp
        + "/iter_"
        + str(iter_idx)
        + "/"
    )
    save_smooth_mesh_folder_path = (
        "../conditional-flow-matching/output/recon_smooth/"
        + timestamp
        + "/iter_"
        + str(iter_idx)
        + "/"
    )

    pcd_folder_path = "../conditional-flow-matching/output/sample/" + timestamp + "/"
    save_pcd_folder_path = (
        "../conditional-flow-matching/output/normal/" + timestamp + "/"
    )
    save_mesh_folder_path = (
        "../conditional-flow-matching/output/recon/" + timestamp + "/"
    )
    save_smooth_mesh_folder_path = (
        "../conditional-flow-matching/output/recon_smooth/" + timestamp + "/"
    )

    pcd_folder_path = "../conditional-flow-matching/output/sample/" + timestamp + "/"
    save_pcd_folder_path = (
        "../conditional-flow-matching/output/normal/" + timestamp + "/"
    )
    save_mesh_folder_path = (
        "../conditional-flow-matching/output/recon/" + timestamp + "/"
    )
    save_smooth_mesh_folder_path = (
        "../conditional-flow-matching/output/recon_smooth/" + timestamp + "/"
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
        overwrite,
    )

    MeshSmoother.smoothMeshFolder(
        save_mesh_folder_path,
        save_smooth_mesh_folder_path,
        n_iter,
        pass_band,
        edge_angle,
        feature_angle,
        num_workers,
        overwrite,
    )
    return True


if __name__ == "__main__":
    while True:
        reconAndSmoothFolder()
        break
        sleep(10)
