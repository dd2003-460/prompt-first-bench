#!/usr/bin/env python3
"""M2a variance probe: per-arm per-rep metric stats + power-risk verdict.
Zero-GPU, read-only over checkpoints. Writes m2a-variance-probe.json (overwrite).
Spec: modules/G-think-mechanism/think-trigger/taskcard-m2a-variance-probe.md
"""
import json
import math
import os
import re

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "checkpoints")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "m2a-variance-probe.json")

ARMS = {
    "cyclone_s0": ["sm-oood-cyclone-r1", "sm-oood-cyclone-r2"],
    "cyclone_s1": ["sm-oood-s1-cyclone-r1", "sm-oood-s1-cyclone-r2"],
    "hw_s0": ["sm-k3-S0-r1", "sm-k3-S0-r2"],
    "hw_s1": ["sm-k3-S1-r1"],
}

CYCLONE_IN = ["衰减", "风眼", "眼壁", "角动量", "潜热", "边界层摩擦", "洋热通量"]
CYCLONE_OUT = ["非凸", "landscape", "梯度下降", "损失面", "相变", "李雅普诺夫"]
HW_IN = ["功耗", "延迟", "带宽", "缓存", "流水线", "时钟", "总线"]
HW_OUT = ["非凸", "landscape", "梯度下降", "损失面", "相变"]

QUANT_RE = re.compile(r"[0-9]|[=\u2265\u2264\u00f7\u00d7%℃]|km|hPa|knot|节")
MECH_PARAM = re.compile(r"变化|改变|增大|减小|升高|降低|中断|切断|增强|减弱")
MECH_CAUSE = re.compile(r"导致|引起|使得|造成|因为|由于|从而|进而")
MECH_QTY = re.compile(r"数量级|量级|约|典型|平均|速率|强度|占比|百分比")


def extract_claims(node_md_path):
    """Return claim text (## Claim section) or None."""
    try:
        with open(node_md_path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return None
    m = re.search(r"^## Claim\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return None
    return m.group(1).strip()


def iter_node_md(ckpt_dir):
    for root, _dirs, files in os.walk(ckpt_dir):
        if "node.md" in files:
            yield os.path.join(root, "node.md")


def metrics_for_rep(ckpt_dir, domain_in, domain_out):
    n_nodes = 0
    quant_hits = 0
    in_hits = 0
    out_hits = 0
    mech_hits = 0
    parse_errors = []
    for path in sorted(iter_node_md(ckpt_dir)):
        claim = extract_claims(path)
        if claim is None:
            parse_errors.append(path)
            continue
        n_nodes += 1
        if QUANT_RE.search(claim):
            quant_hits += 1
        in_hits += sum(claim.count(w) for w in domain_in)
        out_hits += sum(claim.lower().count(w.lower()) if w.isascii() else claim.count(w)
                        for w in domain_out)
        n_factors = sum(bool(r.search(claim)) for r in (MECH_PARAM, MECH_CAUSE, MECH_QTY))
        if n_factors >= 2:
            mech_hits += 1
    if n_nodes == 0:
        return None
    return {
        "n_nodes": n_nodes,
        "quant_density": quant_hits / n_nodes,
        "domain_drift_rate": out_hits / max(in_hits, 1),
        "mech_coverage": mech_hits / n_nodes,
        "parse_errors": parse_errors,
    }


def stats(values):
    n = len(values)
    mean = sum(values) / n
    if n < 2:
        return {"values": values, "mean": mean, "sd": None, "cv": None}
    var = sum((v - mean) ** 2 for v in values) / (n - 1)
    sd = math.sqrt(var)
    cv = (sd / mean) if mean != 0 else None
    return {"values": values, "mean": mean, "sd": sd, "cv": cv}


METRICS = ["quant_density", "domain_drift_rate", "mech_coverage"]


def main():
    arms_out = {}
    all_cvs = []  # (arm, metric, cv)
    for arm, ckpts in ARMS.items():
        domain = "cyclone" if arm.startswith("cyclone") else "hw"
        dom_in = CYCLONE_IN if domain == "cyclone" else HW_IN
        dom_out = CYCLONE_OUT if domain == "cyclone" else HW_OUT
        reps = {}
        for ckpt in ckpts:
            rep = ckpt.rsplit("-", 1)[-1]  # r1 / r2
            ckpt_dir = os.path.join(BASE, ckpt)
            if not os.path.isdir(ckpt_dir):
                reps[rep] = {"status": "missing"}
                continue
            m = metrics_for_rep(ckpt_dir, dom_in, dom_out)
            if m is None:
                reps[rep] = {"status": "parse_error", "note": "no parseable node.md claims"}
            else:
                reps[rep] = m
        vals = {mt: [reps[r][mt] for r in reps if isinstance(reps.get(r), dict)
                     and mt in reps[r]] for mt in METRICS}
        mstats = {}
        for mt in METRICS:
            st = stats(vals[mt])
            mstats[mt] = st
            if st["cv"] is not None:
                all_cvs.append((arm, mt, st["cv"]))
        arms_out[arm] = {"reps": reps, "metric_stats": mstats}

    largest = max(all_cvs, key=lambda t: t[2]) if all_cvs else None
    largest_cv = largest[2] if largest else None
    if largest_cv is None:
        risk = "unknown"
    elif largest_cv > 0.3:
        risk = "high"
    elif any(cv >= 0.15 for _, _, cv in all_cvs):
        risk = "medium"
    else:
        risk = "low"

    result = {
        "arms": arms_out,
        "verdict": {
            "cyclone_reps_per_arm": 2,
            "largest_cv": ({"arm": largest[0], "metric": largest[1], "cv": largest[2]}
                           if largest else None),
            "power_risk": risk,
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    parts = []
    for arm in ARMS:
        ms = arms_out[arm]["metric_stats"]
        seg = ", ".join(
            "{}={:.3f}±{}".format(mt, ms[mt]["mean"],
                                  "{:.3f}".format(ms[mt]["sd"]) if ms[mt]["sd"] is not None else "n/a")
            for mt in METRICS)
        parts.append("{}: {}".format(arm, seg))
    lc = result["verdict"]["largest_cv"]
    print("; ".join(parts) + " | power_risk={} (largest cv: {} {}={:.3f})".format(
        risk, lc["arm"] if lc else "-", lc["metric"] if lc else "-",
        lc["cv"] if lc else float("nan")))


if __name__ == "__main__":
    main()
