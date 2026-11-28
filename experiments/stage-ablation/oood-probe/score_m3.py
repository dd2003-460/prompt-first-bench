#!/usr/bin/env python3
"""M4 scoring: preregistered mechanical metrics for M3 night batch (11 reps).

Metrics per m2-injection-design-20261128.md §2 (prereg, committed pre-run):
  form  = fraction of nodes with >=2 of the three mechanism elements
          (param_change + causal_explanation + effect_quantity)
  flip  = fraction of nodes whose claim contains a domain-internal mechanism
          word from the preregistered vocabulary (mechanical proxy for
          "domain identity judged correctly")
  align = mean over nodes of (flip_node * form_node)
  dsr   = domain-shift ratio = total out-of-domain word hits / in-domain word
          hits over ALL raw-llm output text of the rep (null if denom == 0)
  quant_density = fraction of nodes containing number/formula/interval
          (diagnostic only, not used for verdict)

Field mapping (actual on-disk schema, verified 2026-11-28):
  - ckpt node text field: `claim` (no content/reasoning fields exist;
    prereg "transcript(content+reasoning)" maps to `content` in raw-llm
    jsonl and `claim` in ckpt nodes)
  - raw-llm line field: `content`
"""
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
CKPT_DIR = BASE / "m3-ckpt"
RAW_DIR = BASE / "raw-llm-calls"
OUT_JSON = BASE / "m3-metrics.json"
OUT_SAMPLE = BASE / "m3-manual-sample.txt"

# ---- preregistered vocabularies (verbatim from m2-injection-design §2, DO NOT EDIT) ----
VOCAB = {
    "cyclone": {
        "in": ["衰减", "风眼", "眼壁", "角动量", "潜热", "边界层摩擦", "洋热通量"],
        "out": ["非凸", "landscape", "梯度下降", "损失面", "相变", "李雅普诺夫"],
    },
    "hw": {
        "in": ["功耗", "延迟", "带宽", "缓存", "流水线", "时钟", "总线"],
        "out": ["非凸", "landscape", "梯度下降", "损失面", "相变"],
    },
    "mining": {
        "in": ["金属", "导电", "电磁感应", "涡流", "地层", "矿体", "电阻率"],
        "out": ["非凸", "landscape", "梯度下降", "损失面", "相变"],
    },
}

# ---- form regex patterns (prereg spec: param change = number OR param word;
#      causal = causal connector; effect = magnitude word) ----
PARAM_WORDS = ["参数", "系数", "阈值", "频率"]
CAUSAL_WORDS = ["因为", "由于", "导致", "引起", "驱动", "源于"]
EFFECT_WORDS = ["量级", "幅度", "±", "%", "倍", "区间"]

RE_PARAM = re.compile(r"\d|" + "|".join(PARAM_WORDS))
RE_CAUSAL = re.compile("|".join(CAUSAL_WORDS))
RE_EFFECT = re.compile("|".join(EFFECT_WORDS))
# quant_density: number / formula operator / interval
RE_QUANT = re.compile(r"\d|[+\-*/=<>±]|区间|约|左右|之间")

REPS = [
    # (arm, domain, rep)
    ("v1", "cyclone", 1),
    ("v1", "cyclone", 2),
    ("v1", "cyclone", 3),
    ("v1", "mining", 1),
    ("v1", "mining", 2),
    ("v1", "mining", 3),
    ("v1", "hw", 1),
    ("v1", "hw", 2),
    ("v1", "hw", 3),
    ("s1", "cyclone", 1),
    ("s1", "cyclone", 2),
]


def node_text(node):
    parts = []
    for k in ("claim", "content", "reasoning"):
        if node.get(k):
            parts.append(str(node[k]))
    return "\n".join(parts)


def form_elements(text):
    """Return (param_hit, causal_hit, effect_hit) booleans."""
    return (bool(RE_PARAM.search(text)),
            bool(RE_CAUSAL.search(text)),
            bool(RE_EFFECT.search(text)))


def score_rep(arm, domain, rep):
    ckpt_path = CKPT_DIR / f"m3-{arm}-{domain}-r{rep}.json"
    raw_path = RAW_DIR / f"m3-{arm}-{domain}-r{rep}.jsonl"
    ckpt = json.loads(ckpt_path.read_text(encoding="utf-8"))
    nodes = ckpt["nodes"]
    n = len(nodes)
    assert n > 0, f"{ckpt_path.name}: no nodes"

    form_num = 0
    flip_num = 0
    align_sum = 0.0
    quant_num = 0
    in_vocab = VOCAB[domain]["in"]
    node_flags = []
    for nd in nodes:
        t = node_text(nd)
        p, c, e = form_elements(t)
        n_el = int(p) + int(c) + int(e)
        form_node = n_el >= 2
        flip_node = any(w in t for w in in_vocab)
        quant_node = bool(RE_QUANT.search(t))
        form_num += int(form_node)
        flip_num += int(flip_node)
        align_sum += (1.0 if flip_node else 0.0) * (1.0 if form_node else 0.0)
        quant_num += int(quant_node)
        node_flags.append((nd.get("id"), n_el, p, c, e, form_node, flip_node, t))

    # dsr over raw-llm output text (field: content)
    in_hits = 0
    out_hits = 0
    n_calls = 0
    with raw_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            txt = rec.get("content", "")
            if not txt:
                continue
            n_calls += 1
            for w in in_vocab:
                in_hits += txt.count(w)
            for w in VOCAB[domain]["out"]:
                out_hits += txt.count(w)
    dsr = None if in_hits == 0 else round(out_hits / in_hits, 4)

    return {
        "file": ckpt_path.name,
        "arm": arm,
        "domain": domain,
        "rep": rep,
        "n_nodes": n,
        "form": round(form_num / n, 4),
        "flip": round(flip_num / n, 4),
        "align": round(align_sum / n, 4),
        "dsr": dsr,
        "dsr_in_hits": in_hits,
        "dsr_out_hits": out_hits,
        "dsr_n_calls": n_calls,
        "quant_density": round(quant_num / n, 4),
        "_node_flags": node_flags,
    }


