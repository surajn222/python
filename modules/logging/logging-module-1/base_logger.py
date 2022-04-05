import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to info
handler = logging.StreamHandler()

#File format
log_file_format = "[%(levelname)s] - %(asctime)s - %(name)s - %(pathname)s:%(lineno)d : %(message)s"
formatter = logging.Formatter(log_file_format)

#Formatter
handler.setFormatter(formatter)
logger.addHandler(handler)
