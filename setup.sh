cd ./wn_nc/Lib/ANN/

rm -rf build

mkdir build
cd build

cmake .. -DCMAKE_INSTALL_PREFIX=./install
make -j
make install

cd ../../../..
rm -rf bin

./wn_nc/Bash/build_GR_cpu.sh
./wn_nc/Bash/build_GR_cuda.sh

cd wn_nc/Cpp
pip install -e .

pip install tqdm
pip install pyvista==0.44.1
