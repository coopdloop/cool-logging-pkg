"""utils.py"""
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
            args = colored(args, color='yellow')
            kwargs = colored(kwargs, color='magenta')
            response = f"call to {method_all} {args} {kwargs}"
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
                    colored(text=f"{datetime.now():%H:%M:%S}", color="red"),
                    end=" ")
                print(f"{err}")
    return wrapper


@simple_logging
def text_log(text):
    return text
