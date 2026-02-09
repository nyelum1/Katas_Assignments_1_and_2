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
with open(path, 'r') as file:
    logging.info(f"Reading file: {path}")
    df = pd.read_csv(file)


# Filtering
logging.info("filtering the dataframe")
filtered_df = df[df['REPORT_TYPE'] == "FM-15"]


# Save and Log
output = Path("Result.csv")
filtered_df.to_csv(output, index=False)
logging.info(f"Done! Saved {len(filtered_df)} rows to {output}")

