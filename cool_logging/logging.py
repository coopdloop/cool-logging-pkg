"""logging.py"""
from datetime import datetime
import requests
from functools import wraps
from termcolor import colored

def simple_logging(func):
    """Simple logging decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            # method = colored(func.__name__, color="blue")
            method_all = colored(func.__qualname__, color="blue")
            args_str = colored(str(args), color='yellow')
            kwargs_str = colored(str(kwargs), color='magenta')
            response = f"call to {method_all} {args_str} {kwargs_str}"
            if func.__name__ in "__log":
                response = f"logging {colored(result, 'cyan', attrs=['bold'])}"
            print(
                colored(text=f"{datetime.now():%H:%M:%S}", color="green"),
                end=" ")
            print(f"{response}")
            return result
        except requests.exceptions.RequestException as err:
            if isinstance(err, requests.exceptions.HTTPError):
                print(
                    colored(
                        text=f"{datetime.now():%H:%M:%S}", color="red"),
                    end=" ")
                print(f"{err}")
    return wrapper

class CoolLogger:
    def __init__(self, log_file_path=None):
        self.log_file_path = log_file_path

    def set_log_file_path(self, log_path):
        self.log_file_path = log_path

    def __write_log(self, log_entry):
        if self.log_file_path:
            with open(self.log_file_path, 'a') as log_file:
                log_file.write(log_entry + '\n')
        else:
            print(log_entry)
            


    @simple_logging
    def text_log(self, text):
        return text
