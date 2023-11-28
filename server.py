import socket
from datetime import datetime
from random import randint

IP = '0.0.0.0'
PORT = 8820
QUEUE_SIZE = 1
MAX_PACKET = 1024


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((IP, PORT))
        server_socket.listen(QUEUE_SIZE)
        print('Server is up and running...')
        while True:
            comm_socket, client_address = server_socket.accept()
            print(f'Connected to {client_address}')
            try:
                while True:
                    request = comm_socket.recv(MAX_PACKET).decode()
                    if request == "TIME":
                        current_time = datetime.now()
                        hour = current_time.hour
                        minute = current_time.minute
                        second = current_time.second
                        response = ' '.join(map(str, [hour, minute, second]))
                        comm_socket.send(response.encode())
                        print("Sent time to the client")
                    elif request == "NAME":
                        response = "test server"
                        comm_socket.send(response.encode())
                        print("Sent server name to the client")
                    elif request == "RAND":
                        response = str(randint(1, 10))
                        comm_socket.send(response.encode())
                        print("Sent a random number to the client")
                    elif request == "EXIT":
                        print("Client requested to disconnect.")
                        response = "EXITED SERVER"
                        comm_socket.send(response.encode())
                        break  # Exit the inner loop to wait for the next client
            except socket.error as msg:
                print('Client socket disconnected - ' + str(msg))
            finally:
                comm_socket.close()
                print(f'Connection to {client_address} closed')
    except socket.error as msg:
        print('Failed to open server socket - ' + str(msg))
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()