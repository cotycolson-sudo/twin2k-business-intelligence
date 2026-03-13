# Twin2K Business Intelligence
### TBANLT 485 · Business Intelligence · University of Washington Tacoma
**Student:** Coty Colson | **Instructor:** Professor Michael Turek | **Due:** March 17, 2026
---
## Project Overview
This project applies the **CRISP-DM framework** to the **Twin-2K-500 dataset** — a large-scale behavioral and psychological survey of 2,058 participants across 4 research waves, spanning 500+ validated psychometric and behavioral economics variables.
**Central Business Problem:** Can personality traits, cognitive ability, and behavioral economic tendencies predict an individual's financial risk tolerance?
**Target Variable:** `score_riskaversion_recode` — implied risk aversion coefficient derived from incentivized lottery choice experiments (median-imputed for 233 missing values).
**Applications:** Personalized investment advising · Insurance pricing · Behavioral nudge design · Financial wellness coaching
---
## Dataset
| Attribute | Value |
|---|---|
| Name | Twin-2K-500 |
| Source | Toubia et al. (2025) — Published psychometric research |
| Participants | 2,058 |
| Variables (final) | 59 (after removing 2 unviable columns) |
| Numeric variables | 46 validated psychometric & behavioral scores |
| Categorical variables | 12 demographic variables |
| Research waves | 4 longitudinal waves |
| Format | Processed from 7 parquet files → `twin2k_flat.csv` |
> **Note on dataset size:** The course minimum of 5,000 rows is a proxy for modeling sufficiency. Twin-2K-500 has 60+ variables per participant = 123,480+ total data points vs. ~75,000 for a typical 5,000-row/15-variable dataset — a 1.6× information ratio. Every variable is a validated psychometric scale or behavioral economics experiment result.
---
## CRISP-DM Progress
| Phase | Status | Notes |
|---|---|---|
| Business Understanding | ✅ Complete | Target variable locked, business problem defined |
| Data Understanding | ✅ Complete | 46 numeric + 12 categorical variables fully profiled |
| Data Preparation | 🔄 In Progress | See breakdown below |
| Modeling | ⏳ Pending | Stepwise MLR (Forward / Backward / Mixed) + Decision Trees |
| Evaluation | ⏳ Pending | Compare by Validation R² and RASE |
| Deployment | ⏳ Pending | Final report + Tableau visualizations |
### Data Preparation Breakdown
| Step | Status | Finding |
|---|---|---|
| Skewness assessment | ✅ Complete | 0 variables exceed \|skewness\| > 10 — no transformations needed |
| Missing value imputation | ✅ Complete | `score_riskaversion_recode` (233 imputed) · `score_forwardflow_recode` (1 imputed) |
| Outlier detection (1.5×IQR) | ✅ Complete | 29 variables flagged — all within valid instrument ranges, none removed |
| Categorical grouping | ⏳ Pending | `religion` (12→5) · evaluate `employment_status` (7) |
| Multicollinearity check | ⏳ Pending | Flag \|r\| > 0.75 pairs |
| Final variable selection | ⏳ Pending | Confirm 18-predictor model |
---
## Planned Model Variables
**Target:** `score_riskaversion_recode`
**Predictors (18 planned):**
- **Big Five Personality (5):** extraversion, agreeableness, conscientiousness, openness, neuroticism
- **Cognitive Ability (5):** need for cognition, CRT-2, fluid intelligence, crystallized intelligence, numeracy
- **Economic Behavior (4):** ultimatum game, trust game, dictator game, mental accounting
- **Demographics (4):** age, income, education level, gender
---
## Repository Structure
```
twin2k-business-intelligence/
├── README.md
├── ETHICS.md                        ← Ethical framework for human digital twins
├── .gitignore
├── data/
│   ├── raw/                         ← Parquet files (local only, not committed)
│   └── processed/
│       └── twin2k_flat.csv          ← 2,058 × 61 processed dataset
├── scripts/
│   └── extract_scores.py            ← Parquet → CSV extraction pipeline
├── jmp/
│   ├── twin2k_flat.jmp              ← JMP data table (variable types + recode columns configured)
│   └── notes.md
├── tableau/
│   └── notes.md
└── deliverables/
    └── DataUnderstanding_CotypColson_v2.docx  ← WIP report (screenshots pending)
```
---
## Ethical Framework
See [`ETHICS.md`](ETHICS.md) for full documentation. Key principles:
- **Stochastic vs. deterministic twins** — human behavioral data is probabilistic, not deterministic (unlike industrial digital twins)
- **Ideal Self skew** — self-reported data calibrated against `score_socialdesirability`
- **Uncertainty quantification** — probabilistic outputs over binary predictions
- **No outlier removal** — extreme human responses are valid data points, not errors
---
## Tools & Workflow
| Tool | Purpose |
|---|---|
| JMP Pro | Primary modeling platform (stepwise regression, decision trees) |
| Tableau Public 2025.3 | Visualizations (data extract mode for publishing) |
| Python | Parquet extraction · preprocessing pipeline |
| Claude (Anthropic) | Research support · document structuring · AI assistance |
*Analysis decisions, variable selections, and modeling interpretations reflect independent student judgment.*
---
*TBANLT 485 · Milgard School of Business · University of Washington Tacoma · March 2026*
