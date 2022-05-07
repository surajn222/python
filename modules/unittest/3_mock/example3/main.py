# main.py
from time import sleep
import main2

def get_operating_system():
    print("Here")
    return 'Windows' if main2.is_windows() else 'Linux'

get_operating_system()