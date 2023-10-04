# BoBpiler-Generator
Code Generator For BoBpiler
안녕하세요 밥파일러 퍼저의 첫부분 코드생성기입니다. 우선 리눅스의 cmsith와 yarpgen에다가 forkserver를 적용했습니다.
```
git clone --recursive https://github.com/BoBpiler/BoBpiler-Generator.git
cd BoBpiler-Generator
chmod +x ./build.sh
./build.sh

mkdir tmp && cd tmp
python3 ../main.py
```
깜빡하고 안넣었는데 csmith와 yarpgen 디렉토리에 들어가서 git checkout으로 브랜치를 변경해줘야한다. 
