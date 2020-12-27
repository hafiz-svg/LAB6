import socket
import sys
import time
import errno
import math
from multiprocessing import Process

def process_start(s_sock):
    s_sock.send(str.encode('MY CALCULATOR'))
    while True:
        s_sock.send(str.encode("1-Square root 2-Exponential Function 3- Logaritsm"))
        data = s_sock.recv(2048).decode()
        if data == "1":
            choose = s_sock.recv(2048).decode()
            Response = math.sqrt(float(data))
            s_sock.send(bytes(str(Response),'ascii'))
        elif data == "2":
            choose = s_sock.recv(2048).decode()
            Response = math.exp(float(data))
            s_sock.send(bytes(str(Response),'ascii'))
        elif data == "3":
            choose = s_sock.recv(2048).decode()
            Response = math.log10(float(data))
            s_sock.send(bytes(str(Response),'ascii'))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

    except Exception as e:
                print('an exception occurred!')
                print(e)
                sys.exit(1)
    finally:
     	   s.close()
