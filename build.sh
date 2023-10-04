#csmith build
cd csmith_forkserver
apt install g++ cmake m4
cmake -DCMAKE_INSTALL_PREFIX=./ .
make && make install
cd ..

#PATH 환경 변수에 등록된 디렉토리에 바이너리 넣기(경로없이 사용)
sudo cp $PWD/csmith_forkserver/bin/csmith /usr/local/bin/
sudo cp $PWD/csmith_forkserver/bin/csmith /bin/


#yarpgen build
cd yarpgen_forkserver
mkdir build && cd build
cmake ..
make 
cd ../../

sudo cp $PWD/yarpgen_forkserver/build/yarpgen /usr/local/bin/
sudo cp $PWD/yarpgen_forkserver/build/yarpgen /bin/
