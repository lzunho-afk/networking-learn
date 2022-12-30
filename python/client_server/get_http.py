#!/usr/bin/env python3
# get_http.py -- Send a GET request to a HTTP server
# Lucas Zunho <lucas.zunho@zunho.com.br> (c) MIT

import socket
import sys
import argparse

def main():
    # Command-line arguments
    argparser = argparse.ArgumentParser(description='HTTP Get Request Script')
    argparser.add_argument('--host', action="store", dest="host", required=True)
    argparser.add_argument('--port', action="store", dest="port", required=True)
    argparser.add_argument('--file', action="store", dest="file", required=True)

    args = argparser.parse_args()
    host = args.host
    port = int(args.port)
    filename = args.file

    # Creating filedescriptor
    try:
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        sys.exit("Socket creation returned an error => {}".format(e))

    # Connecting
    try:
        sockfd.connect((host, port))
    except socket.gaierror as e:
        sys.exit("Socket connection returned an address-related error  => {}".format(e))
    except socket.error as e:
        sys.exit("Socket connection returned an error => {}".format(e))

    # Sending request
    try:
        sockfd.sendall("GET {} HTTP/1.0\r\n\r\n".format(filename).encode())
    except socket.error as e:
        sys.exit("Socket file request returned an error => {}".format(e))

    # Recv & Write data
    while True:
        try:
            buff = sockfd.recv(1024)
        except socket.error as e:
            sys.exit("Recv returned an error => {}".format(e))

        if not len(buff):
            break
        sys.stdout.write(buff.decode())

if __name__ == "__main__":
    main()
