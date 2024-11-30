cd ./wn_nc/Lib/ANN/

rm -rf build

mkdir build
cd build

cmake .. -DCMAKE_INSTALL_PREFIX=./install
make -j
make install

cd ../../../..
./build_GR_cpu.sh
./build_GR_cuda.sh

cd wn_nc/Cpp
pip install -e .
