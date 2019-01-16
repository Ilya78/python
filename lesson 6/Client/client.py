from socket import *
from jim_protocol import *
import json
import sys
import argparse
import yaml
import logging
import logging.handlers
sys.path.append('../log')
from client_log_config import *
from decor import *


@decoration_log
def createparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default='7777')
    parser.add_argument('-a', '--addres', default='127.0.0.1')
    return parser

@decoration_log
def load_config():
    with open('config.yaml', 'r') as f_n:
        config = yaml.load(f_n)
        print(config)
    return config

@decoration_log
def client(addres,port,message):
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((addres, port))
    except OSError:
        logger.critical('Ошибка соединения с сервером')
        return

    s.send(message.encode('utf-8'))
    logger.info('отправлен запрос серверу')
    logger.debug('запрос:' + message)
    data = s.recv(1024)
    logger.info('получен ответ от сервера')
    s.close
    return data



if __name__ == '__main__':
    config_param = load_config()
    log = set_log_param(config_param)
    logger = logging.getLogger('app')
    logger.info('Старт приложения')
    parser = createparser()
    namespace = parser.parse_args(sys.argv[1:])

    msg = json.dumps(action_presence)
    data=client(namespace.addres,int(namespace.port),msg)