import json
import sys
import argparse
import yaml
import logging.handlers
from socket import *
from jim_protocol import *
sys.path.append('../log')
from server_log_config import *
from decor import *


@decoration_log
def createparser():
    parser = argparse.ArgumentParser()
    logger.info('Create Parser')
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
def server(addres,port):
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.bind((addres,port))
    except OSError:
        logger.critical('Порт занят')
        return

    s.listen(3)
    while True:
        client, addr = s.accept()
        data = client.recv(1024)
        msg = json.loads(data.decode('utf-8'))

        logger.info('получено сообщение от клиента')


        if msg['action'] == 'presence':
            answer['response']='200'
            msg_to=json.dumps(answer)
            client.send(msg_to.encode('utf-8'))
            logger.info('отправлен ответ клиенту')
            logger.debug('отправлен ответ клиенту:'+msg_to)

        client.close


if __name__ == '__main__':
    config_param = load_config()
    log = set_log_param(config_param)
    logger = logging.getLogger('app')
    logger.info('Старт приложения')
    parser = createparser()
    namespace = parser.parse_args(sys.argv[1:])
    logger.info('Запускаем сервер')
    server(namespace.addres,int(namespace.port))



