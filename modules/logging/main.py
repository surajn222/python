import os
import sys
from modules.logging.loggingInitializer import *
from modules.logging.module2 import *
from modules.logging.loggingInitializer import *
from modules.logging.main2 import *

def loggingInitializer():
    logger = initialize_logger(".")
    logger.info("Test logging: Main file")

loggingInitializer()
main2 = main2()

