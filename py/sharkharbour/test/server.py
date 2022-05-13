import socket
import threading
import time
import os

# 字典集返回数据
def getAnswer(c_data):
    words = {
        'how are you?': 'Fine,thank you.',
        'hi': 'hello',
        'hello': 'hello',
        'how old are you?': '20',
        'what is your name?': 'Andel',
        "what's your name?": 'Andel',
        'where do you work?': 'Beijing',
        'bye': 'Bye'
    }
    flag = 0
    lst = list(words.keys())
    for i in range(len(lst)):
        if len(os.path.commonprefix([c_data, lst[i]])) > len(lst[i]) * 0.8:
            flag = 1
            return words.get(lst[i])
    if flag == 0:
        return "Sorry for that, I don't understand what you say."
# 接收信息

def recv_msg(clientsocket, clientaddress):
    while True:
        recv_data = clientsocket.recvfrom(1024)
        ip, port = clientaddress
        print('Received from client(' + str(ip) + ':' +
              str(port) + '):' + recv_data[0].decode())
        t_send = threading.Thread(target=send_msg, args=(
            clientsocket, clientaddress, recv_data[0]))
        t_send.start()
# 发送信息


def send_msg(clientsocket, clientaddress, recv_data):
    ip, port = clientaddress
    time_data = str(time.asctime(time.localtime()) + "\n")
    ans_data = getAnswer(recv_data.decode())
    send_data = time_data + ans_data

    clientsocket.sendto(send_data.encode(), (ip, port))
#


def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('127.0.0.1', 8000))
    serversocket.listen(5)
    print('Server connecting....')
    while True:
        clientsocket, clientaddress = serversocket.accept()
        t_recv = threading.Thread(
            target=recv_msg, args=(clientsocket, clientaddress))
        t_recv.start()
        # print(str(len(threading.enumerate())) +  "threads are working")
        #
        # if (len(threading.enumerate())<2):
        #     break

    serversocket.close()


if __name__ == "__main__":
    main()
