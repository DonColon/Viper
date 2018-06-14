################################################################################
# Viper - A web server build from scratch with Python.                         #
# © 2018 Dardan Rrafshi                                                        #
# Licensed under MIT (https://github.com/DonColon/Viper/blob/master/LICENSE)   #
################################################################################


class HTTPRequest:
    def __init__(self, data):
        self.method = 'GET'
        self.uri = '/'
        self.protocol = 'HTTP/1.1'
        self.headers = dict()
        self.parameters = dict()

        self.parse(data)

    def parse(self, data):
        request = data.split('\r\n')
        request = [x for x in request if x != '']

        self.parseRequestLine(request[0])

        # TODO Fix GET Reuqest handling
        if self.method == 'GET':
            self.parseHeaders(headers=request[1:])
            self.parseParameters(parameters=request[0])
        elif self.method == 'POST':
            self.parseHeaders(headers=request[1:len(request)-1])
            self.parseParameters(parameters=request[len(request)-1])

    def parseRequestLine(self, requestLine):
        requestLine = requestLine.split(' ')
        self.method = requestLine[0]
        self.uri = requestLine[1]

        if len(requestLine) > 2:
            self.protocol = requestLine[2]

    def parseHeaders(self, headers):
        for header in headers:
            key, value = header.split(': ')
            self.headers[key] = value

    def parseParameters(self, parameters):
        parameters = parameters.split('&')
        for parameter in parameters:
            key, value = parameter.split('=')
            self.parameters[key] = value
