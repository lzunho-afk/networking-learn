#!/usr/bin/env python3
# ntp_print.py -- Prints current time from a NTP server
# Lucas Zunho <lucas.zunho@zunho.com.br> (c) MIT

from time import ctime
import ntplib
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
    argp.add_argument('-c', '--connection-mode', choices=['NTPLIB', 'SKELETON'], action="store", dest="mode", default='NTPLIB', required=True)
    argp.add_argument('--hostname', action="store", dest="host", default='pool.ntp.org', required=False)
    argp.add_argument('-p', '--port', type=int, choices=range(1,65535), metavar='PORT', action="store", dest="port", default=0, required=False)
    args = argp.parse_args()
    connection_mode = args.mode
    host = args.host
    port = args.port

    if connection_mode == 'NTPLIB':
        ntplib_time(host)
    else:
        skeleton_time(host, port)

if __name__ == "__main__":
    main()
