import json
import generator as g
import subprocess
import uuid
import os
import random
import queue

def run_yarpgen(code_gen_queue):
    # 야프젠 실행 코드
    command_yargpen = [yarpgen_executable] + yarpgen_options
    p_yarpgen = subprocess.Popen(command_yargpen, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    g.generator_handshake(p_yarpgen)
    g.generator_clinet(p_yarpgen, "yarpgen", code_gen_queue)

def yarpgen_todo(p, code_gen_queue):
    dir_path = './' + str(uuid.uuid4())
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    seed = random.randint(1, 1000)
    mutation_seed = random.randint(1, 1000) 

    input_seed = dir_path + "|" + str(seed) + "|" + str(mutation_seed)
    p.stdin.write(input_seed + '\n') # 표준 입력 스트림에 값 쓰기
    p.stdin.flush()

    # 서버로부터의 응답 읽기 (필요에 따라 추가 코드 작성)
    p.stdout.readline() #값 받고 버리기
    p.stdout.readline() #값 받고 버리기
    json_yarpgen = p.stdout.readline()

    # JSON 데이터 파싱
    try:
        result = json.loads(json_yarpgen)
        generator_name = result["generator"]
        return_code = result["return_code"]

        # JSON 데이터 활용
        print(f"[+] Generator: {generator_name}")
        print(f"    Return Code: {return_code}")

        json_str = yarpgen_json(dir_path)
        code_gen_queue.put(json_str)
    except json.JSONDecodeError:
        print("[!] JSON 데이터를 파싱하는데 문제가 발생했습니다.")

def yarpgen_json(file):
    file = file + "/func.c" + "|" + "/driver.c"
    data = {
        'generator': 'yarpgen',
        'file_path': file
    }
    json_str = json.dumps(data)
    print(json_str)
    return json_str

#Yarpgen 옵션들
yarpgen_options = ["--std=c", "--mutate=all"]

yarpgen_executable = "/root/BoBpiler/BoBpiler_yarpgen/build/yarpgen" #각자 경로 설정
