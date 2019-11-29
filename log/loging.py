#!/usr/bin/python3
# coding=utf-8

import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG, format="%(asctime)s %(filename)s[line:%(lineno)d] %(message)s",
                    datefmt="datefmt='%Y-%m-%d %X'")

logging.info("info logging")
logging.debug("debug logging")
logging.warning("warning logging")
logging.error("error logging")
logging.critical("critical logging")