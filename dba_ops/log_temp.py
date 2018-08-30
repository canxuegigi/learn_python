#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import logging

def log_write(msg_level, msg):
    logging.basicConfig(level=logging.INFO,
                      format='%(asctime)s [%(levelname)s] %(message)s',
                      datefmt='%a,%Y-%m-%d %H:%M:%S',
                      filename='E:\pycharm_project\dba_ops\logs\operation.log',
                      filemode='a')
    if msg_level == 'INFO':
        logging.info(msg)
    elif msg_level == 'WARNING':
        logging.warning(msg)
    elif msg_level == 'ERROR':
        logging.error(msg)
    else:
        logging.critical(msg)

