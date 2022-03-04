# Daemon Supervisor 

This project executes a bash script and keep it running as much as possible.

## Installation

```bash
$ pip install -r requirements.txt

```

## Usage

**Alfa** usage by now:

* I have some processes in 'processes' folder, make the modification you want, each script has a number in their filename. 
* Open run.py and modify start execution by choosing:
    * process_number: The script file you want to run
    * interval: Checking interval for validating if the process is running
    * secs_per_attempt: The process must overcome this timeout to be considered as recovered.
    * number_attempts: Number of attempts to start the process during recovery mode. 
* Then you just need to run it in python3 :)

## Monitoring

Take a look at app_log.log to see what happen on each case.