# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import socket
import select
import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # 创建socket对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接到服务器
    client_socket.connect(('127.0.0.1', 8002))

    # 设置为非阻塞模式
    client_socket.setblocking(0)

    # 输入数据并发送
    while True:
        # 监听键盘输入和socket接收
        inputs = [sys.stdin, client_socket]
        readable, writable, exceptional = select.select(inputs, [], [])

        for r in readable:
            if r is sys.stdin:
                # 从键盘输入数据
                data = sys.stdin.readline().strip()
                if data:
                    # 发送数据
                    print("send --- ", data)
                    client_socket.send(data.encode())
            elif r is client_socket:
                # 从服务器接收数据
                data = client_socket.recv(1024)
                if data:
                    print("Received:", data.decode())

    client_socket.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
