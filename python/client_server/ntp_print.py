#!/usr/bin/env python3
# ntp_print.py -- Prints current time from a NTP server
# Lucas Zunho <lucas.zunho@zunho.com.br> (c) MIT

from time import ctime
import ntplib
import sys
import argparse

def ntplib_time(host):
    ntp_client = ntplib.NTPClient()
    res = ntp_client.request(host)
    print (ctime(res.tx_time))

def skeleton_time(host, port):
    pass
    
def main():
    # Command-line arguments
    argp = argparse.ArgumentParser(prog="ntp_print.py", description="NTP Print program")
    sargp = argp.add_subparsers(dest="connection_mode", help="Connection modes help", required=True)

    # NTPLIB Parser
    ntplib_argp = sargp.add_parser("ntplib", help="Uses ntplib connection module")
    ntplib_argp.add_argument('--hostname', action="store", dest="host", help='NTP Server to connect', default='pool.ntp.org', required=False)

    # SKELETON Parser
    skeleton_argp = sargp.add_parser("skeleton", help="Uses pure socket communication")
    skeleton_argp.add_argument('--hostname', action="store", dest="host", help='NTP Server to connect', required=True)
    skeleton_argp.add_argument('-p', '--port', type=int, choices=range(1,65535), metavar='PORT', action="store", dest="port", help='NTP Server port', default=123, required=False)

    args = argp.parse_args()

    if args.connection_mode == 'ntplib':
        ntplib_time(args.host)
    elif args.connection_mode == 'skeleton':
        skeleton_time(args.host, args.port)

if __name__ == "__main__":
    main()
