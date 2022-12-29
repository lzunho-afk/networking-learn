#!/usr/bin/env python3
# external_host_addr.py -- Get IP address from a domain
# Lucas Zunho <lucas.zunho@zunho.com.br> (c) MIT

import socket
import sys

# @ARG1 => HOSTNAME
def main():
    if len(sys.argv) != 2:
        sys.exit("Por favor específique um domínio.\nUSAGE: ./external_host_addr.py [HOSTNAME]")
    rhost = sys.argv[1]
    try:
        print("IP Address =>", socket.gethostbyname(rhost))
    except socket.error as emsg:
        sys.exit("Error =>", emsg)

if __name__ == "__main__":
    main()
