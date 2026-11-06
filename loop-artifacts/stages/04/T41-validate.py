#!/usr/bin/env python3
"""Deterministic structural/arithmetic self-check; this is NOT an independent review.

Run from any directory with: python loop-artifacts/stages/04/T41-validate.py
This checks the report's declared inputs and examples, not external URLs, real
prices, measured performance, actual provider availability, or SOP approval.
"""
from decimal import Decimal
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
D = Decimal


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def check_report(filename, expected_nodes, expected_leaves):
    text = (HERE / filename).read_text(encoding="utf-8")
    blocks = re.findall(r"```text\n(.*?)\n```", text, flags=re.S)
    trees = [block for block in blocks if block.startswith("ROOT ")]
    require(len(trees) == 1, f"{filename}: expected exactly one ROOT tree")
    lines = trees[0].splitlines()
    children = {"ROOT": []}
    depth_by_id = {"ROOT": 0}
    stack = ["ROOT"]
    for line in lines[1:]:
        match = re.fullmatch(r"((?:\|   |    )*)(?:\|-- |`-- )([A-Z]\d+)\s+.+", line)
        require(match is not None, f"{filename}: invalid tree line: {line}")
        prefix, node_id = match.groups()
        depth = len(prefix) // 4 + 1
        require(node_id not in children, f"{filename}: duplicate tree node {node_id}")
        require(depth <= len(stack), f"{filename}: missing parent for {node_id}")
        stack = stack[:depth]
        parent = stack[depth - 1]
        children[parent].append(node_id)
        children[node_id] = []
        depth_by_id[node_id] = depth
        stack.append(node_id)

    leaves = {key for key, value in children.items() if not value}
    require(len(children) == expected_nodes, f"{filename}: got {len(children)} nodes")
    require(len(leaves) == expected_leaves, f"{filename}: got {len(leaves)} leaves")
    require(3 <= len(children["ROOT"]) <= 5, f"{filename}: expected 3–5 dimensions")
    require(max(depth_by_id.values()) >= 3, f"{filename}: depth < 3")
    require(all(re.fullmatch(r"L\d{2}", leaf) for leaf in leaves),
            f"{filename}: terminal node without leaf ID")

    sources = set(re.findall(r"^-\s+(S\d+)\b[^\n]*\[\d+\]\(https?://[^\s)]+\)",
                             text, flags=re.M))
    require(sources, f"{filename}: no linked source index")
    rows = {}
    for line in text.splitlines():
        if re.match(r"^\| L\d{2} \|", line):
            fields = [field.strip() for field in line.strip().strip("|").split("|")]
            require(len(fields) == 4, f"{filename}: expected 4 columns in {line}")
            leaf, value, source, sensitivity = fields
            require(leaf not in rows, f"{filename}: duplicate leaf row {leaf}")
            require(re.search(r"\d", value), f"{filename}: {leaf} lacks numeric value")
            refs = set(re.findall(r"\bS\d+\b", source))
            require(refs and refs <= sources, f"{filename}: {leaf} has missing source {refs - sources}")
            require(len(sensitivity) >= 8, f"{filename}: {leaf} lacks sensitivity")
            rows[leaf] = value
    require(set(rows) == leaves, f"{filename}: leaf rows != tree leaves: {set(rows) ^ leaves}")
    for heading in ("交叉验证表", "缺口", "结论"):
        require(heading in text, f"{filename}: missing {heading}")
    print(f"{filename}: {len(children)} nodes, {len(children['ROOT'])} dimensions, "
          f"depth {max(depth_by_id.values())}, {len(leaves)} sourced leaf rows")
    return text, rows


def contains(rows, node, value):
    require(value in rows[node], f"{node}: expected {value!r} in {rows[node]!r}")


def close(actual, expected, tolerance="0.000001"):
    require(abs(actual - D(expected)) <= D(tolerance), f"{actual} != {expected}")


def main():
    q1, gpu = check_report("Q1-execution-log.md", 31, 18)
    q3, api = check_report("Q3-execution-log.md", 35, 21)
    for node, value in {"L04": "3.35", "L05": "2.00", "L13": "3.99",
                        "L14": "2.89", "L17": "1.00", "L18": "1.00"}.items():
        contains(gpu, node, value)
    for node, value in {"L01": "100M", "L02": "50%", "L03": "0.15",
                        "L04": "0.15", "L05": "0.15", "L06": "0.075",
                        "L07": "0.15", "L08": "0.015", "L10": "20M",
                        "L11": "0.60", "L12": "0.60", "L13": "0.60"}.items():
        contains(api, node, value)

    bw_s, bw_p, weights = D(3350), D(2000), D(16)  # GB/s, GB/token
    rate_s, rate_p = D("3.99"), D("2.89")          # USD/GPU-hour
    ts, tp = bw_s / weights, bw_p / weights
    cost = lambda rate, throughput: D(1_000_000) * rate / (D(3600) * throughput)
    close(ts, "209.375")
    close(tp, "125")
    close(cost(rate_s, ts), "5.293532338308458")
    close(cost(rate_p, tp), "6.422222222222222")
    close(rate_s / rate_p, "1.3806228373702423")
    close((rate_s / rate_p) / (ts / tp), "0.8242524402210402")
    close(cost(rate_s, ts * D("0.6")), "8.822553897180763")
    close(cost(rate_p, tp * D("0.8")), "8.027777777777778")
    require(all(s in q1 for s in ("$5.294", "$6.422", "1.38062", "0.82425", "$8.823", "$8.028")),
            "Q1 displayed figures missing")

    # Inputs/outputs in millions of tokens; Together cached price is tied to input.
    def bill(input_m, output_m, hit, p_cache):
        return input_m * ((D(1) - hit) * D("0.15") + hit * p_cache) + output_m * D("0.60")

    half, zero = D("0.5"), D(0)
    for p_cache in (D("0.015"), D("0.075"), D("0.15")):
        close(bill(D(100), D(20), zero, p_cache), "27")
    close(bill(D(100), D(20), half, D("0.015")), "20.25")
    close(bill(D(100), D(20), half, D("0.075")), "23.25")
    close(bill(D(100), D(20), half, D("0.15")), "27")
    close(bill(D(100), D(20), D("0.1"), D("0.015")), "25.65")
    require(all(s in q3 for s in ("$27.00", "$20.25", "$23.25", "$25.65", "(5/9)")),
            "Q3 displayed figures missing")
    print("Arithmetic: documented ideal costs, thresholds, cache scenarios and reversal match")
    print("Limitations: no network verification, actual benchmarks, or independent Reviewer approval")


if __name__ == "__main__":
    main()
