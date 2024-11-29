import os
import torch
from platform import system
from setuptools import find_packages, setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension, CppExtension

SYSTEM = system()

wnnc_root_path = os.getcwd() + "/wn_nc/Cpp/"
wnnc_src_path = wnnc_root_path + "wn_treecode/"
wnnc_include_dirs = [
    wnnc_root_path + "wn_treecode_cpu",
    wnnc_root_path + "wn_treecode_cuda",
]

wnnc_extra_compile_args = [
    "-O3",
    "-DCMAKE_BUILD_TYPE Release",
    "-D_GLIBCXX_USE_CXX11_ABI=0",
    "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
]

if SYSTEM == 'Darwin':
    wnnc_extra_compile_args.append("-std=c++17")
elif SYSTEM == 'Linux':
    wnnc_extra_compile_args.append("-std=c++17")

if torch.cuda.is_available():
    os.environ["TORCH_CUDA_ARCH_LIST"] = "6.0;6.1;6.2;7.0;7.5;8.0;8.6;8.9"

    extra_compile_args = {
        "cxx": wnnc_extra_compile_args + ["-DUSE_CUDA"],
        "nvcc": [
            "-O3",
            "-Xfatbin",
            "-compress-all",
            "-DUSE_CUDA",
            "-std=c++17",
        ],
    }

    wnnc_module = CUDAExtension(
        name="wnnc_cpp",
        sources=[
            wnnc_src_path + 'wn_treecode_cuda/wn_treecode_cuda_torch_interface.cu',
            wnnc_src_path + 'wn_treecode_cuda/wn_treecode_cuda_kernels.cu',
        ],
        include_dirs=wnnc_include_dirs,
        extra_compile_args=extra_compile_args,
    )

else:
    wnnc_module = CppExtension(
        name="wnnc_cpp",
        sources=[
            wnnc_src_path + 'wn_treecode_cpu/wn_treecode_cpu_torch_interface.cpp',
            wnnc_src_path + 'wn_treecode_cpu/wn_treecode_cpu_treeutils.cpp',
            wnnc_src_path + 'wn_treecode_cpu/wn_treecode_cpu_kernels.cpp',
        ],
        include_dirs=wnnc_include_dirs,
        extra_compile_args=wnnc_extra_compile_args + ['-fopenmp'],
    )

setup(
    name="wn_treecode",
    version="1.0.0",
    author="Changhao Li",
    packages=find_packages(),
    ext_modules=[wnnc_module],
    cmdclass={"build_ext": BuildExtension},
    include_package_data=True,
)
