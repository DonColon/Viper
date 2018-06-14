################################################################################
# Viper - A web server build from scratch with Python.                         #
# © 2018 Dardan Rrafshi                                                        #
# Licensed under MIT (https://github.com/DonColon/Viper/blob/master/LICENSE)   #
################################################################################
from viper.echoserver import TCPServer


class HTTPServer(TCPServer):
    statusCode = {
        200: 'OK',
        404: 'Not Found'
    }

    headers = {
        'Server': 'Viper',
        'Content-Type': 'text/html'
    }

    def serveClient(self, data):
        response = (
            'HTTP/1.1 200 OK\r\n',
            '\r\n',
            'Request received!'
        )
        return ''.join(response)


if __name__ == '__main__':
    server = HTTPServer()
    server.run()
