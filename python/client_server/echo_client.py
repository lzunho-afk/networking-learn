#!/usr/bin/env python3
# echo_client.py -- Simple ECHO client
# Lucas Zunho <lucas.zunho@zunho.com.br> (c) MIT

import socket
import sys
import argparse

def main():
    # Commandline arguments
    argp = argparse.ArgumentParser(prog="echo_client.py", description="Simple ECHO client")
    argp.add_argument('--host', '--hostname', action='store', dest='host', help='echo server hostname', required=True)
    argp.add_argument('-p', '--port', type=int, choices=range(1,65535), metavar='PORT', action='store', dest='port', help='echo server port number', required=True)
    args = argp.parse_args()
    host = args.host
    port = args.port
    addr = (host, port)

    # File descriptor
    try:
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockfd.connect(addr)
    except Exception as e:
        sys.exit("=> Socket returned an error: {}".format(e))

    # Buffer
    try:
        print("Enter your text. Put END to stop.")
        input_buff = []
        while True:
            ln = input("> ")
            if ln.upper() == "END":
                break
            else:
                input_buff.append(ln)

        # Text format
        buff = '\n'.join(input_buff)
        buff_size = len(buff)
        buff_count = 0
        print ("\nBUFFER => {}\n".format(buff))

        # Sending
        print("[*] Sending {} bytes of data".format(buff_size))
        sockfd.sendall(buff.encode())

        if buff_count < buff_size:
            buff = sockfd.recv(buff_size)
            buff_count += len(buff)
            print("\t=> Returned {} bytes".format(buff_count))
    except KeyboardInterrupt:
        print("Stopping...")
    except Exception as e:
        print("=> Program returned an exception: {}".format(e))
    finally:
        sockfd.close()

if __name__ == "__main__":
    main()

