import logging

def set_log_param(config_param):
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        level=logging.DEBUG
    )

    if config_param['log_level'] == 'DEBUG':
        config_param['log_level'] = 10
    elif config_param['log_level'] == 'INFO':
        config_param['log_level'] = 20
    elif config_param['log_level'] == 'WARNING':
        config_param['log_level'] = 30
    elif config_param['log_level'] == 'ERROR':
        config_param['log_level'] = 40
    elif config_param['log_level'] == 'CRITICAL':
        config_param['log_level'] = 50
    else:
        config_param['log_level'] = 0

    logger = logging.getLogger('app')

    fn = logging.handlers.RotatingFileHandler(config_param['log_name'],
                                              mode='a',
                                              maxBytes=config_param['maxBytes'],
                                              backupCount=config_param['backupCount'])

    format = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    fn.setFormatter(format)
    logger.addHandler(fn)
    logger.setLevel(config_param['log_level'])
    return 0

