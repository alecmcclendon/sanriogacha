#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8000

# Set the working directory for the server
os.chdir('/opt/render/project/src')

# Configure CGI handler
Handler = http.server.CGIHTTPRequestHandler
Handler.cgi_directories = ["/cgi-bin"]

print(f"Serving at port {PORT}")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
