import subprocess
from daemon_supervisor import daemon_supervisor_functions
import logging

class ProcessManager:
    __instance = None
    _process_number = "0"
    _secs_per_attempt = "1"
    _number_attempts = 1
    __attemptsFailed = 0

    def __new__(self, process_number, secs_per_attempt, number_attempts):
        """Singleton Implementation
        Parameters
        ----------
        process_number : int
            Number of the process, the file should be in /tasks/process-<process_number>.sh
        secs_per_attempt : double
            Seconds to wait for process response
        number_attempts: int
            Number of attempts in case the process fail
        """    
        if ProcessManager.__instance is None:
            ProcessManager.__instance = object.__new__(self)
        
        ProcessManager.__instance._process_number = process_number
        ProcessManager.__instance._secs_per_attempt = secs_per_attempt
        ProcessManager.__instance._number_attempts = number_attempts

        return ProcessManager.__instance
    
    def start_process(self):
        """Starting the process"""
        logging.info('Starting Process' + ProcessManager.__instance._process_number)
        process = subprocess.Popen(["/bin/bash -c processes/process-"+ProcessManager.__instance._process_number+".sh"], shell=True, stdout=False, close_fds=True)
        """"Waiting time to validate later if there is some error"""
        try:
            stream_data = process.communicate(timeout=ProcessManager.__instance._secs_per_attempt)[0]
        except subprocess.TimeoutExpired:
            return True
        
        if process.returncode == 1:
            ProcessManager.__instance.__attemptsFailed=ProcessManager.__instance.__attemptsFailed+1
            logging.warning('The attempt to start the process failed.')
            return False
        else:
            logging.info('Process Finished Successfuly')
            return True
    
    def start_process_recovery(self):
        """Start Process Recovery Operation"""
        if not ProcessManager.__instance.start_process():
            while ProcessManager.__instance.__attemptsFailed < ProcessManager.__instance._number_attempts:
                if daemon_supervisor_functions.is_process_running(ProcessManager.__instance._process_number):
                    ProcessManager.__instance.__attemptsFailed = 0
                    break
                else:
                    ProcessManager.__instance.start_process()
            logging.error('Process could not be started')
            return False



        
        

        














"""


x = ProcessManager()
setattr(x, '_value', "8")
print (getattr(x,'_value')) 
y = ProcessManager()
setattr(y, '_value', "3")
print (getattr(y,'_value')) 
print (getattr(x,'_value')) 
"""