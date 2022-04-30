from socket import socket
from threading import Thread
from sys import argv

def main():
    exit("Usage: ./proxy.py [local_host] [local_port] [remote_host] [remote_port] [receive_first]") if len(argv) !=6 else 0
    
    # 为监听客户端创建的socket
    lhost, lport = argv[1], int(argv[2])
    # 为连接服务端创建的socket
    rhost, rport = argv[3], int(argv[4])
    # 连接建立后是否由服务端先向客户端发送信息，True代表是
    receive_first=True if argv[5] =="True" else False
    
    server_loop(lhost,lport,rhost,rport,receive_first)

def server_loop(lhost,lport,rhost,rport,receive_first):
    s = socket(0x02, 0x01, 0x00)
    s.setsockopt(0xFFFF, 0x04, 1)
    s.bind((lhost, lport))
    s.listen(5)
    # 开始监听后，等待来自客户端的连接
    while True:
        print("waiting for local client connection")
        c, addr = s.accept()
        print("[*]Received connection from %s:%d"%(addr[0],addr[1]))
        # 收到来自客户端的链接后，就开启一个代理线程
        proxy = Thread(target = proxy_handler, args=(c, rhost,rport, receive_first))
        proxy.start()

# 定义代理线程
def proxy_handler(c,rhost,rport,receive_first):
    # 创建一个socket以连接服务端
    remote_s=socket(0x02, 0x01, 0x00)
    remote_s.connect((rhost, rport))
    # 如果需要服务端先向客户端发送信息
    if receive_first:
        remote_buffer = receive_from(remote_s)
        print("[<==]Receive %d bytes from remote host receive first"%len(remote_buffer))
        # 下面两行是对收到信息的处理，得到有用的信息（做十六进制处理和自定义的处理，如果不需要，可以省略）
        hexdump(remote_buffer)
        remote_buffer=remote_buffer
        # 如果处理后仍有有用的信息，则发送给客户端
        if len(remote_buffer):
            c.sendall(remote_buffer)
            print("[==>]Sending %d bytes to local hosts"%len(remote_buffer))
    while True:
        # 从客户端接收请求信息，由于本文中的例子不需要客户端发送请求，所以注释掉这一段
        # client_buffer=receive_from(client.socket)
        # print "[<==]Receive %d bytes from localhost"%len(local_buffer)
        # #下面两行是对收到信息的处理，得到有用的信息（做十六进制处理和自定义的处理，如果不需要，可以省略）
        # hexdump(client_buffer)
        # remote_buffer=request_handler(client_buffer)
        # #如果处理后仍有有用的请求信息，则发送给服务端
        # if len(client_buffer):
        #     remote_socket.sendall(client_buffer)
        #     print "[==>]Sending %d to remote"%len(local_buffer)
        remote_buffer=receive_from(remote_s)
        print("[<==]Receive %d bytes from remote host receive first"%len(remote_buffer))
        # 下面两行是对收到信息的处理，得到有用的信息（做十六进制处理和自定义的处理，如果不需要，可以省略）
        hexdump(remote_buffer)
        remote_buffer=remote_buffer
        # 如果处理后仍有有用的信息，则发送给客户端
        if len(remote_buffer):
            c.sendall(remote_buffer)
            print("[==>]Sending %d bytes to local hosts"%len(remote_buffer))
        
        # 如果从服务端和客户端都不再收到信息了，就关闭连接（由于本文的例子需要等待服务端继续发送信息，所以不关闭连接，注释掉这一段）
        # if not (len(local_buffer) or len(remote_buffer)):
        #     client_socket.close()
        #     remote_socket.close()
        #     print "[*]No more data. Closing connections"
        #     break

# 上面的代码中还有一些小的方法没有定义：
# 由于是TCP代理，所以接收的信息块可能比较大，所以不直接用.recv()方法，而是写一个receive_from方法来获取发送的全部信息
def receive_from(s :socket):
    buffer = ""
    s.settimeout(2)
    try:
        while True:
            data = s.recv(4096)
            if not data:
                break
            buffer += data
    except:
        pass
    return buffer

# 十六进制处理函数，无需深究，如果不需十六进制转换，可以省略
def hexdump(src :bytes):
    length, result, digits = 32, [], 2
    for i in range(0, len(src), length):
        s = src[i : i+length]
        hexa = ''.join(["%02X "%x for x in s])
        text = "".join([chr(x if 0x20 <= x < 0x7F else 0x2E) for x in s])
        result.append("%08X  %-*s %s" % (i, length * (digits + 1), hexa, text))
    print('\n'.join(result))

# 运行主函数
if __name__ == "__main__":
    main()
