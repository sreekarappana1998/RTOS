import pexpect
import threading
import time

child_server = pexpect.spawn('./server')

n=90
l=[]
for i in range(n):
    l.append(pexpect.spawn('./client 127.0.0.1'))


def whattodo(term_win):
    term_win.expect('online')
    for i in range(5):
        term_win.sendline("hi")

thread_list=[]
for j in range(n):
    t=threading.Thread(target=whattodo,args=[l[j]])
    t.daemon=True
    thread_list.append(t)
#start all threads
for k in range(n):
    thread_list[k].start()

start = time.time()
#expect
l[n-1].sendline("hi")
l[n-2].expect("hi")
print(time.time()-start)

for p in range(n):
    thread_list[p].join()


print("end")
