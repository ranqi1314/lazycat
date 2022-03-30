import threading
import queue
import time
import zipfile

def run_test(q,zf):
    while not q.empty():
        password = q.get()
        try:
            zf.extractall(pwd=password.encode("utf8"))
            print('\n[+] Password = ' + password + '\n')
            q.queue.clear()
        except Exception  as e:
            # print('[x] Not '+password)
            pass
        q.task_done()  # 处理完成

# 显示进度 （当前，总数）
def progressbar(nowprogress, toyal):
    get_progress = int((nowprogress+1)*(50/toyal))   # 显示多少>
    get_pro = int(50-get_progress)  # 显示多少-
    percent = (nowprogress+1)*(100/toyal)
    if percent > 100:
        percent = 100
    print("\r"+"["+">"*get_progress+"-"*get_pro+']'+"%.2f" %
          percent + "%", end="")

def show_test(q, qlen):
    while not q.empty():
        # print(q.qsize(),q.unfinished_tasks,qlen )
        progressbar(qlen-q.unfinished_tasks, qlen)
        time.sleep(0.2)
    progressbar(qlen, qlen)

def main():
    start = time.time()
    zf=zipfile.ZipFile('C:\\Users\\Administrator\\Desktop\\1.zip')
    threadlist = []
    # 创建队列
    q = queue.Queue()  # 不传MaxSize
    qlen = 0 # 记录队列长度
    with open('C:\\Users\\Administrator\\Desktop\\破解字典\\400W常用密码\\1pass02.txt',encoding="utf-8") as f:
        for i in f.readlines():
            q.put(i.strip("\n"))
            qlen += 1
    # 处理线程
    for x in range(0, 11):  # <=== 运行的线程数量
        th = threading.Thread(target=run_test, args=(q,zf,))
        threadlist.append(th)
    # 进度线程
    threadlist.append(threading.Thread(target=show_test, args=(q, qlen,)))
    # 运行并加入等待运行完成
    for t in threadlist:
        t.start()
    for t in threadlist:
        t.join()
    print('/n')
    end = time.time()
    print (end-start)
if __name__ == '__main__':
    print("运行")
    main()
    print("结束")

