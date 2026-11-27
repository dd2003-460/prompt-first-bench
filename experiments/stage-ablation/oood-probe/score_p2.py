#!/usr/bin/env python3
"""P2 S0 cyclone arm scorer: objective metric extraction + mechanism coverage.
Reads sm-arm.json + baseline-arm.txt, writes metrics-s0-cyclone.json.
No LLM calls, no git ops.
"""
import json, re, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
SM = os.path.join(BASE, "sm-arm.json")
BL = os.path.join(BASE, "baseline-arm.txt")
OUT = os.path.join(BASE, "metrics-s0-cyclone.json")
LOG = os.path.join(BASE, "sm-arm.log")

MECH_PATTERNS = {
    "energy_source_loss": r"潜热|热通量|能量|蒸发",
    "surface_friction": r"摩擦|粗糙",
    "vertical_wind_shear": r"切变",
    "outflow_blocking": r"辐散|流出|阻塞",
}

# numeric + unit, e.g. "100-200 W/m^2", "6-12 小时", "90%", "50 km", "2 m/s"
UNIT = r"(?:W/m\s*\^?\s*2|W/m²|kt|km/h|km|km/hour|m/s|%|hPa|°C|℃|C\b|小时|天|秒|米|公里|mm|mb|Pa|J/kg|K\b)"
QUANT_RE = re.compile(r"\d+(?:\.\d+)?(?:\s*[-~–—]\s*\d+(?:\.\d+)?)?\s*" + UNIT)


def quant_hits(text):
    """Return list of matched quant phrases (deduped, order-preserving)."""
    seen, out = set(), []
    for m in QUANT_RE.finditer(text):
        s = m.group(0).strip()
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


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


def main():
    d = json.load(open(SM, encoding="utf-8"))
    nodes = d["nodes"]
    base_txt = open(BL, encoding="utf-8").read()

    # ---- SM objective metrics ----
    sm_n_nodes = d.get("n_nodes", len(nodes))
    sm_wall_sec = d.get("wall_sec")
    sm_final_state = d.get("final_state")

    # llm calls: nodes + verify/rework calls in rounds_log; fallback grep log
    rl = d.get("rounds_log", [])
    extra = 0
    if isinstance(rl, list):
        for r in rl:
            rs = json.dumps(r, ensure_ascii=False) if not isinstance(r, str) else r
            extra += len(re.findall(r"verify|rework", rs))
    sm_llm_calls = sm_n_nodes + extra
    sm_llm_calls_method = "nodes + rounds_log verify/rework matches"
    if os.path.exists(LOG):
        logtxt = open(LOG, encoding="utf-8", errors="replace").read()
        n_call_done = len(re.findall(r"call done", logtxt))
        if n_call_done:
            sm_llm_calls = n_call_done
            sm_llm_calls_method = f"grep 'call done' in sm-arm.log = {n_call_done}"

    sm_l1_claims = [
        {"id": n.get("id"), "claim": n.get("claim")}
        for n in nodes if str(n.get("level", "")).upper().startswith("L1")
    ]

    all_claims = " ".join(str(n.get("claim", "")) for n in nodes)
    sm_quant = quant_hits(all_claims)
    sm_levels_dist = {}
    for n in nodes:
        lv = str(n.get("level", "?"))
        sm_levels_dist[lv] = sm_levels_dist.get(lv, 0) + 1

    # mechanism coverage over concatenated SM claims
    sm_mech = mech_hits_in_text(all_claims)
    sm_mech_hit_ids = {}
    for name, pat in MECH_PATTERNS.items():
        ids = sorted({str(n.get("id")) for n in nodes
                      if re.search(pat, str(n.get("claim", "")))})
        sm_mech_hit_ids[name] = ids

    # ---- Baseline ----
    base_chars = len(base_txt)
    base_quant = quant_hits(base_txt)
    base_mech = mech_hits_in_text(base_txt)

    def cov(hits):
        return sum(1 for v in hits.values() if v["hit"])

    metrics = {
        "task": "P2 S0 cyclone arm scoring",
        "qid": d.get("qid"),
        "sm_n_nodes": sm_n_nodes,
        "sm_wall_sec": sm_wall_sec,
        "sm_final_state": sm_final_state,
        "sm_llm_calls": sm_llm_calls,
        "sm_llm_calls_method": sm_llm_calls_method,
        "sm_levels_dist": sm_levels_dist,
        "sm_l1_claims": sm_l1_claims,
        "sm_quant_claims": len(sm_quant),
        "sm_quant_examples": sm_quant[:10],
        "sm_mechanism_hits": sm_mech,
        "sm_mechanism_hit_ids": sm_mech_hit_ids,
        "sm_mech_cov": f"{cov(sm_mech)}/4",
        "base_chars": base_chars,
        "base_quant_claims": len(base_quant),
        "base_quant_examples": base_quant[:10],
        "base_mechanism_hits": base_mech,
        "base_mech_cov": f"{cov(base_mech)}/4",
    }

    json.dump(metrics, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    # ---- console summary (kept short) ----
    print("wrote", OUT)
    print("sm_mech_cov", metrics["sm_mech_cov"],
          {k: v["hit"] for k, v in sm_mech.items()},
          "ids:", sm_mech_hit_ids)
    print("base_mech_cov", metrics["base_mech_cov"],
          {k: v["hit"] for k, v in base_mech.items()})
    print("sm_quant", len(sm_quant), "base_quant", len(base_quant))
    print("sm_l1_claims", len(sm_l1_claims))
    for c in sm_l1_claims:
        print("  L1", c["id"], "|", str(c["claim"])[:110])
    print("sm_llm_calls", sm_llm_calls, "(", sm_llm_calls_method, ")")
    print("sm_wall_sec", sm_wall_sec, "final_state", sm_final_state,
          "levels", sm_levels_dist)


if __name__ == "__main__":
    main()
