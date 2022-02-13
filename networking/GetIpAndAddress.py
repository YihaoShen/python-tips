# 原理:通过向dns服务器发送一个UDP报文段，获取其中的IP地址(该地址为局域网中的地址)
import socket


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


if __name__ == "__main__":
    print(main())
