# Spark Job Cost Anomaly Detector

A Spark workload can finish successfully while a retry storm or resource spike drives cost above its baseline.

## What I built

I built a Spark cost review tool that checks cost against baseline, retry count, and executor hours. Its report lists each anomalous job with the reasons operators can investigate.

## How it works

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

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [spark_cost_anomaly.py](spark_cost_anomaly.py) implements the CLI and decision rules. Uses `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 spark_cost_anomaly.py sample_jobs.csv
```

The feature build shows a cost spike. Ranking training also shows a retry storm and capacity hotspot. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 spark_cost_anomaly.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

The thresholds work on exported summaries. Use job timelines and executor metrics to identify the cause before tuning a cluster.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
