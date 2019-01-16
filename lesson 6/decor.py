import logging

def decoration_log(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger('app')
        msg = "Функция {0} вызвана из функции  ".format(func.__name__)+func.__module__
        print(msg)
        logger.info(msg)
        res = func(*args, **kwargs)
        return res
    return wrapper

