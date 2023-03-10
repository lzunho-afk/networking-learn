#!/usr/bin/env python3
# addr_reuse.py -- Address reuse example
# Lucas Zunho <lucas.zunho@zunho.com.br> (c) MIT
#
# With SO_REUSEADDR you can close the server and rerun it on the same port --
# this program is a simple use example

import socket
import sys
import argparse

HOST = "127.0.0.1"

def main():
    # Command-line arguments
    argp = argparse.ArgumentParser(prog="addr_reuse.py", description="address reuse example program")
    argp.add_argument('-p', '--port', type=int, choices=range(1,65535), metavar='PORT', action="store", dest="port", default=0, required=False)
    args = argp.parse_args()
    PORT = args.port
    
    # Creating file descriptor example
    try:
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        sys.exit("Err. => File descriptor returned an exception: {}".format(e))

    # Getting old address socket state
    sock_config = sockfd.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("Default => {}".format(sock_config))

    # Config Update
    sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_config = sockfd.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("New State => {}".format(sock_config))

    # Creating new file descriptor
    try:
        newfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        sys.exit("Err. => File descriptor returned an exception: {}".format(e))

    # Reuse config
    newfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    newfd.bind((HOST, PORT))
    newfd.listen(1)
    print("[*] Listening on port {}".format(newfd.getsockname()[1]))
    while True:
        try:
            clientfd, clientaddr = newfd.accept()
            print("\t=> Connection From {}:{}".format(clientaddr[0], clientaddr[1]))
        except KeyboardInterrupt:
            break
        except socket.error as e:
            sys.exit("Err. => Connection loop returned an error: {}".format(e))

if __name__ == "__main__":
    main()
