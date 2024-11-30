from wn_nc.Module.wnnc_reconstructor import WNNCReconstructor

def demo():
    pcd_file_path = '/home/chli/Downloads/sample_9.xyz'
    save_pcd_file_path = './output/sample_9_wnnc.xyz'
    width_tag = 'l0'
    wsmin = 0.01
    wsmax = 0.04
    iters = 40
    use_gpu = True
    use_tqdm = True
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
        use_tqdm,
        overwrite)
    return True
