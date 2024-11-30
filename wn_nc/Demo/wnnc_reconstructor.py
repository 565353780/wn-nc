from wn_nc.Module.wnnc_reconstructor import WNNCReconstructor

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

    wnnc_reconstructor = WNNCReconstructor()

    wnnc_reconstructor.estimateNormal(
        pcd_file_path,
        save_pcd_file_path,
        width_tag,
        wsmin,
        wsmax,
        iters,
        use_gpu,
        print_progress,
        overwrite)

    wnnc_reconstructor.reconstructSurface(
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

    wnnc_reconstructor = WNNCReconstructor()

    wnnc_reconstructor.autoReconstructSurface(
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
    pcd_folder_path = '/home/chli/github/ASDF/conditional-flow-matching/output/sample/20241129_20:39:44/'
    save_pcd_folder_path = '/home/chli/github/ASDF/conditional-flow-matching/output/normal/20241129_20:39:44/'
    save_mesh_folder_path = '/home/chli/github/ASDF/conditional-flow-matching/output/recon/20241129_20:39:44/'
    width_tag = 'l0'
    wsmin = 0.01
    wsmax = 0.04
    iters = 40
    use_gpu = True
    print_progress = True
    overwrite = False

    wnnc_reconstructor = WNNCReconstructor()

    wnnc_reconstructor.autoReconstructSurfaceFolder(
        pcd_folder_path,
        save_pcd_folder_path,
        save_mesh_folder_path,
        width_tag,
        wsmin,
        wsmax,
        iters,
        use_gpu,
        print_progress,
        overwrite)
    return True
