#!/usr/bin/env python3

import logging

logger = logging.getLogger(__name__)

def log():
    logger.info("An INFO message from " + __name__)
    logger.error("An ERROR message from + " + __name__)