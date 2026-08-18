import sys
import unittest
from pathlib import Path


project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "src"))

from main import normalize_alert, validate_alert


class TestAlertFunctions(unittest.TestCase):
    def test_valid_alert_does_not_raise_error(self):
        alert = {
            "timestamp": "2026-08-17T14:32:10Z",
            "event": "Successful login",
            "severity": "high",
        }

        validate_alert(alert)

    def test_missing_required_field_raises_value_error(self):
        alert = {
            "timestamp": "2026-08-17T14:32:10Z",
            "severity": "high",
        }

        with self.assertRaises(ValueError):
            validate_alert(alert)

    def test_invalid_severity_raises_value_error(self):
        alert = {
            "timestamp": "2026-08-17T14:32:10Z",
            "event": "Successful login",
            "severity": "urgent",
        }

        with self.assertRaises(ValueError):
            validate_alert(alert)

    def test_normalize_alert_cleans_and_completes_fields(self):
        alert = {
            "timestamp": " 2026-08-17T14:32:10Z ",
            "event": " Successful login ",
            "severity": " HIGH ",
        }

        normalized_alert = normalize_alert(alert)

        self.assertEqual(normalized_alert["timestamp"], "2026-08-17T14:32:10Z")
        self.assertEqual(normalized_alert["event"], "Successful login")
        self.assertEqual(normalized_alert["severity"], "high")
        self.assertIsNone(normalized_alert["source_ip"])


if __name__ == "__main__":
    unittest.main()
