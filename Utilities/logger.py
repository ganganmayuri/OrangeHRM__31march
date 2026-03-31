import inspect
import logging


class logger_class:
    @staticmethod
    def get_logger():
        logger = logging.getLogger("Orange_HRM")
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('.\\Logs\\Orange_HRM.logs')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger


