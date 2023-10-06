#csmith build
# sudo apt-get update
# sudo apt-get install libnlohmann-json-dev

cd csmith_forkserver
sudo apt install g++ cmake m4
cmake -S . -B build
cd build
make -j 4
mv ./src/csmith ./
cd ../../

#PATH 환경 변수에 등록된 디렉토리에 바이너리 넣기(경로없이 사용)
sudo cp $PWD/csmith_forkserver/build/csmith /usr/local/bin/csmith_forkserver
sudo cp $PWD/csmith_forkserver/build/csmith /bin/csmith_forkserver


#yarpgen build
cd yarpgen_forkserver
mkdir build && cd build
cmake ..
make -j 4
cd ../../

sudo cp $PWD/yarpgen_forkserver/build/yarpgen /usr/local/bin/yarpgen_forkserver
sudo cp $PWD/yarpgen_forkserver/build/yarpgen /bin/yarpgen_forkserver
