
import pexpect
import time

server = pexpect.spawn('./server')

j=25
c_s=[]
for i in range(j):
    c_s.append(pexpect.spawn('./client 127.0.0.1'))

c_s[j-10].expect('online')

start_time = time.time()
c_s[j-10].sendline('hi')

c_s[j-1].expect('hi')

end_time = time.time()
print(end_time - start_time)


print("end")
