import psutil

def is_process_running(process_number):
    """Check if the process is running"""
    process_name = "process-"+process_number+".sh"
    for psaux in psutil.process_iter():
        try:
            if process_name in psaux.name():
                return True
        except (psutil.Error):
            pass
    return False;