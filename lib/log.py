import os
import logging

looperpath = os.environ.get('LOOPERPATH')
def precheck():

    if looperpath is None:
        logging.error('$LOOPERPATH environment var not set, is this sourced?')
        exit(1)

    if not os.path.exists(os.path.join(looperpath, 'logs')):
        os.mkfifo(os.path.join(looperpath, 'logs'))

    logging.info("looper system started :) .")


def logger():
    logs = ""
    while True:
        print('reading uwu')
        with open(os.path.join(looperpath, 'logs'), 'r') as logfile:
            logs = logfile.read()
        if logs == "quit\n":
            logging.info(logs)
            break

        print("AAA '{}'".format(logs))
        logging.info(logs)


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    try:
        precheck()
        logger()
    except KeyboardInterrupt:
        logging.info("quitting")


