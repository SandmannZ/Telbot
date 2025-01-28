import logging

def setup_logger(log_file="bot.log"):
    """
    Configures and returns a logger.
    """
    logging.basicConfig(
        level=logging.INFO,  # Set to DEBUG to capture all logs
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=log_file,
        filemode="a",  # Append to the log file
    )
    logger = logging.getLogger()
    return logger
