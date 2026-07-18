# Spark Job Cost Anomaly Detector

Detects Spark training and feature engineering jobs whose runtime cost or retry behavior is outside expected bounds.

Focus: Spark, ML training reliability, cloud cost guardrails, SRE.

Portfolio framing: Apple-scale client-style platform project using synthetic data only.

## Run

```bash
python3 spark_cost_anomaly.py sample_jobs.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```
