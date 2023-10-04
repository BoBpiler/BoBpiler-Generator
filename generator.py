import yarpgen_utils as y
import csmith_utils as c
import io
import time
import queue
import os

def generator_handshake(p):
    pay = p.stdout.readline()  # 읽은 내용의 양 끝 공백 제거
    if pay != "[+] generator client hello\n":
        print("[!] generator client hello failed")
        exit(1)
    p.stdin.write("[+] generator server hello\n")
    p.stdin.flush()
    pay = p.stdout.readline()  # 읽은 내용의 양 끝 공백 제거
    if pay != "[+] done\n":
        print("[!] generator server hello failed")
        exit(1)
    print("[+] generator handshake done!")
    p.stdin.flush()

def generator_clinet(p, generator, code_gen_queue):
    while True:
        current_size = code_gen_queue.qsize()
        if code_gen_queue.qsize() < 999:
            if generator == "csmith": #시스미스일경우 실행
                print(f"{generator} 넣을게~ 현재 큐의 크기: {current_size}")
                c.csmith_todo(p, code_gen_queue)
            elif generator == "yarpgen": # 야프젠일 경우 실행
                print(f"{generator} 넣을게~ 현재 큐의 크기: {current_size}")
                y.yarpgen_todo(p, code_gen_queue)
        else: 
            while code_gen_queue.qsize() >= 1000:
                print("Queue is full. Waiting for space...")
                time.sleep(60)  # 큐가 비어질 때까지 대기