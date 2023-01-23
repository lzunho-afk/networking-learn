#!/usr/bin/env python3
# -*- Coding: UTF-8 -*-

import os
import sys
import socket
import threading
import argparse
import socketserver

HOST = '127.0.0.1'
PORT = 0
BUFFERSIZE = 1024
MSG = 'Python programming ECHO! -- default msg...'

class ForkClient():
    """ Forking server client """
    def __init__(self, addr):
        # Filedescriptor creation
        try:
            self.sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            sys.exit("Unable to create file descriptor!")
        
        # Server Connection
        self.sockfd.connect(addr)

    def run(self):
        """ Client-Server call """

        # Sending data
        current_pid = os.getpid()
        print("[*] PID {} -> Sending \"{}\"".format(current_pid, MSG))
        msg_l = self.sockfd.send(MSG.encode())
        print("\t \-> Sent {} ch".format(msg_l))

        # Server Response
        res = self.sockfd.recv(BUFFERSIZE)
        print("[*] PID {} -> Received \"{}\"".format(current_pid, res[5:]))

    def shutdown(self):
        """ Client Cleanup """
        self.sockfd.close()


class ServerRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Send echo msm back to client
        buff = self.request.recv(BUFFERSIZE)
        current_pid = os.getpid()
        res = "{}: {}".format(current_pid, buff)
        print("[*] Server sending response [current_pid: data] [{}]".format(res))
        self.request.send(res.encode())

class ForkServer(socketserver.ForkingMixIn, socketserver.TCPServer, ):
    """ Included from parents """
    pass

def main():
    server = ForkServer((HOST, PORT), ServerRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    print("[App] Starting server loop on PID {}...".format(os.getpid()))

    # Client
    client = ForkClient((ip, port))
    client.run()

    client1 = ForkClient((ip, port))
    client1.run()

    # Clean-up
    server.shutdown()
    client.shutdown()
    client1.shutdown()
    server.socket.close()

if __name__ == "__main__":
    main()