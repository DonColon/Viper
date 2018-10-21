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

        if self.method == 'GET':
            self.parseHeaders(headers=request[1:])
        elif self.method == 'POST':
            self.parseHeaders(headers=request[1:len(request)-1])
            self.parseParameters(parameters=request[len(request)-1])

    def parseRequestLine(self, requestLine):
        requestLine = requestLine.split(' ')
        self.method = requestLine[0]

        if '?' in requestLine[1]:
            url = requestLine[1].split('?')
            self.parseParameters(parameters=url[1])
            self.uri = url[0]
        else:
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


status = {
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',

    300: 'Multiple Choice',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See Other',
    304: 'Not Modified',
    307: 'Temporary Redirect',
    308: 'Permanent Redirect',

    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Payload Too Large',
    414: 'URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Requested Range Not Satisfiable',
    417: 'Expectation Failed',
    418: 'I\'m a teapot',
    421: 'Misdirected Request',
    426: 'Upgrade Required',
    428: 'Precondition Required',
    429: 'Too Many Requests',
    431: 'Request Header Fields Too Large',
    451: 'Unavailable For Legal Reasons',

    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    506: 'Variant Also Negotiates',
    507: 'Insufficient Storage',
    508: 'Loop Detected',
    510: 'Not Extended',
    511: 'Network Authentication Required'
}


class HTTPResponse:
    def __init__(self):
        self.statusCode = '200'
        self.reason = 'OK'
        self.protocol = 'HTTP/1.1'
        self.headers = {
            'Server': 'Viper',
            'Connection': 'Keep-Alive'
        }
        self.body = ''

    def status(self, code):
        self.statusCode = code
        self.reason = status[code]

    def updateHeaders(self, headers):
        self.headers.update(headers)

    def __str__(self):
        response = '{} {} {}\r\n'.format(self.protocol, self.statusCode, self.reason)
        for header in self.headers:
            response += '{}: {}\r\n'.format(header, self.headers[header])
        response += '\r\n'
        response += self.body
        return response
