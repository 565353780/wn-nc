from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension, CppExtension

cpp_folder_path = '../wn-nc/wn_nc/Cpp/'

setup(
    name='wn_treecode',
    packages=['wn_treecode'],
    ext_modules=[
        CUDAExtension('wn_treecode._cuda', [
            cpp_folder_path + 'wn_treecode/wn_treecode_cuda/wn_treecode_cuda_torch_interface.cu',
            cpp_folder_path + 'wn_treecode/wn_treecode_cuda/wn_treecode_cuda_kernels.cu',
        ],
        extra_compile_args={'cxx': ['-O3'],
                            'nvcc': ['-O3']}),

        CppExtension('wn_treecode._cpu', [
            cpp_folder_path + 'wn_treecode/wn_treecode_cpu/wn_treecode_cpu_torch_interface.cpp',
            cpp_folder_path + 'wn_treecode/wn_treecode_cpu/wn_treecode_cpu_treeutils.cpp',
            cpp_folder_path + 'wn_treecode/wn_treecode_cpu/wn_treecode_cpu_kernels.cpp',
        ],
        extra_compile_args={'cxx': ['-O3', '-fopenmp']}),

        ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
