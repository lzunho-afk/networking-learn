#!/usr/bin/env python3
# -*- Coding: UTF-8 -*-

import os
import sys
import socket
import threading
import argparse
import socketserver

HOST = '127.0.0.1'
PORT = None
BUFFERSIZE = None
MSG = None

def client(host, port, msg):
    """ Simple client for multiclient server """
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockfd.connect((host, port))
    try:
        sockfd.sendall(msg.encode())
        res = sockfd.recv(BUFFERSIZE)
        print("[Client] -> Received {}".format(res))
    finally:
        sockfd.close()

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """ Threaded TCP request handler """
    def handle(self):
        data = self.request.recv(BUFFERSIZE)
        current_thread = threading.current_thread()
        res = "{}: {}".format(current_thread, data)
        self.request.sendall(res.encode())

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """ Included from parents """
    pass

def main():
    global MSG, BUFFERSIZE, PORT
    # Commandline arguments
    argp = argparse.ArgumentParser(prog="echo_multiclient_server.py", description="Simple ECHO server/client example")
    argp.add_argument('-m', '--msg', '--message', action='store', dest='msg', help='ECHO message string', default="Python programming ECHO! -- default msg")
    argp.add_argument('-p', '--port', type=int, choices=range(1,65535), metavar='PORT', action='store', dest='port', help='ECHO server port number', default=0)
    argp.add_argument('-b', '--buffsize', type=int, action='store', dest='buffsize', help='ECHO buffer size', default=1024)
    args = argp.parse_args()
    MSG = args.msg
    BUFFERSIZE = args.buffsize
    PORT = args.port

    # Running server instance
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    host, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("[*] Server loop running. Thread -> {}".format(server_thread.name))

    # Running clients
    client(host, port, "I'm Client 1...")
    client(host, port, "John, aka Client 2.")
    client(host, port, "Hello from Client 3!!")
    
    # Clean-up
    server.shutdown()

if __name__ == "__main__":
    main()