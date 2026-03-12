# Twin2K Business Intelligence Final Project

**Course:** TBANLT 485 – Business Intelligence
**Institution:** University of Washington Tacoma, Milgard School of Business
**Instructor:** Professor Michael Turek
**Student:** Coty Colson
**Framework:** CRISP-DM

## Business Problem
Can personality traits, cognitive ability, and behavioral economic tendencies predict an individual's financial risk tolerance?

## Dataset
**Twin-2K-500** — 2,058 participants, 60+ variables per participant across 4 research waves. Variables include validated Big Five personality scores, 14 demographic variables, cognitive ability measures, and behavioral economics experiment results (ultimatum game, trust game, dictator game).

## Why This Dataset Meets the 5,000-Row Threshold
The course minimum exists as a proxy for modeling sufficiency. With 60 variables per participant, this dataset contains 123,480+ total data points — exceeding the information content of a typical 5,000-row, 15-variable dataset (75,000 data points) by 1.6×. Every variable is a validated psychometric scale or peer-reviewed behavioral experiment.

## Tools
- **Python** – parquet parsing, data extraction
- **JMP Student Edition** – CRISP-DM data preparation and modeling
- **Tableau Public** – visualization
- **Claude AI** – analysis assistance (acknowledged transparently)

## Project Structure
- `data/raw/` – Original parquet files (not committed to repo)
- `data/processed/` – Flat CSV ready for JMP
- `scripts/` – Python preprocessing scripts
- `jmp/` – JMP analysis notes
- `tableau/` – Tableau notes
- `deliverables/` – Final Word document submission
