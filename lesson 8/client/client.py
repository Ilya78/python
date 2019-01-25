import datetime
import json
import yaml
from json import JSONDecodeError
from socket import *
from threading import Thread
import sys
import logging.handlers
sys.path.append('../log')
from server_log_config import *
class JimChah():
    '''
    Базовый класс чата
    '''

    def __init__(self,account_name):
        self.account_name_from = account_name


    def presenceChat(self,messageStatus):
        msg = {
            "action": "presence",
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "type": "status",
            "user": { "account_name": self.account_name_from,
                      "status": messageStatus
                    }
            }
        return msg

    def probeChat(self):
        pass

    def authenticate(self):
        pass

    def joinChat(self):
        pass

    def leaveChat(self):
        pass

    def msgChat(self, accont_name_to, message):
        msg = {
            "action": "msg",
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "to": accont_name_to,
            "from": self.account_name_from,
            "message": message
        }
        return msg

def connect(addres,port):
    sock = socket(AF_INET, SOCK_STREAM)
    try:
        sock.connect((addres, port))
    except OSError:
        logger.info('Ошибка соединения с сервером')

    return sock

def recive_msg(sock):
    while True:
        dataJsonStr = sock.recv(1024)
        try:
           data = json.loads(dataJsonStr)
        except JSONDecodeError:
           pass
        else:
            logger.info("\n{} - {} : {}".format(data['time'], data['from'], data['message']))


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
    sock_send = connect('127.0.0.1', 7777)
    sock_recive = connect('127.0.0.1', 7777)

    th_reciver = Thread(target=recive_msg, args=(sock_recive,))
    th_reciver.daemon = False
    th_reciver.start()
    logger.info('Поток запущен')

    name = input('Введите ваше имя в чате: ')

    chat = JimChah(name)

    while True:
        data = input('>>')
        msg = chat.msgChat('#', data)

        if data == 'exit':
            break

        sock_send.send(json.dumps(msg).encode('utf-8'))  # Отправить!
        sock_send.recv(1024)



if __name__ == '__main__':
    config_param = load_config()
    log = set_log_param(config_param)
    logger = logging.getLogger('app')
    logger.info('Старт приложения')
    main()

