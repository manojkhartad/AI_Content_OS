# ==========================================================
# Imports
# ==========================================================

import logging
from datetime import datetime
from pathlib import Path


# ==========================================================
# Log Directory
# ==========================================================

LOGS_DIR = Path("logs")

LOGS_DIR.mkdir(

    parents=True,

    exist_ok=True

)


# ==========================================================
# Log File
# ==========================================================

LOG_FILE = (

    LOGS_DIR /

    f"{datetime.now():%Y-%m-%d}.log"

)


# ==========================================================
# Logger
# ==========================================================

class Logger:

    _logger = None

    # ------------------------------------------------------
    # Get Logger
    # ------------------------------------------------------

    @classmethod
    def get_logger(cls):

        if cls._logger is not None:

            return cls._logger

        logger = logging.getLogger(

            "AI_Content_OS"

        )

        logger.setLevel(

            logging.INFO

        )

        logger.propagate = False

        # ----------------------------------------------
        # Formatter
        # ----------------------------------------------

        formatter = logging.Formatter(

            "%(asctime)s | %(levelname)-8s | %(message)s",

            "%Y-%m-%d %H:%M:%S"

        )

        # ----------------------------------------------
        # File Handler
        # ----------------------------------------------

        file_handler = logging.FileHandler(

            LOG_FILE,

            encoding="utf-8"

        )

        file_handler.setFormatter(

            formatter

        )

        # ----------------------------------------------
        # Console Handler
        # ----------------------------------------------

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(

            formatter

        )

        # ----------------------------------------------
        # Avoid Duplicate Handlers
        # ----------------------------------------------

        if not logger.handlers:

            logger.addHandler(

                file_handler

            )

            logger.addHandler(

                console_handler

            )

        cls._logger = logger

        return logger


# ==========================================================
# Global Logger
# ==========================================================

logger = Logger.get_logger()