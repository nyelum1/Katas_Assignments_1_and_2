from pathlib import Path
import pandas as pd
import argparse
import logging

# Setup the Logger
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

logging.info(f"file name : {path}")

# Use Context Manager to load data
# This ensures the file is handled safely
with open(args.filename, 'r') as file:
    logging.info(f"Reading file: {args.filename}")
    df = pd.read_csv(file)

    logging.info("writing df.head to screen")
    logging.info(df.head)

