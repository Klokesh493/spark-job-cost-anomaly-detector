# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 spark_cost_anomaly.py sample_jobs.csv
daily-feature-build: cost_spike
ranking-training: cost_spike,retry_storm,capacity_hotspot
test_detects_cost_retry_and_capacity_risk (test_spark_cost_anomaly.SparkCostAnomalyTest) ... ok
test_filters_healthy_jobs (test_spark_cost_anomaly.SparkCostAnomalyTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
````
