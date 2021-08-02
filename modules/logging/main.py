import os
import sys
from modules.logging.loggingInitializer import *
from modules.logging.module2 import *

def main():
    logging = initialize_logger(".")
    logging.info("INFO LOG")
    logging.info("WARN LOG")
    logging.debug("DEBUG LOG")

    module2class = sampleClass()
    module2class = sampleClass()

main()

