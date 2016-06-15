# -*- coding: utf-8 -*-
"""
log function
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import logging
import logging.config
from xbuild import builDir


def logger(levelName, saveName, saveDir='./'):
    """
    logger(levelName, saveName, saveDir='./')

    high level logging
    levelName: default, console, file
    how to use:
    alog = logger('default', 'log13.txt')
    alog.debug('debug message!')
    alog.info('info message!')
    alog.error('error message')
    alog.critical('critical message')
    alog.warning('warning message')
    """
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'default': {'format': '%(asctime)s %(levelname)s %(message)s',
                        'datefmt': '%Y-%m-%d %H:%M:%S',
                        },
            'verbose': {'format': '%(asctime)s %(levelname)s %(module)s \
                %(process)d %(thread)d %(message)s',
                        'datefmt': '%Y-%m-%d %H:%M:%S',
                        },
            'simple': {'format': '%(levelname)s %(message)s',
                       'datefmt': '%Y-%m-%d %H:%M:%S'
                       },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': 'ext://sys.stdout',
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'default',
                'filename': builDir(saveDir, saveName),
                'maxBytes': 1024000,
                'backupCount': 3,
                'encoding': 'utf8',
            },
        },
        'loggers': {
            'default': {
                'level': 'DEBUG',
                'handlers': ['console', 'file'],
            },
            'console': {
                'level': 'DEBUG',
                'handlers': ['console'],
            },
            'file': {
                'level': 'INFO',
                'handlers': ['file'],
            },
        },
        # 'disable_existing_loggers': False,
    })
    return logging.getLogger(levelName)
