CPP_FOLDER_PATH=../wn-nc/wn_nc/Cpp

g++ -O3 -fopenmp \
  ${CPP_FOLDER_PATH}/gaussrecon_src/Cube.cpp \
  ${CPP_FOLDER_PATH}/gaussrecon_src/MarchingCubes.cpp \
  ${CPP_FOLDER_PATH}/gaussrecon_src/Octree.cpp \
  ${CPP_FOLDER_PATH}/gaussrecon_src/plyfile.cpp \
  ${CPP_FOLDER_PATH}/gaussrecon_src/Geometry.cpp \
  ${CPP_FOLDER_PATH}/gaussrecon_src/Mesh.cpp \
  ${CPP_FOLDER_PATH}/gaussrecon_src/main_GaussRecon_cpu.cpp \
  ${CPP_FOLDER_PATH}/gaussrecon_src/ply.cpp \
  ${CPP_FOLDER_PATH}/gaussrecon_src/ReconOctNode.cpp \
  ${CPP_FOLDER_PATH}/gaussrecon_src/ANNAdapter.cpp \
  ${CPP_FOLDER_PATH}/wn_treecode/wn_treecode_cpu/wn_treecode_cpu_kernels.cpp \
  ${CPP_FOLDER_PATH}/wn_treecode/wn_treecode_cpu/wn_treecode_cpu_treeutils.cpp \
  -I${CPP_FOLDER_PATH}/wn_treecode/wn_treecode_cpu/ \
  -I${CPP_FOLDER_PATH}/gaussrecon_src/CLI11 -I${CPP_FOLDER_PATH}/gaussrecon_src/ANN/include \
  -L${CPP_FOLDER_PATH}/gaussrecon_src/ANN/lib \
  -lz -lANN \
  -o main_GaussRecon_cpu
