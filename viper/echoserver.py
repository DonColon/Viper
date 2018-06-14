################################################################################
# Viper - A web server build from scratch with Python.                         #
# © 2018 Dardan Rrafshi                                                        #
# Licensed under MIT (https://github.com/DonColon/Viper/blob/master/LICENSE)   #
################################################################################
import socket


class TCPServer:
    def __init__(self, host='127.0.0.1', port=8080, buffersize=1024, backlog=128):
        self.serverAddress = (host, port)
        self.buffersize = buffersize
        self.backlog = backlog

    def run(self):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            listener.bind(self.serverAddress)
            listener.listen(self.backlog)
        except socket.error as message:
            print(str(message))

        print('Serving HTTP at {}'.format(listener.getsockname()))
        while True:
            clientConnection, clientAddress = listener.accept()
            print('Connected to {}:{}'.format(clientAddress[0], clientAddress[1]))

            request = clientConnection.recv(self.buffersize)
            response = self.serveClient(request.decode())

            clientConnection.sendall(response.encode())
            clientConnection.close()

    def serveClient(self, data):
        """Handles an incoming request and returns a response.
        Override this in subclass."""
        return data


if __name__ == '__main__':
    server = TCPServer()
    server.run()
