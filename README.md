# Twin2K Business Intelligence

### TBANLT 485 · Business Intelligence · University of Washington Tacoma

**Student:** Coty Colson | **Instructor:** Professor Michael Turek | **Completed:** March 17, 2026

---

## Project Overview

This project applies the **CRISP-DM framework** to the **Twin-2K-500 dataset** — a large-scale behavioral and psychological survey of 2,058 participants across 4 research waves, spanning 500+ validated psychometric and behavioral economics variables.

**Central Business Problem:** Can personality traits, cognitive ability, and behavioral economic tendencies predict an individual's financial risk tolerance?

**Target Variable:** `score_riskaversion_recode` — implied risk aversion coefficient derived from incentivized lottery choice experiments (median-imputed for 233 missing values).

**Applications:** Personalized investment advising · Insurance pricing · Behavioral nudge design · Financial wellness coaching

---

## Central Finding

> Three independent modeling approaches converge on the same conclusion: the Twin-2K-500 instrument cannot predict financial risk aversion with deployment-ready accuracy. The best predictive model explains **1.5% of variance** (Validation R²=0.015). This is a meaningful finding, not a modeling failure — the result is consistent across methods and robust to model complexity.

**The digital twin concept is commercially sound. The measurement instrument needs rethinking:** away from self-report personality proxies, toward longitudinal, incentivized, domain-specific behavioral data.

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
| Data Preparation | ✅ Complete | See breakdown below |
| Modeling | ✅ Complete | Explanatory MLR + 3 stepwise runs + Bootstrap Forest |
| Evaluation | ✅ Complete | 3-variable linear model selected as final |
| Deployment | ✅ Complete | Final report + Tableau dashboard + repo artifacts |

### Data Preparation Breakdown

| Step | Status | Finding |
|---|---|---|
| Skewness assessment | ✅ Complete | 0 variables exceed \|skewness\| > 10 — no transformations needed |
| Missing value imputation | ✅ Complete | `score_riskaversion_recode` (233 imputed, median=0.07) · `score_forwardflow_recode` (1 imputed, median=0.82) |
| Outlier detection (1.5×IQR) | ✅ Complete | 29 variables flagged — all within valid instrument ranges, none removed |
| Categorical grouping | ✅ Complete | `religion` recoded 12→6 groups (top 5 by avg target + Other_Religion) |
| Multicollinearity check | ✅ Complete | 0 pairs exceeded \|r\| > 0.75 — all 18 predictors retained |
| Final variable selection | ✅ Complete | 18-predictor model confirmed (5 Big Five + 5 cognitive + 4 behavioral + 4 demographic) |

---

## Final Model Variables

**Target:** `score_riskaversion_recode`

**Predictors (18):**

- **Big Five Personality (5):** extraversion, agreeableness, conscientiousness, openness, neuroticism
- **Cognitive Ability (5):** need for cognition, CRT-2, fluid intelligence, crystallized intelligence, numeracy
- **Economic Behavior (4):** ultimatum game, trust game, dictator game, mental accounting
- **Demographics (4):** age, income, education level, gender

---

## Modeling Results

### Model Comparison

| Model | OOB Error / RMSE | R² | Predictors | Notes |
|---|---|---|---|---|
| Explanatory MLR | 0.2270 | 0.027 | 18 | No partition — for interpretation |
| **Predictive MLR — Forward BIC** | **0.2271** | **0.015** | **3** | **✅ Final model** |
| Predictive MLR — Backward BIC | 0.2271 | 0.015 | 3 | Identical to Forward |
| Predictive MLR — Mixed (p≤0.25) | 0.2264 | 0.021 | 12 | Worse BIC — overfitting |
| Bootstrap Forest | 0.2950 (RASE) | — | 18 | OOB honest error |

### Final Predictive Model Equation

```
score_riskaversion_recode = 0.1315
  − 0.000573 × score_trustgame_sender
  − 0.01669  × income[$75k–$100k]
  − 0.01901  × age[18–29]
```

### Significant Predictors (Explanatory MLR, p < 0.05)

| Variable | p-value | Direction |
|---|---|---|
| score_trustgame_sender | 0.005 | Higher trust → lower risk aversion |
| crt2_score | 0.008 | Higher CRT → lower risk aversion |
| income[$75k–$100k] | 0.006 | This bracket → lower risk aversion |
| age[18–29] | 0.006 | Younger adults → lower risk aversion |

### Bootstrap Forest — Top 5 Variable Importance

| Variable | Importance | Category |
|---|---|---|
| score_needforcognition | 8.0% | Cognitive |
| score_neuroticism | 7.8% | Big Five |
| score_extraversion | 7.5% | Big Five |
| education_level | 7.1% | Demographic |
| score_openness | 6.9% | Big Five |

> **Key analytical tension:** All five Big Five traits ranked in the top 8 by forest importance, yet none were significant in the explanatory MLR — suggesting nonlinear interaction effects that linear regression cannot detect. Those interactions were still insufficient to improve out-of-sample accuracy (forest RASE 0.2950 vs. linear model RMSE 0.2271).

---

## Repository Structure

```
twin2k-business-intelligence/
├── README.md
├── ETHICS.md                              ← Ethical framework for human digital twins
├── .gitignore
├── data/
│   ├── raw/                               ← Parquet files (local only, not committed)
│   └── processed/
│       └── twin2k_flat.csv                ← 2,058 × 61 processed dataset
├── scripts/
│   └── extract_scores.py                  ← Parquet → CSV extraction pipeline
├── jmp/
│   ├── twin2k_flat.jmp                    ← JMP data table with recode columns + embedded model scripts
│   └── notes.md
├── tableau/
│   ├── viz_variable_importance.csv        ← Bootstrap Forest importance by category
│   ├── viz_model_comparison.csv           ← Model comparison (RMSE, R², predictors)
│   ├── viz_risk_distribution.csv          ← Risk aversion score distribution (10 bins)
│   ├── viz_stepwise_history.csv           ← Forward stepwise BIC by step
│   └── notes.md
└── deliverables/
    ├── Twin2K_FinalReport_CotypColson.docx   ← Full CRISP-DM report (all 6 phases + screenshots)
    ├── Twin2K_DataDictionary_CotypColson.docx ← 59 variables, 8 color-coded sections
    ├── DataUnderstanding_CotypColson_v2.docx  ← Earlier working draft
    └── model_outputs/                         ← PDF exports of all JMP model windows
        ├── explanatory_mlr.pdf
        ├── stepwise_forward.pdf
        ├── stepwise_backward.pdf
        ├── stepwise_mixed.pdf
        └── bootstrap_forest.pdf
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
| JMP Student Edition | Primary modeling platform (MLR, stepwise regression, Bootstrap Forest) |
| Tableau Public 2025.3 | Dashboard — *"Can a Digital Twin Predict Your Financial Risk Tolerance?"* |
| Python | Parquet extraction · preprocessing pipeline |
| Claude (Anthropic) | Research support · document structuring · AI assistance |

*Analysis decisions, variable selections, and modeling interpretations reflect independent student judgment.*

---

*TBANLT 485 · Milgard School of Business · University of Washington Tacoma · March 2026*
