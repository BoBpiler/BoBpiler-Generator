import json
import generator as g
import subprocess
import uuid
import os
import random
import queue

def run_csmith(code_gen_queue):
    # 시스미스 실행 코드
    command_csmith = [csmith_executable] + csmith_options
    p_csmtih = subprocess.Popen(command_csmith, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    g.generator_handshake(p_csmtih)
    g.generator_clinet(p_csmtih, "csmith", code_gen_queue)

def csmith_todo(p, code_gen_queue):
    _uuid = str(uuid.uuid4())
    dir_path = './' + _uuid
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_path = dir_path + '/'  + _uuid + '.c'
    
    seed = random.randint(1, 1000)
    input_seed = file_path + "|" + str(seed)
    p.stdin.write(input_seed + '\n') # 표준 입력 스트림에 값 쓰기
    p.stdin.flush()

    # 서버로부터의 응답 읽기 (필요에 따라 추가 코드 작성)
    json_str = p.stdout.readline()

    # JSON 데이터 파싱
    try:
        result = json.loads(json_str)
        generator_name = result["generator"]
        return_code = result["return_code"]

        # JSON 데이터 활용
        print(f"[+] Generator: {generator_name}")
        print(f"    Return Code: {return_code}")

        json_str = csmith_json(file_path)
        code_gen_queue.put(json_str)
    except json.JSONDecodeError:
        print("[!] JSON 데이터를 파싱하는데 문제가 발생했습니다.")

def csmith_json(file):
    data = {
        'generator': 'csmith',
        'file_path': file
    }
    json_str = json.dumps(data)
    print(json_str)
    return json_str

#Csmith 옵션들
csmith_options = [
    '--max-array-dim', '3', 
    '--max-array-len-per-dim', '10', 
    '--max-block-depth', '3', 
    '--max-block-size', '5', 
    '--max-expr-complexity', '10', 
    '--max-funcs', '3', 
    '--max-pointer-depth', '3', 
    '--max-struct-fields', '10', 
    '--max-union-fields', '10', 
    '--muls', '--safe-math', 
    '--no-packed-struct', 
    '--paranoid', 
    '--pointers', 
    '--structs', 
    '--unions', 
    '--volatiles', 
    '--volatile-pointers', 
    '--const-pointers', 
    '--global-variables', 
    '--no-builtins', 
    '--inline-function', 
    '--inline-function-prob', '50'
]

csmith_executable = "/root/BoBpiler/BoBpiler_csmith/bin/csmith" #각자 경로 설정