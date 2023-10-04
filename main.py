import multiprocessing
import csmith_utils as c
import yarpgen_utils as y
import queue

def main():

    #생성된 파일 JSON데이터 큐에 모아두기
    global code_gen_queue
    code_gen_queue = multiprocessing.Queue(maxsize=1000)

    # 각각의 프로세스 생성
    csmith_process = multiprocessing.Process(target=c.run_csmith, args=(code_gen_queue,))
    yarpgen_process = multiprocessing.Process(target=y.run_yarpgen, args=(code_gen_queue,))

    # 프로세스 시작
    csmith_process.start()
    yarpgen_process.start()

    # 프로세스 종료 대기
    csmith_process.join()
    yarpgen_process.join()

main()