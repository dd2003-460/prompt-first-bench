#!/usr/bin/env python3
"""K4a 2x2 六臂机械记分: 指标抽取 + 气象4机制 + 硬件37unit LLM批判.
Phase A (机械, 无LLM): 6臂指标 + 气象 mech_hits/mech_cov/mech_review.
Phase B (LLM, 12次, temperature=0): 硬件 37units x 3臂, 4批(10/10/10/7), 带缓存可重入.
输出: metrics-2x2.json. 不做 transfer/handcrafted 判决 (K4b=Lead).
"""
import json, os, re, sys, time
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
AB = os.path.dirname(BASE)
sys.path.insert(0, AB)  # ablation_harness

GOLD = "/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/B-pipeline-ablation/data/gold-q9-units.json"
OUT = os.path.join(BASE, "metrics-2x2.json")
CACHE_DIR = os.path.join(BASE, ".k4a-llm-cache")

# ---------------- 机械指标层 (S1) ----------------
# 数值=[0-9]+(\.[0-9]+)? + 单位 (任务卡单位表, 长单位优先, 单字母单位加负向前瞻防英文词误配)
UNIT_ALT = (r"W/m\s*\^?\s*2|tok/s|km/h|hPa|°C|℃|MW|GW|GB|MB|TB|ms|kt|/h|/s|"
            r"亿|万|节点|层|倍|%|\$|W(?![A-Za-z0-9])|s(?![A-Za-z0-9])|h(?![A-Za-z0-9])|x(?![A-Za-z0-9])")
QUANT_RE = re.compile(r"\d+(?:\.\d+)?\s*(?:" + UNIT_ALT + ")")

# 气象 4 机制 (与 P2 同口径)
MECH_PATTERNS = {
    "energy_source_loss": r"潜热|热通量|能量|蒸发",
    "surface_friction": r"摩擦|粗糙",
    "vertical_wind_shear": r"切变",
    "outflow_blocking": r"辐散|流出|阻塞",
}
# 同义词人工复核位的机械扫描表 (只提示, 不改判)
MECH_REVIEW_SYNONYMS = {
    "energy_source_loss": r"热源|热能|水汽|凝结释放|供热|潜热输送",
    "surface_friction": r"拖曳|阻力|粗糙度|地表耗散",
    "vertical_wind_shear": r"垂直梯度|风向随高度|高层急流",
    "outflow_blocking": r"下沉|低空急流|阻塞高压|外流",
}

ARMS = {
    "S0_weather": {"kind": "sm", "json": "sm-arm.json", "log": "sm-arm.log"},
    "S1_weather": {"kind": "sm", "json": "s1-sm-arm.json", "log": "s1-sm-arm.log"},
    "B_weather":  {"kind": "b", "txt": "baseline-arm.txt"},
    "S0_hw":      {"kind": "sm", "json": "k3-s0-hw.json", "log_seg": ("[S0] SM=", "[S1] SM=")},
    "S1_hw":      {"kind": "sm", "json": "k3-s1-hw.json", "log_seg": ("[S1] SM=", None)},
    "B_hw":       {"kind": "b", "txt": "k3-baseline-hw.txt", "meta": "k3-baseline-hw.json"},
}


def quant_count(text):
    return len(QUANT_RE.findall(text))


def mech_hits_in_text(text):
    hits = {}
    for name, pat in MECH_PATTERNS.items():
        ms = list(re.finditer(pat, text))
        frag = ""
        if ms:
            m0 = ms[0]
            a, b = max(0, m0.start() - 25), min(len(text), m0.end() + 25)
            frag = text[a:b].replace("\n", " ")
        hits[name] = {"hit": bool(ms), "n_matches": len(ms), "fragment": frag}
    return hits


def mech_review_entry(arm_claims, name):
    """claims: [(id, text)] 或 [(None, fulltext)]; 机械扫同义词表, 只提示不改判."""
    pat = MECH_REVIEW_SYNONYMS[name]
    found, ids = [], set()
    for nid, txt in arm_claims:
        ms = list(re.finditer(pat, txt))
        if ms:
            found.extend(sorted({m.group(0) for m in ms}))
            ids.add(str(nid))
    if found:
        return f"疑似同义表述: {sorted(set(found))} (claim id: {sorted(ids)}) — 未改判, 待人工复核"
    return "无关键词命中, 机械同义词扫描亦未见疑似表述 — 待人工复核"


def log_calls_by_segment(logfile, seg_start_marker, seg_end_marker):
    """k3-hw3.log 按臂段切分: [seg_start_marker, seg_end_marker) 内 grep 'call done'."""
    lines = open(logfile, encoding="utf-8", errors="replace").readlines()
    i0 = next((i for i, l in enumerate(lines) if l.startswith(seg_start_marker)), 0)
    i1 = len(lines)
    if seg_end_marker:
        i1 = next((i for i, l in enumerate(lines) if l.startswith(seg_end_marker)), len(lines))
    return sum(1 for l in lines[i0:i1] if "call done" in l)


