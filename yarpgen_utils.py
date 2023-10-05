import json
import generator_utils as g
import subprocess
import uuid
import os
import random
import queue

def run_yarpgen(code_gen_queue, csmith_path, yarpgen_path):
    command_yargpen = [yarpgen_executable] + yarpgen_options
    p_yarpgen = subprocess.Popen(command_yargpen, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    g.generator_handshake(p_yarpgen)
    g.generator_clinet(p_yarpgen, "yarpgen", code_gen_queue, csmith_path, yarpgen_path)

def yarpgen_todo(p, code_gen_queue, yarpgen_path):
    _uuid = str(uuid.uuid4())
    dir_path = yarpgen_path + _uuid
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    seed = random.randint(1, 4294967296)
    mutation_seed = random.randint(1, 4294967296)

    input_seed = dir_path + "|" + str(seed) + "|" + str(mutation_seed)
    p.stdin.write(input_seed + '\n')
    p.stdin.flush()

    p.stdout.readline() 
    p.stdout.readline() 
    json_yarpgen = p.stdout.readline()

    try:
        result = json.loads(json_yarpgen)
        generator_name = result["generator"]
        return_code = result["return_code"]

        print(f"[+] Generator: {generator_name}")
        print(f"    Return Code: {return_code}")

        json_str = yarpgen_json(dir_path, _uuid)
        code_gen_queue.put(json_str)
    except json.JSONDecodeError:
        print("[!] JSON 데이터를 파싱하는데 문제가 발생했습니다.")

def yarpgen_json(file, _uuid):
    file = file + "/func.c" + "|" + "/driver.c"
    data = {
        'generator': 'yarpgen',
        'uuid' : _uuid,
        'file_path': file
    }
    json_str = json.dumps(data)
    print(json_str)
    return json_str

yarpgen_options = ["--std=c", "--mutate=all"]

<<<<<<< HEAD
yarpgen_executable = "yarpgen_forkserver" #각자 경로 설정
=======
yarpgen_executable = "yarpgen" 
>>>>>>> b5c4275 (GIMOZZI)
