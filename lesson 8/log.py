import logging
import inspect

def log(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger('app')
        msg = "Функция {0} вызвана из функции  ".format(func.__name__)+inspect.stack()[1].function
        print(msg)
        logger.info(msg)
        res = func(*args, **kwargs)
        return res
    return wrapper

