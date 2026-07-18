import csv
import sys


def cost_ratio(row):
    baseline = max(float(row["baseline_cost_usd"]), 1.0)
    return float(row["cost_usd"]) / baseline


def anomaly_reasons(row):
    reasons = []
    if cost_ratio(row) >= 1.35:
        reasons.append("cost_spike")
    if int(row["retries"]) >= 3:
        reasons.append("retry_storm")
    if float(row["executor_hours"]) >= 800:
        reasons.append("capacity_hotspot")
    return reasons


def anomalous_jobs(rows):
    return [
        {"job_name": row["job_name"], "team": row["team"], "reasons": anomaly_reasons(row)}
        for row in rows
        if anomaly_reasons(row)
    ]


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for job in anomalous_jobs(csv.DictReader(handle)):
            print(f'{job["job_name"]}: { ",".join(job["reasons"]) }')


if __name__ == "__main__":
    main(sys.argv[1])
