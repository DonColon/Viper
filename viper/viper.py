################################################################################
# Viper - A web server build from scratch with Python.                         #
# © 2018 Dardan Rrafshi                                                        #
# Licensed under MIT (https://github.com/DonColon/Viper/blob/master/LICENSE)   #
################################################################################
import socket


SERVER_ADDRESS = (HOST, PORT) = 'localhost', 8080
BACKLOG = 5


def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind(SERVER_ADDRESS)
        server.listen(BACKLOG)
    except socket.error as message:
        print(str(message))

    print('Serving HTTP on Port {}'.format(PORT))
    while True:
        clientConnection, clientAddress = server.accept()
        print('Connected to {} : {}'.format(clientAddress[0], clientAddress[1]))
        serveClient(clientConnection)


def serveClient(client):
    request = client.recv(2048)
    print(request.decode())

    response = 'HTTP/1.1 200 OK\n\r\n\rHello World!'

    client.sendall(response.encode())
    client.close()


if __name__ == '__main__':
    run()
