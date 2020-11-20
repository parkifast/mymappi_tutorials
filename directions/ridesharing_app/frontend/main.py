import http.server
import socketserver

# Simple HTTP Server to simulate a Frontend APP 
# that send index html.

URL = "127.0.0.1"
PORT = 3000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://{URL}:{PORT}")
    httpd.serve_forever()
