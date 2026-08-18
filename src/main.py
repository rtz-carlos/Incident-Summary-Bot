import argparse
import json
from pathlib import Path

from openai import OpenAIError

from llm_client import generate_incident_summary


def validate_alert(alert):
    if not isinstance(alert, dict):
        raise TypeError("Alert must be a dictionary")

    required_fields = ("timestamp", "event", "severity")
    for field in required_fields:
        value = alert.get(field)
        if value is None or (isinstance(value, str) and not value.strip()):
            raise ValueError(f"Required field '{field}' is missing or empty")

    severity = alert["severity"]
    if not isinstance(severity, str):
        raise ValueError("Severity must be text")

    allowed_severities = ("low", "medium", "high", "critical")
    if severity.strip().lower() not in allowed_severities:
        raise ValueError(
            "Severity must be one of: low, medium, high, critical"
        )


def normalize_alert(alert):
    if not isinstance(alert, dict):
        raise TypeError("Alert must be a dictionary")

    fields = (
        "timestamp",
        "source_ip",
        "destination_ip",
        "username",
        "hostname",
        "event",
        "action",
        "severity",
        "file_hash",
    )
    normalized_alert = {}

    for field in fields:
        value = alert.get(field)
        if isinstance(value, str):
            value = value.strip()
        if field == "severity" and isinstance(value, str):
            value = value.lower()
        normalized_alert[field] = value

    return normalized_alert


def main():
    project_root = Path(__file__).resolve().parent.parent
    default_alert_path = project_root / "data" / "sample_alert.json"

    parser = argparse.ArgumentParser(description="Load and normalize an alert")
    parser.add_argument(
        "alert_file",
        nargs="?",
        default=default_alert_path,
        type=Path,
        help="path to the alert JSON file",
    )
    args = parser.parse_args()
    alert_path = args.alert_file

    try:
        with alert_path.open("r", encoding="utf-8") as alert_file:
            alert = json.load(alert_file)
    except FileNotFoundError:
        print(f"Error: file not found: {alert_path}")
        return
    except json.JSONDecodeError as error:
        print(f"Error: invalid JSON in {alert_path}: {error}")
        return

    try:
        validate_alert(alert)
        normalized_alert = normalize_alert(alert)
    except (ValueError, TypeError) as error:
        print(f"Error: {error}")
        return

    print("Alert loaded and normalized successfully")
    print("Generating incident summary...")

    try:
        summary = generate_incident_summary(normalized_alert)
    except (ValueError, OpenAIError) as error:
        print(f"Error generating summary: {error}")
        return

    print("Incident summary:")
    print(summary.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
