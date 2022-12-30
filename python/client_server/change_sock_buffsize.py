#!/usr/bin/env python3
# change_sock_buffsize.py -- Change default socket buffer size
# Lucas Zunho <lucas.zunho@zunho.com.br> (c) MIT

import socket
import sys
import argparse

def main():
    # Command-line arguments
    argp = argparse.ArgumentParser(description='Change socket buffer size program')
    argp.add_argument('-ss', '--send-size', action="store", dest="sendlen", required=True)
    argp.add_argument('-rs', '--recv-size', action="store", dest="recvlen", required=True)
    args = argp.parse_args()
    send_buffer_size = int(args.sendlen)
    recv_buffer_size = int(args.recvlen)

    # Filedescriptor creation
    try:
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        sys.exit("Socket creation returned an error => {}".format(e))

    # Getting socket buffer size
    buffer_size = sockfd.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print ("[Old Socket Config]: \n\tBufferSize => {}".format(buffer_size))

    # Setting new buffer size
    sockfd.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sockfd.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        send_buffer_size)
    sockfd.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        recv_buffer_size)

    # Getting socket NEW buffer size
    buffer_size = sockfd.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print ("[New Socket Config]:\n\tBufferSize => {}".format(buffer_size))

if __name__ == "__main__":
    main()
