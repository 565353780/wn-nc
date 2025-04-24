from wn_nc.Module.wnnc_reconstructor import WNNCReconstructor


def estimateNormal():
    pcd_file_path = 'your_pcd_file, support [.xyz, .ply, .obj, .npy]'
    save_pcd_file_path = 'save pcd file with estimated normal, support [.ply, .obj]'

    width_tag = 'l0'
    wsmin = 0.01
    wsmax = 0.04
    iters = 40
    use_gpu = True
    print_progress = True
    overwrite = False

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

    return True

if __name__ == "__main__":
    estimateNormal()
