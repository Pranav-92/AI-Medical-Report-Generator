import re
from utils.range_utils import parse_range, evaluate_value

def analyze_lines(lines):
    results = []

    for item in lines:
        line = item["text"]
        page_no = item["page_no"]

        # Test name = text before first number
        name_match = re.match(r"([A-Za-z /()\-]+)", line)
        if not name_match:
            continue

        test_name = name_match.group(1).strip()

        # Value (first number only)
        value_match = re.search(r"(\d+\.?\d*)", line)
        range_match = re.search(r"(\d+\.?\d*)\s*[-–]\s*(\d+\.?\d*)", line)

        if not value_match or not range_match:
            continue

        value = float(value_match.group(1))
        range_text = f"{range_match.group(1)}-{range_match.group(2)}"

        low, high = parse_range(range_text)
        if low is None:
            continue

        status = evaluate_value(value, low, high)
        if status == "NORMAL":
            continue

        results.append({
            "test": test_name,
            "value": value,
            "normal_range": range_text,
            "status": status,
            "page_no": page_no
        })

    return results
