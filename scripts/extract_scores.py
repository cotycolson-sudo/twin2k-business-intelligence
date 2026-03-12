"""
extract_scores.py
-----------------
Parse Twin-2K-500 persona parquet files and produce a flat CSV for JMP analysis.

Usage:
    python scripts/extract_scores.py

Configure DATA_RAW_PATH and DATA_PROCESSED_PATH below to match your local
directory layout before running.
"""

import re
import os
import pandas as pd

# ---------------------------------------------------------------------------
# Configuration – adjust these paths to match your local environment
# ---------------------------------------------------------------------------
DATA_RAW_PATH = "data/raw"          # directory containing persona_chunk_001..007.parquet
DATA_PROCESSED_PATH = "data/processed"  # output directory
OUTPUT_FILENAME = "twin2k_flat.csv"

# ---------------------------------------------------------------------------
# Ordered list of the 7 source parquet files
# ---------------------------------------------------------------------------
PARQUET_FILES = [
    f"persona_chunk_{str(i).zfill(3)}.parquet" for i in range(1, 8)
]

# ---------------------------------------------------------------------------
# Demographic fields and the label text that precedes them in persona_summary
# (case-insensitive match is used when searching)
# ---------------------------------------------------------------------------
DEMOGRAPHIC_FIELDS = {
    "geographic_region":    "geographic region",
    "gender":               "gender",
    "age":                  "age",
    "education_level":      "education level",
    "race":                 "race",
    "marital_status":       "marital status",
    "religion":             "religion",
    "religious_attendance": "religious attendance",
    "political_affiliation":"political affiliation",
    "income":               "income",
    "political_views":      "political views",
    "employment_status":    "employment status",
}

# ---------------------------------------------------------------------------
# Numeric score variables extracted via "variable_name = <number>" patterns.
# Variables that contain hyphens (ST-TW, CNFU-S) need literal hyphens in the
# regex – these are handled automatically by re.escape() in the extractor.
# ---------------------------------------------------------------------------
SCORE_VARIABLES = [
    "score_extraversion",
    "score_agreeableness",
    "wave1_score_conscientiousness",
    "score_openness",
    "score_neuroticism",
    "score_needforcognition",
    "score_agency",
    "score_communion",
    "score_minimalism",
    "score_BES",
    "score_GREEN",
    "crt2_score",
    "score_fluid",
    "score_crystallized",
    "score_syllogism_merged",
    "score_actual_total",
    "score_overconfidence",
    "score_overplacement",
    "score_ultimatum_sender",
    "score_ultimatum_accepted",
    "score_mentalaccounting",
    "score_socialdesirability",
    "wave2_score_conscientiousness",
    "score_anxiety",
    "score_HI",
    "score_HC",
    "score_VI",
    "score_VC",
    "score_finliteracy",
    "score_numeracy",
    "score_deductive_certainty",
    "score_forwardflow",
    "score_discount",
    "score_presentbias",
    "score_riskaversion",
    "score_lossaversion",
    "score_trustgame_sender",
    "score_trustgame_receiver",
    "score_RFS",
    "score_ST-TW",          # hyphen in name – handled by re.escape()
    "score_depression",
    "score_CNFU-S",         # hyphen in name – handled by re.escape()
    "score_selfmonitor",
    "score_SCC",
    "score_needforclosure",
    "score_maximization",
    "score_wason",
    "score_dictator_sender",
]


# ---------------------------------------------------------------------------
# Extraction helpers
# ---------------------------------------------------------------------------

def extract_demographic(text: str, label: str) -> str | None:
    """
    Extract the value that follows a labeled line such as:
        "Gender: Male"
        "Geographic Region: Midwest"

    Returns a stripped string or None if not found.
    The match is case-insensitive and allows optional whitespace around ':'.
    """
    # Match "<label>: <value>" where value runs to end of line
    pattern = re.compile(
        r"(?i)(?:^|\n)\s*" + re.escape(label) + r"\s*:\s*(.+)",
    )
    m = pattern.search(text)
    if m:
        return m.group(1).strip()
    return None


