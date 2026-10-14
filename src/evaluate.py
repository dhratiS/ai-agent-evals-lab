import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def grade_run(run, task):
    refunds = run["refund_records"]

    if len(refunds) != 1:
        return {
            "passed": False,
            "reason": "Expected exactly one refund record."
        }

    refund = refunds[0]

    if refund["order_id"] != task["order_id"]:
        return {
            "passed": False,
            "reason": "Refund was created for the wrong order."
        }

    if refund["amount_cents"] != task["expected_amount_cents"]:
        return {
            "passed": False,
            "reason": "Refund amount was incorrect."
        }

    if refund["status"] != "succeeded":
        return {
            "passed": False,
            "reason": "Refund did not succeed."
        }

    return {
        "passed": True,
        "reason": "Exactly one correct refund succeeded."
    }


def main():
    input_path = PROJECT_ROOT / "data" / "day01_runs.json"

    with input_path.open(encoding="utf-8") as file:
        dataset = json.load(file)

    results = []

    for run in dataset["runs"]:
        grade = grade_run(run, dataset["task"])

        result = {
            "run_id": run["run_id"],
            **grade
        }

        results.append(result)

        label = "PASS" if grade["passed"] else "FAIL"
        print(f"Run {run['run_id']}: {label} - {grade['reason']}")

    passed_count = sum(1 for result in results if result["passed"])
    success_rate = passed_count / len(results) * 100

    report = {
        "total_runs": len(results),
        "passed_runs": passed_count,
        "task_success_rate_percent": round(success_rate, 1),
        "results": results
    }

    output_path = PROJECT_ROOT / "results" / "day01_results.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    print(f"\nTask success rate: {success_rate:.1f}%")


if __name__ == "__main__":
    main()