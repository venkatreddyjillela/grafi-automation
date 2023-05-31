import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        file_handler = logging.FileHandler(filename=".\\Logs\\automation.log", mode='a')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        # logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        if not logger.hasHandlers():
            # logger.addHandler(stdout_handler)
            logger.addHandler(file_handler)
        return logger