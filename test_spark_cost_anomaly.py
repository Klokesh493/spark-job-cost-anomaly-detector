import unittest

from spark_cost_anomaly import anomalous_jobs, anomaly_reasons


class SparkCostAnomalyTest(unittest.TestCase):
    def test_detects_cost_retry_and_capacity_risk(self):
        row = {"cost_usd": "1800", "baseline_cost_usd": "1100", "retries": "4", "executor_hours": "900"}
        self.assertEqual(anomaly_reasons(row), ["cost_spike", "retry_storm", "capacity_hotspot"])

    def test_filters_healthy_jobs(self):
        rows = [
            {"job_name": "ok", "team": "a", "cost_usd": "90", "baseline_cost_usd": "100", "retries": "0", "executor_hours": "10"},
            {"job_name": "bad", "team": "b", "cost_usd": "180", "baseline_cost_usd": "100", "retries": "0", "executor_hours": "10"},
        ]
        self.assertEqual([job["job_name"] for job in anomalous_jobs(rows)], ["bad"])


if __name__ == "__main__":
    unittest.main()
