################################################################################
# Viper - A web server build from scratch with Python.                         #
# © 2018 Dardan Rrafshi                                                        #
# Licensed under MIT (https://github.com/DonColon/Viper/blob/master/LICENSE)   #
################################################################################
from viper.echoserver import TCPServer
from viper.httpmessage import HTTPRequest
from viper.httpmessage import HTTPResponse

import mimetypes
import os


class HTTPServer(TCPServer):

    def serveClient(self, data):
        request = HTTPRequest(data)

        try:
            requesthandler = getattr(self, 'do{}'.format(request.method))
            response = requesthandler(request)
        except AttributeError:
            response = self.notifyError(501)

        return str(response)

    def doGET(self, request):
        response = HTTPResponse()
        filename = request.uri.strip('/')

        if os.path.exists(filename):
            response.status(200)

            with open(filename) as file:
                response.body = file.read()

            extraHeaders = dict()
            extraHeaders['Content-Type'] = mimetypes.guess_type(filename)[0]
            extraHeaders['Content-Length'] = len(response.body)

            response.updateHeaders(extraHeaders)
        else:
            response = self.notifyError(404)

        return response

    def notifyError(self, statusCode):
        response = HTTPResponse()
        response.status(statusCode)
        response.body = '<h1>{} {}</h1>'.format(response.statusCode, response.reason)

        extraHeaders = dict()
        extraHeaders['Content-Type'] = 'text/html'
        extraHeaders['Content-Length'] = len(response.body)

        response.updateHeaders(extraHeaders)
        return response


if __name__ == '__main__':
    server = HTTPServer()
    server.run()
