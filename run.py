import logging
import time
from daemon_supervisor import daemon_supervisor_functions
from daemon_supervisor import process_manager

logging.basicConfig(filename="app_log.log",
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG)

def start(process_number, secs_per_attempt, number_attempts, interval):
    manager = process_manager.ProcessManager(process_number, secs_per_attempt, number_attempts)
    dont_give_up=True

    while dont_give_up == True:
        if daemon_supervisor_functions.is_process_running(process_number):
            logging.info('Process Running :)')
            time.sleep(interval)
        else:
            logging.warning('Going to Recovery Process')
            if manager.start_process_recovery() == False:
                dont_give_up = False


start("5", 6, 15 , 1)

