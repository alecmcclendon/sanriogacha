import os
from http.server import test, CGIHTTPRequestHandler

port = int(os.environ.get("PORT", 8000))
test(HandlerClass=CGIHTTPRequestHandler, port=port)
