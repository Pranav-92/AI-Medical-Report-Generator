import re

LAB_PATTERN = re.compile(
    r"""
    (?P<test>[A-Za-z0-9 ()/%\-.,]+?)\s+
    (?P<value>\d+\.?\d*)\s*
    (?P<unit>[a-zA-Zµ/%³×]*)\s+
    (?P<range>[<>\d.\-–]+)
    """,
    re.VERBOSE
)

def parse_lab_line(line):
    match = LAB_PATTERN.search(line)
    if not match:
        return None

    return {
        "test": match.group("test").strip(),
        "value": float(match.group("value")),
        "unit": match.group("unit"),
        "reference": match.group("range")
    }
