import socket                     				                 #导入socket模块

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建客户机socket
clientsocket.connect(('127.0.0.1', 8000))                        #连接到服务器
while 1:                                                         #循环以接收用户输入，并发送到服务器，接收服务器的回送数据
    data = input('>')             				                 #接收用户输入数据
    clientsocket.send(data.encode()) 		                     #把数据转换为bytes对象，并发送到服务器
    if data=='exit': break             			                 #如果数据为exit，终止循环
    newdata = clientsocket.recv(1024) 	                         #接收服务器的回送数据
    print('Received from server: ',  newdata.decode() )          #输出接收到数据
clientsocket.close()                			                 #关闭客户机socket

