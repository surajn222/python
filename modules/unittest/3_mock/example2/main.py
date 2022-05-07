# main.py
from time import sleep
from main2 import is_windows


def get_operating_system():
    print("Here")
    return 'Windows' if is_windows() else 'Linux'

get_operating_system()