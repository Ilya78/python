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


def server(addres,port):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((addres,port))
    s.listen(3)
    while True:
        client, addr = s.accept()
        data = client.recv(1024)
        msg = json.loads(data.decode('utf-8'))

        if msg['action'] == 'presence':
            answer['response']='200'
            msg_to=json.dumps(answer)
            client.send(msg_to.encode('utf-8'))

        client.close


if __name__ == '__main__':
    parser = createparser()
    namespace = parser.parse_args(sys.argv[1:])

    server(namespace.addres,int(namespace.port))
