# 🧠 Twin2K Business Intelligence
### TBANLT 485 · University of Washington Tacoma · Milgard School of Business

> **Can personality traits, cognitive ability, and behavioral economic tendencies predict an individual's financial risk tolerance?**

---

## 🌐 Project Context: Modeling the Virtual Self

This repository explores the frontier of Business Intelligence through the lens of human digital twinning, utilizing the Twin2k-500 dataset (Toubia et al., 2025). While the concept of digital twins originated in aerospace and manufacturing — exemplified by the fully digital prototyping of the Boeing 777 — applying this technology to human behavior introduces a unique set of ethical and methodological challenges. Unlike industrial systems governed by the laws of physics, human twins are built upon self-reported psychometric data, requiring sophisticated calibration to account for social desirability bias and narrative agency. This project implements a predictive framework that balances functional optimization with a commitment to algorithmic fairness, seeking to model not just who a consumer is, but the psychological nuances that define their decision-making architecture.

---

## 📋 Project Overview

| | |
|---|---|
| **Course** | TBANLT 485 – Business Intelligence |
| **Instructor** | Professor Michael Turek |
| **Student** | Coty Colson |
| **Framework** | CRISP-DM |
| **Due Date** | March 17, 2026 |

This project applies the full CRISP-DM data mining framework to the **Twin-2K-500 dataset** — a large-scale behavioral and psychological survey of 2,058 participants — to build a predictive model for **financial risk tolerance** (`score_riskaversion`) from personality and cognitive variables.

---

## 🗂 Repository Structure

    twin2k-business-intelligence/
    ├── data/
    │   ├── raw/               # Parquet source files (local only, not committed)
    │   └── processed/
    │       └── twin2k_flat.csv  # 2,058 rows × 61 columns, JMP-ready
    ├── scripts/
    │   └── extract_scores.py  # Parquet → flat CSV extraction pipeline
    ├── jmp/
    │   └── notes.md           # JMP analysis notes (CRISP-DM phases)
    ├── tableau/
    │   └── notes.md           # Tableau visualization notes
    ├── deliverables/          # Final Word document submission
    ├── .gitignore
    └── README.md

---

## 📊 Dataset

**Twin-2K-500** is a peer-reviewed behavioral economics and personality dataset collected across 4 research waves.

| Attribute | Value |
|---|---|
| Participants | 2,058 |
| Variables per participant | 60+ |
| Total data points | 123,480+ |
| Source | Published psychometric research |

### Why This Dataset Meets the 5,000-Row Threshold

The course minimum exists as a proxy for *modeling sufficiency* — ensuring enough information to build meaningful models. Row count is a proxy for information density, but this dataset inverts the typical tradeoff:

| Dataset | Rows | Variables | Total Data Points |
|---|---|---|---|
| Typical course dataset | 5,000 | ~15 | ~75,000 |
| **Twin-2K-500** | **2,058** | **60+** | **123,480+** |

With **1.6× more information** than the 5,000-row benchmark — and every variable drawn from a validated psychometric scale or behavioral economics experiment — this dataset exceeds the modeling sufficiency threshold on information content while offering substantially higher data quality.

---

## 🎯 Business Problem

**Predicting financial risk tolerance from personality and behavioral traits.**

**Target Variable:** `score_riskaversion` — implied risk aversion coefficient from lottery choice experiments

**Predictor Categories:**

| Category | Variables |
|---|---|
| Big Five Personality | Extraversion, Agreeableness, Conscientiousness, Openness, Neuroticism |
| Cognitive Ability | Need for Cognition, CRT Score, Fluid Intelligence, Crystallized Intelligence, Numeracy |
| Economic Behavior | Ultimatum Game, Trust Game, Dictator Game, Mental Accounting |
| Demographics | Age, Income, Education Level, Gender |

---

## 🔄 CRISP-DM Phases

- [x] **Business Understanding** — Define business problem and target variable
- [x] **Data Understanding** — Univariate analysis, missing value assessment
- [ ] **Data Preparation** — Skewness correction, outlier detection, imputation, grouping
- [ ] **Modeling** — Stepwise regression (Forward, Backward, Mixed) in JMP
- [ ] **Evaluation** — Compare models by Validation R² and RASE
- [ ] **Deployment** — Document findings, build Tableau visualizations

---

## 🛠 Tools

| Tool | Purpose |
|---|---|
| Python (PyArrow, Pandas) | Parquet parsing, data extraction |
| JMP Student Edition | CRISP-DM data prep and modeling |
| Tableau Public | Visualization |
| Claude AI | Analysis assistance (transparently acknowledged) |
| GitHub | Version control and project documentation |

---

## 🚀 Getting Started

```bash
git clone https://github.com/cotycolson-sudo/twin2k-business-intelligence.git
cd twin2k-business-intelligence
pip install pandas pyarrow
python scripts/extract_scores.py
```

*TBANLT 485 · University of Washington Tacoma · Milgard School of Business*
