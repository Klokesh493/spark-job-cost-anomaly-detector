# Spark Job Cost Anomaly Detector architecture

Detects Spark training and feature engineering jobs whose runtime cost or retry behavior is outside expected bounds.

```mermaid
flowchart LR
    N0["sample_jobs.csv"]
    N1["spark_cost_anomaly.py"]
    N2["cost ratio / anomaly reasons / anomalous jobs"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