def arm_metrics(spec):
    m = {"file": spec["json"] if spec["kind"] == "sm" else spec["txt"]}
    if spec["kind"] == "sm":
        d = json.load(open(os.path.join(BASE, spec["json"]), encoding="utf-8"))
        nodes = d["nodes"]
        m.update({
            "n_nodes": d.get("n_nodes", len(nodes)),
            "wall_sec": d.get("wall_sec"),
            "final_state": d.get("final_state"),
            "status_dist": {s: sum(1 for n in nodes if n.get("status") == s)
                            for s in ("verified", "degraded", "pending")},
            "l1_claims": [{"id": n.get("id"), "claim": n.get("claim")}
                          for n in nodes if str(n.get("level", "")).upper().startswith("L1")],
        })
        claims_text = " ".join(str(n.get("claim", "")) for n in nodes)
        m["quant_claims"] = quant_count(claims_text)
        if "log" in spec:
            m["llm_calls"] = sum(1 for l in open(os.path.join(BASE, spec["log"]),
                                                 encoding="utf-8", errors="replace")
                                 if "call done" in l)
            m["llm_calls_method"] = f"grep 'call done' in {spec['log']}"
        else:
            s0, s1 = spec["log_seg"]
            m["llm_calls"] = log_calls_by_segment(os.path.join(BASE, "k3-hw3.log"), s0, s1)
            m["llm_calls_method"] = f"grep 'call done' in k3-hw3.log 段 [{s0}..{s1 or 'EOF'})"
        m["_claims_text"] = claims_text
        m["_claims_pairs"] = [(n.get("id"), str(n.get("claim", ""))) for n in nodes]
    else:
        txt = open(os.path.join(BASE, spec["txt"]), encoding="utf-8").read()
        m.update({"chars": len(txt), "quant_claims": quant_count(txt), "llm_calls": 1,
                  "llm_calls_method": "B臂=1 (任务卡定义)"})
        if spec.get("meta"):
            meta = json.load(open(os.path.join(BASE, spec["meta"]), encoding="utf-8"))
            m["wall_sec"] = meta[0]["sec"] if meta else None
        else:
            m["wall_sec"] = None
        m["_claims_text"] = txt
        m["_claims_pairs"] = [(None, txt)]
    return m


# ---------------- S3 硬件 gold unit 批判 (LLM) ----------------
PROMPT_TMPL = ("你是判分员。下面是一道题的 gold 要点清单(10条)和一个候选答案(40个事实节点拼接)。"
               "逐条判断候选答案是否实质覆盖该要点(覆盖=1, 未覆盖或答错=0, 部分覆盖=0 并在 reason 说明)。"
               "输出 JSON: {\"scores\":[0/1...], \"reasons\":[每条≤20字...]}。"
               "要点清单: {units}。候选答案: {claims_concat}。")


def parse_judge(raw, n_expected):
    t = raw.strip()
    t = re.sub(r"^```(?:json)?\s*", "", t)
    t = re.sub(r"\s*```$", "", t)
    a, b = t.find("{"), t.rfind("}")
    if a < 0 or b <= a:
        raise ValueError("no JSON object in response")
    d = json.loads(t[a:b + 1])
    scores, reasons = d.get("scores"), d.get("reasons")
    if not isinstance(scores, list) or len(scores) != n_expected:
        raise ValueError(f"scores len {len(scores) if isinstance(scores, list) else scores} != {n_expected}")
    scores = [int(s) for s in scores]
    reasons = [str(r)[:40] for r in (reasons or [""] * n_expected)]
    reasons = (reasons + [""] * n_expected)[:n_expected]
    return scores, reasons


def run_llm_phase(arms, units):
    from ablation_harness import call_llm
    os.makedirs(CACHE_DIR, exist_ok=True)
    batches = [units[i:i + 10] for i in range(0, len(units), 10)]
    results, parse_errors, n_calls = {}, [], 0
    for arm, m in arms.items():
        if arm.endswith("_weather"):
            continue
        cand = m["_claims_text"][:30000]
        scores_all, reasons_all = {}, {}
        for bi, batch in enumerate(batches):
            units_str = "\n".join(f"{i+1}. {u['text'][:200]}" for i, u in enumerate(batch))
            prompt = PROMPT_TMPL.replace("{units}", units_str).replace("{claims_concat}", cand)
            cache_f = os.path.join(CACHE_DIR, f"{arm}_b{bi}.json")
            parsed = None
            if os.path.exists(cache_f):
                c = json.load(open(cache_f, encoding="utf-8"))
                if c.get("ok"):
                    parsed = (c["scores"], c["reasons"])
            if parsed is None:
                raw = None
                for attempt in (1, 2):  # 解析失败重试1次
                    raw, _ = call_llm(prompt, max_tokens=2048, temperature=0)
                    n_calls += 1
                    try:
                        parsed = parse_judge(raw, len(batch))
                        break
                    except Exception as e:
                        if attempt == 2:
                            parse_errors.append({"arm": arm, "batch": bi,
                                                 "err": str(e)[:120], "raw_head": (raw or "")[:200]})
                json.dump({"ok": parsed is not None,
                           "scores": parsed[0] if parsed else None,
                           "reasons": parsed[1] if parsed else None,
                           "raw": raw}, open(cache_f, "w", encoding="utf-8"), ensure_ascii=False)
            if parsed:
                for j, u in enumerate(batch):
                    scores_all[u["unit_id"]] = parsed[0][j]
                    reasons_all[u["unit_id"]] = parsed[1][j]
        results[arm] = {"scores": scores_all, "reasons": reasons_all}
    return results, parse_errors, n_calls, [len(b) for b in batches]


