from services.lab_line_parser import parse_lab_line
from services.normal_range_parser import parse_reference_range

def analyze_report(pages):
    flagged = []

    for page in pages:
        for line in page["lines"]:
            parsed = parse_lab_line(line)
            if not parsed:
                continue

            low, high = parse_reference_range(parsed["reference"])
            value = parsed["value"]

            status = "NORMAL"

            if low is not None and value < low:
                status = "LOW"
            elif high is not None and value > high:
                status = "HIGH"

            if status != "NORMAL":
                flagged.append({
                    "test_name": parsed["test"],
                    "value": f"{value} {parsed['value']}",
                    "reference_range": parsed["reference"],
                    "status": status,
                    "page_no": page["page_no"]
                })

    return flagged
