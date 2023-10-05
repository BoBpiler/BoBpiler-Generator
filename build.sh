#csmith build
# sudo apt-get update
# sudo apt-get install libnlohmann-json-dev

cd csmith_forkserver
sudo apt install g++ cmake m4
cmake -DCMAKE_INSTALL_PREFIX=./ .
make -j 4 && make install
cd ..

#PATH 환경 변수에 등록된 디렉토리에 바이너리 넣기(경로없이 사용)
sudo cp $PWD/csmith_forkserver/bin/csmith /usr/local/bin/csmith_forkserver
sudo cp $PWD/csmith_forkserver/bin/csmith /bin/csmith_forkserver


#yarpgen build
cd yarpgen_forkserver
mkdir build && cd build
cmake ..
make -j 4
cd ../../

sudo cp $PWD/yarpgen_forkserver/build/yarpgen /usr/local/bin/yarpgen_forkserver
sudo cp $PWD/yarpgen_forkserver/build/yarpgen /bin/yarpgen_forkserver
