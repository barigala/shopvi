import logging
import allure
import os

def customLogger(logLevel=logging.DEBUG):
    # Define the log directory and file
    log_dir = "D:\\PyProjects\\shopvipytest\\tests\\reports"
    log_file = os.path.join(log_dir, "testreport.log")

    # Ensure the directory exists
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger("ShopVI")  # Updated logger name
    logger.setLevel(logLevel)

    # Clear previous handlers if any (to avoid duplicate logs)
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler to write logs to a file, always overwrite
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(logLevel)

    # Formatter for the log file
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    # Adding the file handler to the logger
    logger.addHandler(file_handler)

    return logger

def allureLogs(message):
    with allure.step(message):
        pass
