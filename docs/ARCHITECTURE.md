# Spark Job Cost Anomaly Detector architecture

Detects Spark training and feature engineering jobs whose runtime cost or retry behavior is outside expected bounds.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
