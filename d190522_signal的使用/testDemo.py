import time
import signal
 
 
def handle_SIGALRM(signum, frame):
    print('alarm {0}!'.format(int(time.time())))
 
 
def main():
    print('=======================begin=======================')

    signal.signal(signal.SIGINT, handle_SIGALRM)  # 注册 SIGINT 信号的处理器为handle_SIGALRM函数，按下CTrl+C会触发
    print('done')
    time.sleep(10)
    print('=======================end=========================')
 
 
if __name__ == '__main__':
    main()