def extract_score(text: str, var_name: str) -> float | None:
    """
    Extract the numeric value from a pattern like:
        "score_extraversion = 3.75"
        "score_ST-TW = 0.5"

    re.escape() handles hyphens and other special chars in variable names.
    Accepts integers, floats, and negative numbers.
    Returns a Python float or None if not found.
    """
    pattern = re.compile(
        r"(?:^|[\s,;(])" + re.escape(var_name) + r"\s*=\s*(-?\d+(?:\.\d+)?)",
        re.MULTILINE,
    )
    m = pattern.search(text)
    if m:
        return float(m.group(1))
    return None


def parse_row(row: pd.Series) -> dict:
    """
    Given a DataFrame row that contains a `persona_summary` text field,
    return a flat dict of all demographic and score variables.
    """
    text = row.get("persona_summary", "") or ""

    record: dict = {}

    # --- demographic variables (string) ---
    for col, label in DEMOGRAPHIC_FIELDS.items():
        record[col] = extract_demographic(text, label)

    # --- numeric score variables ---
    for var in SCORE_VARIABLES:
        record[var] = extract_score(text, var)

    return record


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def main() -> None:
    # 1. Load and concatenate all 7 parquet files
    frames: list[pd.DataFrame] = []
    for filename in PARQUET_FILES:
        path = os.path.join(DATA_RAW_PATH, filename)
        print(f"Loading {path} …")
        df_chunk = pd.read_parquet(path)
        frames.append(df_chunk)

    df_raw = pd.concat(frames, ignore_index=True)
    print(f"\nConcatenated dataframe shape: {df_raw.shape}")

    # 2. Validate that required columns are present
    required_cols = {"pid", "persona_summary"}
    missing_cols = required_cols - set(df_raw.columns)
    if missing_cols:
        raise ValueError(f"Source data is missing required columns: {missing_cols}")

    # 3. Parse every row
    print("\nParsing persona_summary for each participant …")
    parsed_records = df_raw.apply(parse_row, axis=1)
    df_parsed = pd.DataFrame(list(parsed_records))

    # 4. Combine pid with parsed columns
    df_out = pd.concat([df_raw[["pid"]].reset_index(drop=True), df_parsed], axis=1)

    # 5. Write output CSV
    os.makedirs(DATA_PROCESSED_PATH, exist_ok=True)
    out_path = os.path.join(DATA_PROCESSED_PATH, OUTPUT_FILENAME)
    df_out.to_csv(out_path, index=False)
    print(f"\nWrote {out_path}")

    # 6. Summary report
    n_rows, n_cols = df_out.shape
    print(f"\n{'='*60}")
    print(f"  Total rows written   : {n_rows}")
    print(f"  Total columns written: {n_cols}")
    print(f"{'='*60}")

    # Missing-value counts
    print("\nMissing value counts per column:")
    missing = df_out.isnull().sum()
    WARN_THRESHOLD = 50
    any_warned = False
    for col, cnt in missing.items():
        if cnt > 0:
            warn = ""
            if cnt > WARN_THRESHOLD:
                warn = "  *** WARNING: >50 missing ***"
                any_warned = True
            print(f"  {col:<45} {cnt:>6}{warn}")

    if not any_warned:
        print("  (no column exceeds 50 missing values)")

    # Preview first 3 rows (transpose for readability)
    print(f"\n{'='*60}")
    print("First 3 rows preview (selected columns):")
    print(f"{'='*60}")
    preview_cols = ["pid"] + list(DEMOGRAPHIC_FIELDS.keys()) + SCORE_VARIABLES[:5]
    preview_cols = [c for c in preview_cols if c in df_out.columns]
    print(df_out[preview_cols].head(3).to_string(index=False))
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
