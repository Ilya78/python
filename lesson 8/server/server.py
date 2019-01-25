from socket import *
import select
import sys
import yaml
import argparse
import json
import logging.handlers
from threading import Thread
sys.path.append('../log')
from server_log_config import *

import time


class JimChah():
    '''
    Базовый класс чата
    '''
    clients = []

    def __init__(self,sock):
        self.sock=sock

    def add_new_client(self):
        try:
            conn, addr = self.sock.accept()  # Проверка подключений
        except OSError as e:
            pass  # timeout вышел
        else:
            logger.info("Получен запрос на соединение от %s" % str(addr))
            JimChah.clients.append(conn)



    def recive_message(self):
        pass

    def send2chat(self):
        pass

    def send2user(self):
        pass

    def read_requests(self,r_clients):
        responses = {}  # Словарь ответов сервера вида {сокет: запрос}

        for s in list(r_clients):
            try:
                data =  s.recv(1024).decode('ascii')
                responses[s] = data
            except:
                pass

        return responses

    def write_responses(self,response, w_clients):
        for sock in w_clients:
            for key in response:
                sock.send(response[key].encode('ascii'))

def server(addres, port):
    sock = socket(AF_INET, SOCK_STREAM)
    try:
        sock.bind((addres, port))
    except OSError:
        logger.info('Порт занят')

    sock.listen(3)
    return sock

def new_clients(chat):
    while True:
        chat.add_new_client()

def load_config():
    with open('config.yaml', 'r') as f_n:
        config = yaml.load(f_n)
    return config

def createparser():
    parser = argparse.ArgumentParser()
    logger.info('Create Parser')
    parser.add_argument('-p', '--port', default='7777')
    parser.add_argument('-a', '--addres', default='127.0.0.1')
    return parser


def main():
    parser = createparser()
    namespace = parser.parse_args(sys.argv[1:])
    logger.info('Запускаем сервер')
    server(namespace.addres, int(namespace.port))
    sock = server(namespace.addres, int(namespace.port))

    new_chat = JimChah(sock)

    th_reciver = Thread(target=new_clients, args=(new_chat,))
    th_reciver.daemon = False
    th_reciver.start()

    logger.info('поток запущен')

    while True:
        wait = 10
        r_clients = []
        w_clients = []
        e = []
        try:
            r_clients, w_clients, e = select.select(new_chat.clients, new_chat.clients, new_chat.clients, wait)
        except:
            if len(e) > 0:
                logger.info('исключение', e)  # Ничего не делать, если какой-то клиент отключился

        resp = new_chat.read_requests(r_clients)
        if len(resp) > 0:
            new_chat.write_responses(resp, w_clients)


if __name__ == '__main__':
    config_param = load_config()
    log = set_log_param(config_param)
    logger = logging.getLogger('app')
    logger.info('Старт приложения')
    main()








