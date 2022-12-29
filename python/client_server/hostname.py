#!/usr/bin/env python3
# hostname.py -- Shows machine's name & ipv4 address
# Lucas Zunho <lucas.zunho@zunho.com.br> (c) MIT

import socket

def main():
    hostname = socket.gethostname()
    addr = socket.gethostbyname(hostname)
    print ("Hostname => {}\nIP Address => {}".format(hostname, addr))

if __name__ == '__main__':
    main()
