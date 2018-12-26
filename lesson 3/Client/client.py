from socket import *
from jim_protocol import *
import json
import os
import time
import sys
import argparse

def createparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default='7777')
    parser.add_argument('-a', '--addres', default='127.0.0.1')
    return parser


def client(addres,port,message):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addres,port))
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    s.close
    return data



if __name__ == '__main__':
    parser = createparser()
    namespace = parser.parse_args(sys.argv[1:])

    msg = json.dumps(action_presence)
    data=client(namespace.addres,int(namespace.port),msg)
    print(data)