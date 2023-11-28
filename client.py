import socket

MAX_PACKET = 1024


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        my_socket.connect(('127.0.0.1', 8820))
        while True:
            inputted = input("4 bytes request only: ")
            my_socket.send(str(inputted).encode())
            a = my_socket.recv(MAX_PACKET).decode()
            print(a)
            if a == "EXITED SERVER":
                break
    except socket.error as err:
        print('Received socket error:', str(err))


if __name__ == '__main__':
    main()