import json
import generator_utils as g
import subprocess
import uuid
import os
import random
import queue

def run_csmith(code_gen_queue, csmith_path, yarpgen_path):
    command_csmith = [csmith_executable] + csmith_options
    p_csmtih = subprocess.Popen(command_csmith, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    g.generator_handshake(p_csmtih)
    g.generator_clinet(p_csmtih, "csmith", code_gen_queue, csmith_path, yarpgen_path)

def csmith_todo(p, code_gen_queue, csmith_path):
    _uuid = str(uuid.uuid4())
    dir_path = csmith_path + _uuid
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_path = dir_path + '/'  + _uuid + '.c'
    
    seed = random.randint(1, 4294967296)
    input_seed = file_path + "|" + str(seed)
    p.stdin.write(input_seed + '\n')
    p.stdin.flush()

    json_str = p.stdout.readline()

    try:
        result = json.loads(json_str)
        generator_name = result["generator"]
        return_code = result["return_code"]

        print(f"[+] Generator: {generator_name}")
        print(f"    Return Code: {return_code}")

        json_str = csmith_json(file_path, _uuid)
        code_gen_queue.put(json_str)
    except json.JSONDecodeError:
        print("[!] JSON 데이터를 파싱하는데 문제가 발생했습니다.")

def csmith_json(file ,_uuid):
    data = {
        'generator': 'csmith',
        'uuid' : _uuid,
        'file_path': file
    }
    json_str = json.dumps(data)
    print(json_str)
    return json_str

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

<<<<<<< HEAD
# 절대경로
csmith_executable = "csmith_forkserver"
=======
csmith_executable = "csmith"
>>>>>>> b5c4275 (GIMOZZI)
