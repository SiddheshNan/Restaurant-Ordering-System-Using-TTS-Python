from threading import Thread
import os
import main
import wsserver
import signal
import time

try:
    Thread(target=wsserver.WebServer().start()).start()
    time.sleep(3)
    Thread(target=main.doStart).start()
except (KeyboardInterrupt, SystemExit):
    print('\n! Received keyboard interrupt, quitting threads.\n')
