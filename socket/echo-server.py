# _author_ = "CHANRBO"
# _*_ coding=utf-8 _*_
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('waiting for connection...')
while True:
    socket, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
def tcplink(sock, addr):
    print('Accept new connction from %s:%s...' %addr)
    sock.send(b'welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send('hell, %s' % data.decode('utf-8').encode('utf-8'))
    sock.close()
    print('connection from %s:%s closed.' % addr)
