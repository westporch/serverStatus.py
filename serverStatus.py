#!/usr/bin/python
#Usage: ./serverStatus.py list.txt
#Date: 2016.04.19

import os
import sys
from socket import *

def check_server_status(server_addr):
    sock = socket(AF_INET, SOCK_STREAM)

    try:
        #sock.connect(('192.168.0.132', 22))
        sock.connect((server_addr, 22))
        print "\033[92m%s -> Alive\033[00m\n" % (server_addr)
    except Exception as e:
        print "\033[91m%s -> Dead\033[00m\n" % (server_addr)

    sock.close()


def get_server_lists():
    server_list_file = sys.argv[1]
    f = open(server_list_file, 'r')

    lines = f.readlines()
    for server_addr in lines:
        #print(line)
        check_server_status(server_addr)

    f.close()


get_server_lists()
