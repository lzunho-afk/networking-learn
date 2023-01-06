#!/usr/bin/env python3
# echo_server.py -- Simple echo server
# Lucas Zunho <lucas.zunho@zunho.com.br> (c) MIT

import socket
import sys
import argparse

def main():
    # Commandline arguments
    argp = argparse.ArgumentParser(prog="echo_server.py", description="Simple ECHO server")
    argp.add_argument('--host', '--hostname', action="store", dest="host", default="localhost", help='server hostname', required=False)
    argp.add_argument('-p', '--port', type=int, choices=range(1,65535), metavar='PORT', action="store", dest="port", default=0, help='server port number', required=False)
    argp.add_argument('--payload-size', type=int, action="store", dest="payload_size", default=2048, help='recv payload size', required=False)
    argp.add_argument('-b', '--backlog', action="store", type=int, dest="backlog", default=5, help='bind backlog count', required=False)
    args = argp.parse_args()
    backlog = args.backlog
    payload_size = args.payload_size
    host = args.host
    port = args.port
    addr = (host, port)

    # File descriptor
    try:
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Addr reuse
    except socket.error as e:
        sys.exit("=> Socket creation returned an error: {}".format(e))
        
    # Binding
    try:
        sockfd.bind(addr)
        sockfd.listen(backlog)
    except Exception as e:
        sys.exit("=> Binding returned an error: {}".format(e))

    # Connection Loop
    print("[*] Listening on {}:{}".format(host, sockfd.getsockname()[1]))
    try:
        while True:
            clientfd, clientaddr = sockfd.accept()
            print("~> Got connection from {}:{}".format(clientaddr[0], clientaddr[1]))
            buff = clientfd.recv(payload_size).decode()
            if buff:
                # Buffer Printing
                print (".Buffer => [")
                for ln in buff.split('\n'):
                    print (">", ln)
                print ("]")
                
                # ACK
                clientfd.send(buff.encode())
                print(".ACK -- {} bytes".format(len(buff.encode('utf-8'))))
            clientfd.close()
    except KeyboardInterrupt:
        sys.exit("Stopping...")
    except Exception as e:
        sys.exit("=> Server returned an exception: {}".format(e))

if __name__ == "__main__":
    main()
