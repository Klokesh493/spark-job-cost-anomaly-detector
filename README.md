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

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Business problem

A Spark workload can finish successfully while a retry storm or resource spike drives cost above its baseline.

## Project walkthrough

```mermaid
flowchart LR
    A["Spark job cost, retries, and executor hours"]
    B["Check cost ratio, retry count, and compute thresholds"]
    C{"Anomaly reason found?"}
    D["Emit job, owner team, and reason codes"]
    E["Omit healthy job"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
