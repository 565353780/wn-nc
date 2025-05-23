CPP_FOLDER_PATH=../wn-nc/wn_nc/Cpp
ANN_INSTALL_FOLDER_PATH=../wn-nc/wn_nc/Lib/ANN/build/install
BIN_FOLDER_PATH=../wn-nc/bin

mkdir ${BIN_FOLDER_PATH}

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
  -I${CPP_FOLDER_PATH}/gaussrecon_src/CLI11 -I${ANN_INSTALL_FOLDER_PATH}/include \
  -L${ANN_INSTALL_FOLDER_PATH}/lib \
  -lz -lann \
  -o ${BIN_FOLDER_PATH}/main_GaussRecon_cpu
