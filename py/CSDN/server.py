#!/usr/bin/python
from socket import socket
from sys import argv
import threading

#初始化请求队列，以便同时对多个客户端进行应答
request_queue = []

#对请求列表进行操作，对请求队列中的socket连接进行处理
def client_handler(request_queue):
    #如果有已建立的socket连接，则提示用户输入想要发送的信息内容
    msg = 0
    if request_queue:
        msg = input("message:")
    #如果用户输入的是"exit",就关闭所有的连接，否则就向所有已连接的客户端发送输入的内容
    if msg == "exit":
        for client_socket in request_queue:
            client_socket.close()
            break
    else:
        #由于本例中只是简单地发送消息，所以直接用send方法，如果是比较耗时的操作，可以创建对每个request创建一个线程
        for client_socket in request_queue:
            client_socket.send(msg.encode())
            print("sending '%s' to proxy"%msg)

#每1秒检测一次，是否有新的来自客户端的连接，如果有，就放进请求列表中去，然后对请求列表进行操作
def connection(server):
    global request_queue
    while True:
        server.settimeout(1)
        try:
            client_socket,addr = server.accept()
            request_queue.append(client_socket)
            print("[*]Connection received from %s:%d"%(addr[0],addr[1]))
        except:
            pass
        client_handler(request_queue)

#主函数
def main():
    if len(argv) != 3:
        exit("./echo_socket_server.py [listen_ip] [listen_port]")
    
    server = socket(0x02, 0x01, 0x00)
    server_ip, server_port = argv[1], int(argv[2])
    server.bind((server_ip, server_port))
    server.listen(5)
    #开启一个线程，检测连接并对现有连接进行操作
    c_thread = threading.Thread(target = connection,args=(server,))
    c_thread.start()

if __name__ == "__main__":
    main()
