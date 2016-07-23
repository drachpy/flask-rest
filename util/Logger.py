import logging

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# fh = logging.FileHandler('debug.log')
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# fh.setFormatter(formatter)
# logger.addHandler(fh)

class ErrorLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.fh = logging.FileHandler('error.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
        self.fh.setFormatter(formatter)
        self.logger.addHandler(self.fh)

    def log(self, log):
        self.logger.error(log)


class InfoLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.fh = logging.FileHandler('info.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
        self.fh.setFormatter(formatter)
        self.logger.addHandler(self.fh)

    def log(self, log):
        self.logger.info(log)
