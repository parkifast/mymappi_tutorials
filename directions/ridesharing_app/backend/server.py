import http.server
import socketserver
import os, json

# Simple HTTP Server to simulate a Backend API 
# to response matrix request from a Frontend APP.

URL = "127.0.0.1"
PORT = 8000

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Read allocations generated
        data = open(os.path.join("..", "database", "allocations.json"), "r").read()
        # Create the response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        # Send response to the client
        self.wfile.write(data.encode())

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f"Serving at http://{URL}:{PORT}")
    httpd.serve_forever()
