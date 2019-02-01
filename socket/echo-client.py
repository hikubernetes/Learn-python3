import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立一个连接
s.connect(('127.0.0.1', 9999))
#接收消息
print(s.recv(1024).decode('utf-8'))
for data in [b'bob', b'echo', b'mike']:
    #发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