def main():
    results = []
    for arm, domain, rep in REPS:
        r = score_rep(arm, domain, rep)
        results.append(r)
        print(f"{r['file']}: n={r['n_nodes']} form={r['form']} flip={r['flip']} "
              f"align={r['align']} dsr={r['dsr']} quant={r['quant_density']}")

    # by_arm_domain means
    by_ad = {}
    for key in [(r["arm"], r["domain"]) for r in results]:
        grp = [r for r in results if (r["arm"], r["domain"]) == key]
        if not grp:
            continue
        dsrs = [r["dsr"] for r in grp if r["dsr"] is not None]
        by_ad[f"{key[0]}-{key[1]}"] = {
            "n_reps": len(grp),
            "form_mean": round(sum(r["form"] for r in grp) / len(grp), 4),
            "flip_mean": round(sum(r["flip"] for r in grp) / len(grp), 4),
            "align_mean": round(sum(r["align"] for r in grp) / len(grp), 4),
            "dsr_mean": round(sum(dsrs) / len(dsrs), 4) if dsrs else None,
            "quant_density_mean": round(sum(r["quant_density"] for r in grp) / len(grp), 4),
        }

    notes = [
        "v1-mining-r1: n_nodes=31 (< 40), state-machine rework dynamic, not an error; scored as-is",
        "field mapping: prereg 'transcript(content+reasoning)' -> ckpt node field `claim` (only text field present) + raw-llm field `content`",
        "dsr counted over raw-llm output `content` of all calls per rep (incl. planning/judge calls)",
        "quant_density is diagnostic only (prereg: not part of verdict)",
        "vocabularies verbatim from m2-injection-design-20261128.md §2",
    ]

    out = {
        "reps": [{k: v for k, v in r.items() if k != "_node_flags"} for r in results],
        "by_arm_domain": by_ad,
        "regex_patterns": {
            "param_change": RE_PARAM.pattern,
            "causal_explanation": RE_CAUSAL.pattern,
            "effect_quantity": RE_EFFECT.pattern,
            "quant_density": RE_QUANT.pattern,
            "form_rule": "elements>=2 of {param_change, causal_explanation, effect_quantity}",
        },
        "vocab": VOCAB,
        "notes": notes,
    }
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nwrote {OUT_JSON}")

    # ---- manual sample: 10 nodes, >=1 per arm-domain group, spread by rep ----
    groups = {}
    for r in results:
        g = f"{r['arm']}-{r['domain']}"
        groups.setdefault(g, []).append(r)
    picks = []
    # one node per group first (5 groups), then fill remaining 5 by cycling reps
    order = list(groups.keys())
    gi = 0
    taken_reps = set()
    while len(picks) < 10:
        g = order[gi % len(order)]
        grp = groups[g]
        # pick a rep not yet sampled in this group if possible
        cand = [r for r in grp if (g, r["rep"]) not in taken_reps] or grp
        r = cand[0]
        flags = r["_node_flags"]
        # vary the node index so samples aren't all N1
        idx = len(picks) % len(flags)
        nid, n_el, p, c, e, form_node, flip_node, text = flags[idx]
        picks.append({
            "file": r["file"], "group": g, "node_id": nid,
            "n_elements": n_el,
            "param": p, "causal": c, "effect": e,
            "form_ge2": form_node, "flip": flip_node,
            "text_head": text[:80],
        })
        taken_reps.add((g, r["rep"]))
        gi += 1

    lines = [
        "M4 manual sample: 10 nodes for regex-vs-intuition check (Lead review)",
        "columns: file | node_id | elements(param/causal/effect) | n_el | form(>=2) | flip | text[:80]",
        "=" * 100,
    ]
    for i, p in enumerate(picks, 1):
        lines.append(f"[{i:02d}] {p['file']} {p['node_id']}")
        lines.append(f"     elem: param={int(p['param'])} causal={int(p['causal'])} effect={int(p['effect'])} "
                     f"-> n_el={p['n_elements']} form_ge2={p['form_ge2']} flip={p['flip']}")
        lines.append(f"     text: {p['text_head']}")
        lines.append("")
    OUT_SAMPLE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT_SAMPLE}")


if __name__ == "__main__":
    main()
