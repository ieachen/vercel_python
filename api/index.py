
# from http.server import BaseHTTPRequestHandler
# from urllib import parse

# class handler(BaseHTTPRequestHandler):

# 	def do_GET(self):
# 		s = self.path
# 		dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
# 		self.send_response(200)
# 		self.send_header('Content-type','text/plain')
# 		self.end_headers()

# 		if "name" in dic:
# 			message = "Hello, " + dic["name"] + "!"
# 		else:
# 			message = "Hello, stranger!"

# 		self.wfile.write(message.encode())
# 		return
        

from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # ################ 输出 json 格式：
        # import json
        # self.send_header('Content-type', 'application/json')
        # self.end_headers()
        # data = {'result': 'this is a test'}
        # self.wfile.write(json.dumps(data).encode())

        # _dict = {
        #     'x-forwarded-for': self.headers.get('x-forwarded-for'),
        #     'User-Agent': self.headers.get('User-Agent'),
        #     'DNT': self.headers.get('DNT'),
        # }

        _dict = dict(self.headers)
        print(_dict)
        _str = 'The followings are header info: \n\n'
        for k, v in _dict.items():
            _str += f'{k}: {v} \n'
        message_bytes = _str.encode()

        self.wfile.write(message_bytes)


# def run():
#     from http.server import HTTPServer

#     host = ('localhost', 8888)
#     server = HTTPServer(host, handler)
#     print("Starting server, listen at: %s:%s" % host)
#     server.serve_forever()

#     # 然后在浏览器打开  http://localhost:8888/  即可访问

#     return


# 本地调试需要运行以下的 run()。
# 但在 vercel 不需要，只需要定义 BaseHTTPRequestHandler 即可

# if __name__ == '__main__':
#     run()
