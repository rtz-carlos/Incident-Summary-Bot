import json
from pathlib import Path


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

    print("Alert loaded successfully")
    print(json.dumps(alert, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
