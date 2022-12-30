#!/usr/bin/env python3
# service_name.py -- Get localhost service name
# Lucas Zunho <lucas.zunho@zunho.com.br> (c) MIT

import socket
import sys

USAGE = "Usage: ./service_name.py [PROTOCOL] [PORT_RANGE]\nEx.: ./service_name.py tcp 80-25"

def port_esp(port, protocol):
    try:
        service_name = socket.getservbyport(port, protocol)
        print("Port {} => Service Name \"{}\"".format(port, service_name))
    except Exception as e:
        print("Port {} => Service Name \"{}\"".format(port, e))

def main():
    if len(sys.argv) < 3:
        sys.exit(USAGE)
        
    if '-' in sys.argv[2]:
        port_range = sys.argv[2].split('-')
        if port_range[0].isdigit() and port_range[1].isdigit():
            for port in range(int(port_range[0]), int(port_range[1])):
                port_esp(port, sys.argv[1])
        else:
            sys.exit(USAGE)
    elif sys.argv[2].isdigit():
        port = int(sys.argv[2])
        port_esp(port, sys.argv[1])
    else:
        sys.exit(USAGE)

if __name__ == "__main__":
    main()
