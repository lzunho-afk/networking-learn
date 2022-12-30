#!/usr/bin/env python3
# ip_convert.py -- Convert IPv4 address to packed format (hex)
# Lucas Zunho <lucas.zunho@zunho.com.br> (c) MIT

import socket
import sys
from binascii import hexlify

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: ./ip_convert.py {ADDRESSES}\nEx.: ./ip_convert.py 127.0.0.1 192.168.0.1")
    for addr in sys.argv[1:]:
        pkg_addr = socket.inet_aton(addr)
        unpkg_addr = socket.inet_ntoa(pkg_addr)
        print ("Input ADDR => {}\nPkg ADDR => {}; UnPkg ADDR => {}".format(
            addr,
            pkg_addr,
            unpkg_addr
        ))

if __name__ == "__main__":
    main()