def cov_block(scores, unit_ids):
    ids = [u for u in unit_ids if u in scores]
    covered = sum(1 for u in ids if scores[u] == 1)
    return {"covered": f"{covered}/{len(unit_ids)}", "coverage": round(covered / len(unit_ids), 4)
            if unit_ids else None, "n_scored": len(ids)}


def main():
    anomalies = []
    units = json.load(open(GOLD, encoding="utf-8"))["units"]
    assert len(units) == 37, f"gold units != 37: {len(units)}"
    gate_ids = [u["unit_id"] for u in units if u.get("gate")]
    all_ids = [u["unit_id"] for u in units]

    # ---- S1+S2: 机械层 ----
    arms = {name: arm_metrics(spec) for name, spec in ARMS.items()}
    for name, m in arms.items():
        if m.get("wall_sec") is None:
            anomalies.append(f"{name}: wall_sec 未记录 (B气象臂无元数据)")

    mech_hits, mech_review = {}, {}
    for arm in ("S0_weather", "S1_weather", "B_weather"):
        m = arms[arm]
        hits = mech_hits_in_text(m["_claims_text"])
        mech_hits[arm] = hits
        mech_review[arm] = {}
        for name, h in hits.items():
            if not h["hit"]:
                mech_review[arm][name] = mech_review_entry(m["_claims_pairs"], name)
    mech_cov = {a: f"{sum(1 for v in h.values() if v['hit'])}/4" for a, h in mech_hits.items()}

    # ---- S3: LLM 批判 ----
    llm_results, parse_errors, n_calls, batch_sizes = run_llm_phase(arms, units)
    unit_cov, gate_cov = {}, {}
    for arm, r in llm_results.items():
        unit_cov[arm] = dict(cov_block(r["scores"], all_ids), unit_scores=r["scores"], reasons=r["reasons"])
        gate_cov[arm] = cov_block(r["scores"], gate_ids)

    # ---- S4: 落盘 ----
    p2 = json.load(open(os.path.join(BASE, "metrics-s0-cyclone.json"), encoding="utf-8"))
    metrics = {
        "task": "K4a 2x2 六臂机械记分 (指标+气象4机制+硬件37unit批判)",
        "generated_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "arms": {a: {k: v for k, v in m.items() if not k.startswith("_")} for a, m in arms.items()},
        "weather_mech": {
            "patterns": MECH_PATTERNS,
            "mech_hits": mech_hits,
            "mech_cov": mech_cov,
            "mech_review": mech_review,
            "note": "mech_review 仅对 hit=false 项填写; 机械同义词扫描提示, 不改判",
        },
        "hardware_unit_cov": {
            "n_units": len(units), "n_gate": len(gate_ids),
            "gate_unit_ids": gate_ids,
            "batch_sizes": batch_sizes,
            "llm_calls_made": n_calls,
            "llm_model": "qwen3.8-27b@8787 temperature=0",
            "unit_cov": unit_cov,
            "gate_cov": gate_cov,
            "parse_errors": parse_errors,
        },
        "p2_reuse": p2,
        "anomalies": anomalies,
    }
    json.dump(metrics, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    # ---- 控制台摘要 (短) ----
    print("wrote", OUT)
    for a in ("S0_weather", "S1_weather", "B_weather"):
        m = arms[a]
        print(a, "mech_cov", mech_cov[a], "quant", m["quant_claims"],
              "llm_calls", m["llm_calls"],
              "n_nodes" if m.get("n_nodes") is not None else "chars",
              m.get("n_nodes", m.get("chars")))
    for a in ("S0_hw", "S1_hw", "B_hw"):
        m = arms[a]
        print(a, "unit_cov", unit_cov.get(a, {}).get("covered"),
              "gate_cov", gate_cov.get(a, {}).get("covered"),
              "quant", m["quant_claims"], "llm_calls", m["llm_calls"],
              "n_nodes" if m.get("n_nodes") is not None else "chars",
              m.get("n_nodes", m.get("chars")))
    print("llm_calls_made", n_calls, "parse_errors", len(parse_errors))
    for e in parse_errors:
        print("  PARSE_ERR", e["arm"], "batch", e["batch"], e["err"])
    for a in anomalies:
        print("ANOMALY:", a)


if __name__ == "__main__":
    main()
