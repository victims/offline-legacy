import http.server
import socketserver

PORT = 8000

class redirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.do_redirect('remove')
        self.do_redirect('update')
        super(redirectHandler, self).do_GET()

    def do_redirect(self, path):
        if self.path == '/service/%s/1970-01-01T00:00:00' % path:
            self.send_response(301)
            self.send_header('Location', '/service/v2/%s/1970-01-01T00:00:00/' % path)
            self.end_headers()

with socketserver.TCPServer(("", PORT), redirectHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()