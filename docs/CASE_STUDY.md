# Spark Job Cost Anomaly Detector walkthrough

## Business problem

Detects Spark training and feature engineering jobs whose runtime cost or retry behavior is outside expected bounds.

## Reproduce the workflow

Run `python3 spark_cost_anomaly.py sample_jobs.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
daily-feature-build: cost_spike
ranking-training: cost_spike,retry_storm,capacity_hotspot
```

The sample supplies these fields. `job_name`, `team`, `executor_hours`, `cost_usd`, `baseline_cost_usd`, `retries`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
