# Skills and verification

## What this repository demonstrates

A Spark cost review tool that checks cost against baseline, retry count, and executor hours. Its report lists each anomalous job with the reasons operators can investigate.

## Reproduce the result

The feature build shows a cost spike. Ranking training also shows a retry storm and capacity hotspot. Reproduce the primary fixture with `python3 spark_cost_anomaly.py sample_jobs.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The thresholds work on exported summaries. Use job timelines and executor metrics to identify the cause before tuning a cluster.

Use the reason codes to separate cost changes, retry bursts, and executor-hour hotspots before contacting the listed team.

[spark_cost_anomaly.py](../spark_cost_anomaly.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
