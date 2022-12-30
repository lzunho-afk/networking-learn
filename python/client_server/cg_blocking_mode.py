#!/usr/bin/env python3
# cg_blocking_mode.py -- Set blocking/non-blocking socket mode
# Lucas Zunho <lucas.zunho@zunho.com.br> (c) MIT

import socket
import sys
import argparse

HOST = '127.0.0.1'

# Check 'listen' command-line argument
def check_listen(n):
    nval = int(n)
    if nval <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int" % n)
    return nval

def main():
    # Command-line arguments
    argp = argparse.ArgumentParser(prog='cg_blocking_mode.py', description='Blocking/Non-blocking socket program')
    argp.add_argument('-l', '--listen', type=check_listen, action="store", dest="listen_count", required=True)
    argp.add_argument('-m', '--mode', choices=['BLOCKING', 'NONBLOCKING'], action="store", dest="mode", required=True)
    argp.add_argument('-t', '--timeout', type=float, action="store", dest="timeout", default=float(0.5), required=False)
    argp.add_argument('-p', '--port', type=int, choices=range(1,65535), metavar='PORT', action="store", dest="port", default=0, required=False)
    args = argp.parse_args()
    listen_count = args.listen_count
    mode = 0 if args.mode == 'BLOCKING' else 1
    timeout = args.timeout
    port = args.port
    
    # File Descriptor
    try:
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        sys.exit("Socket creation returned an error => {}".format(e))

    # Setting mode
    sockfd.setblocking(mode)
    sockfd.settimeout(timeout)
    sockfd.bind((HOST, port))

    # Listening
    sockfd_addr = sockfd.getsockname()
    print ("[*] Started on {}".format(sockfd_addr))
    sockfd.listen(listen_count)

    # Receiving 1024 bytes and closing connection to client
    try:
        while True:
            clientfd, client_addr = sockfd.accept()
            print("-> Received connection from: {}".format(client_addr))
            buff = clientfd.recv(1024).decode()
            print("-> Recv: {}".format(buff))
            clientfd.send("ACK".encode())
            clientfd.close()
    except KeyboardInterrupt as e:
        sockfd.close()
    except Exception as e:
        sys.exit("=> {}".format(e))

if __name__ == "__main__":
    main()
