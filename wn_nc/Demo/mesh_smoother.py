from wn_nc.Module.mesh_smoother import MeshSmoother

def demo():
    timestamp = '20241202_18:30:59'
    mesh_folder_path = '/home/chli/github/ASDF/conditional-flow-matching/output/recon/' + timestamp + '/'
    save_mesh_folder_path = '/home/chli/github/ASDF/conditional-flow-matching/output/recon_smooth/' + timestamp + '/'
    n_iter = 100
    pass_band = 0.01
    edge_angle = 15.0
    feature_angle = 45.0
    num_workers = 12
    overwrite = False

    MeshSmoother.smoothMeshFolder(
        mesh_folder_path,
        save_mesh_folder_path,
        n_iter,
        pass_band,
        edge_angle,
        feature_angle,
        num_workers,
        overwrite)
    return True
