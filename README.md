# Lifestyle Risk Analytics

Multi-dataset health analytics project that studies how lifestyle factors (physical activity, BMI, stress, and age) relate to diabetes, heart disease, and sleep outcomes.

## Why this project matters

Healthcare data is often analyzed in silos. This project combines three complementary datasets to identify patterns that appear across conditions, not just inside one disease domain. The result is a lightweight analytics workflow that can support risk-awareness dashboards, prevention campaigns, or early-stage product prototyping in health-tech.

## What this repository does

- Cleans and standardizes three raw health datasets.
- Produces focused analyses for diabetes, heart disease, and sleep health.
- Generates cross-dataset insights around physical activity as a shared protective factor.
- Saves publication-ready charts (`.png`) for reporting and portfolio use.

## Key insights

- Higher BMI is associated with more advanced diabetes categories.
- Heart disease prevalence increases with age and aligns with higher cholesterol/BP.
- Stress level is negatively correlated with sleep duration.
- Physical activity shows beneficial signals in both diabetes and sleep contexts.

## Repository structure

```text
.
├── raw_data/                              # Source datasets
├── cleaned_data/                          # Outputs from cleaning script
├── clean_dataset.py                       # Cleaning pipeline
├── diabetes_analysis.py                   # Diabetes-focused analysis
├── heart_analysis.py                      # Heart disease-focused analysis
├── sleep_analysis.py                      # Sleep-focused analysis
├── combine_analysis.py                    # Cross-dataset analysis
├── requirements.txt                       # Python dependencies
└── *.png                                  # Generated visual outputs
```

## Quick start

### 1) Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Run data cleaning

```bash
python3 clean_dataset.py
```

### 3) Run analyses

```bash
python3 diabetes_analysis.py
python3 heart_analysis.py
python3 sleep_analysis.py
python3 combine_analysis.py
```

## Outputs

- `diabetes_health_insights.png`
- `heart_disease_insights.png`
- `sleep_health_insights.png`
- `combined_physical_activity_impact.png`

## Data sources

- BRFSS 2015 diabetes indicators dataset
- Heart disease prediction dataset
- Sleep health and lifestyle dataset

See `raw_data/` for files included in this project snapshot.

## Suggested GitHub repository metadata

### Better repository name ideas

- `lifestyle-risk-analytics`
- `multi-dataset-health-analytics`
- `health-lifestyle-insights`

### Suggested GitHub topics (tags)

`python`, `data-analysis`, `healthcare-analytics`, `pandas`, `matplotlib`, `public-health`, `data-visualization`, `risk-analysis`, `portfolio-project`

## Notes

- This project provides observational analysis, not medical diagnosis.
- Use outputs for educational/research and portfolio purposes.
