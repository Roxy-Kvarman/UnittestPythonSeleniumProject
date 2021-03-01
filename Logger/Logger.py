import logging
import sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='C:\\Users\\roxy.kvarman\\PycharmProjects\\UnittestPythonSeleniumProject\\Logs\\tests.log',
                    filemode='a')
logger = logging.getLogger()
sys.stderr.write = logger.error
sys.stdout.write = logger.info
