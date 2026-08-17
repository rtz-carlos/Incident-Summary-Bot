import json
from pathlib import Path


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
    alert_path = project_root / "data" / "sample_alert.json"

    try:
        with alert_path.open("r", encoding="utf-8") as alert_file:
            alert = json.load(alert_file)
    except FileNotFoundError:
        print(f"Error: file not found: {alert_path}")
        return
    except json.JSONDecodeError as error:
        print(f"Error: invalid JSON in {alert_path}: {error}")
        return

    normalized_alert = normalize_alert(alert)

    print("Alert loaded successfully")
    print("Normalized alert:")
    print(json.dumps(normalized_alert, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
