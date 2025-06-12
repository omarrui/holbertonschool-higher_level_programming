#!/usr/bin/python3
"""
task_03_http_server

this module contains
1 server and 1 class
"""
import http.server
import socketserver
import json


class MyHandler(http.server.BaseHTTPRequestHandler):
    """
    this class sends a response for
    special path
    """
    def do_GET(self):
        

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
