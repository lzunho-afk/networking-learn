#!/usr/bin/env python3
# addr_reuse.py -- Address reuse example
# Lucas Zunho <lucas.zunho@zunho.com.br> (c) MIT

import socket
import sys
import argparse

HOST = "127.0.0.1"
PORT = 0

def main():
    # Commandline arguments
    argp 
    
    # Creating file descriptor
    try:
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        sys.exit("Err. => File descriptor returned an exception: %s".format(e))

    # Getting old address socket state
    sock_config = sockfd.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("Default => {}".format(sock_config))

    # Config Update
    sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_config = sockfd.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("New State => {}".format(sock_config))

if __name__ == "__main__":
    main()
