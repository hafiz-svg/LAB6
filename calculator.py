import socket

def get_input(ClientSocket):
   no = input("Enter Number:")
   ClientSocket.send(no.encode())

ClientSocket = socket.socket()
host = '192.168.56.105'
port = 8888

try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

response = ClientSocket.recv(1024).decode()
print(response)
while True:
    show = ClientSocket.recv(1024).decode()
    print(show)
    Input = input('Your input:')
    ClientSocket.send(str.encode(Input))
    if Input == "1":
        get_input(ClientSocket)
    elif Input == "2":
        get_input(ClientSocket)
    elif Input == "3":
        get_input(ClientSocket)
    else:
         print ("\n Error : Mathematical Operations Input doesn't match With The List!")
    Response = ClientSocket.recv(2048).decode
    print("Result:",Response)
ClientSocket.close()

