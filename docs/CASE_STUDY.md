# Spark Job Cost Anomaly Detector walkthrough

## Business problem

A Spark workload can finish successfully while a retry storm or resource spike drives cost above its baseline.

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
