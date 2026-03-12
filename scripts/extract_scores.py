# extract_scores.py
# Reads Twin-2K-500 parquet files, selects relevant columns (Big Five scores,
# demographics, cognitive ability, behavioral economics variables, and financial
# risk tolerance), and writes a flat CSV to data/processed/ for use in JMP.

DATA_RAW_PATH = "/mnt/user-data/uploads/"
DATA_PROCESSED_PATH = "data/processed/twin2k_flat.csv"

import pandas as pd
import pyarrow
import re
import os
import json


def main():
    # extraction logic coming next
    pass


if __name__ == "__main__":
    main()
