import os
import http.server
import socketserver

PORT = 8080

class redirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.do_redirect('remove')
        self.do_redirect('update')
        self.go_to_blog()
        super(redirectHandler, self).do_GET()

    def do_redirect(self, path):
        if self.path == '/service/%s/1970-01-01T00:00:00' % path:
            self.send_response(301)
            self.send_header('Location', '/service/v2/%s/1970-01-01T00:00:00/' % path)
            self.end_headers()

    def go_to_blog(self):
        if self.path in ('/index.html', '/'):
            self.send_response(301)
            self.send_header('Location', 'https://blog.victi.ms')
            self.end_headers()


# Server from the server directory as it has the required files
os.chdir('server')
with socketserver.ThreadingTCPServer(("", PORT), redirectHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
