from pathlib import Path
import pandas as pd
import argparse
import logging

# 1. Setup the Logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("log.log"),
        logging.StreamHandler()
    ],
)

logging.info("testing logger for printing and saving log file to disk")