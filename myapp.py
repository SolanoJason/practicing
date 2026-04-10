import logging

logger = logging.getLogger("simple_example")

logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
logger.addHandler(handler)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s %(message)s")
handler.setFormatter(formatter)

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")