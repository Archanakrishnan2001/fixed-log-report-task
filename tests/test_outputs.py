import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load_report():
    assert REPORT.exists(), "no report.json found at /app/report.json"
    with open(REPORT) as f:
        return json.load(f)


def test_report_is_valid_json():
    """Criterion 1: /app/report.json exists and contains valid JSON."""
    _load_report()


def test_total_requests():
    """Criterion 2: total_requests equals the total number of lines in access.log."""
    data = _load_report()
    assert data.get("total_requests") == 6


def test_unique_ips():
    """Criterion 3: unique_ips equals the number of distinct IP addresses in access.log."""
    data = _load_report()
    assert data.get("unique_ips") == 3


def test_top_path():
    """Criterion 4: top_path equals the most frequently requested path in access.log."""
    data = _load_report()
    assert data.get("top_path") == "/index.html"
