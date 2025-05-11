#!/usr/bin/env python3
# server.py
import http.server
import socketserver
import cgi

PORT = 8000

Handler = http.server.CGIHTTPRequestHandler
Handler.cgi_directories = ["/cgi-bin"]

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
