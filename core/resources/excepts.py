import sys
import logging
import tkinter as tk
from tkinter import messagebox
import traceback
from resources import functions

with open('logger.log', 'w') as file:
    pass  # Better way (?) to create if doesnt exists and delete everything inside

logger = logging.getLogger(__name__)
def handle_exception(exc_type, exc_value, exc_traceback, tkobj=None):
    print('type:', exc_type, 'value:', exc_value, 'tb:', exc_traceback, 'tk:', tkobj)
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    exc = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback, chain=False))
    exc_chain = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback, chain=True))

    logger.critical('Unhandled exception\n\n{}\n'.format(exc_chain))
    with open('logger.log', 'r') as loggerfile, \
        open('exception_logger.log', 'w') as excloggerfile:
        for line in loggerfile:
            excloggerfile.write(line)

    if 'During handling of the above exception, another exception occurred:' in exc_chain:
        exc = 'During handling of the last exception, another exception occurred:\n' + exc
    functions.show_window_messagebox('Unhandled exception', 'An unexpected error ocurred.\nYou can send the "exception_logger.log" to the author of this program.\nMore details of the error:\n\n' + exc, geometry='*', button='OK')


def tkinter_exception(tkobj, exc_type, exc_value, exc_traceback):
    handle_exception(exc_type, exc_value, exc_traceback, tkobj)


def except_exception(exc_type, exc_value, exc_traceback):
    handle_exception(exc_type, exc_value, exc_traceback)


logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] (%(levelname)s)\t%(message)s')

stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logger.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)

sys.excepthook = except_exception
tk.Tk.report_callback_exception = tkinter_exception

logger.info('Logger ready')