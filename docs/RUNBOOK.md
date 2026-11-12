# Spark Job Cost Anomaly Detector runbook

## What the project does

A Spark workload can finish successfully while a retry storm or resource spike drives cost above its baseline.

See the [architecture and data flow](ARCHITECTURE.md) and [project case study](CASE_STUDY.md).

## Run from a clean checkout

Use Python 3 and Make. Install the pinned developer tools in a local environment.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

Run a bundled scenario from the repository root.

```sh
python3 spark_cost_anomaly.py sample_jobs.csv
```

## Expected result

- Demo 1. `2 lines of output. Open the baseline for the full result.` [Baseline](../examples/Demo%201.stdout.txt)
- Last sample record in isolation. `(no stdout)` [Baseline](../examples/Last%20sample%20record%20in%20isolation.stdout.txt)

Run `make replay` to compare results with the baselines and regenerate the [replay report](../reports/replay.md).
The [rules page](RULES.md) links to the code behind the decision.

## Verify a change

Run `make check PYTHON=python` inside the virtual environment. This runs the application checks, Ruff lint, and the Bandit static gate.
The [development guide](DEVELOPMENT.md) explains the tools and the [local report](../reports/devsecops.md) records what passed.

## If a check fails

Run the first failing command on its own. For a replay mismatch, inspect the diff and compare the input, rule, and expected output before updating the baseline.
For a lint or Bandit finding, review the reported source line and rerun the relevant target.

## Golden note

Use the reason codes to separate cost changes, retry bursts, and executor-hour hotspots before contacting the listed team.

## Operating limits

Use the [case study](CASE_STUDY.md) to check assumptions before applying a result to a live environment.
