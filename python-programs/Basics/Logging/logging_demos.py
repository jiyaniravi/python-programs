import logging
import os

logging.basicConfig(filename='logs.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# logging.disable(logging.INFO)

logging.debug('This is debug log')
logging.info('This is info log')
logging.warning('This is warn log')
logging.error('This is error log')
logging.critical('This is critical log')

print(os.getcwd())  #A:\B\C\D\python-programs