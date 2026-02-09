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

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=Path)
args = parser.parse_args()

path = Path(args.filename)

logging.info("testing argparse for file inputs")