from wn_nc.Demo.wnnc_reconstructor import (
    demo_normal_recon,
    demo_auto_recon,
    demo_auto_recon_folder,
)
from wn_nc.Demo.mesh_smoother import demo as demo_smooth_mesh_folder
from time import sleep

if __name__ == "__main__":
    # demo_normal_recon()
    # demo_auto_recon()
    while True:
        demo_auto_recon_folder()
        demo_smooth_mesh_folder()
        sleep(10)
