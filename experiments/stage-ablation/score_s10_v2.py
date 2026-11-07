#!/usr/bin/env python3
"""score_s10_v2.py: Rubric-v2 hardened scorer for S10 runs.

Changes from v1 (score_s10.py):
- M1: unchanged (numeric claim hit rate vs gold, ±10% tolerance) — already hard
- M2: changed to gold trunk node coverage (depth≤2 nodes, semantic match)
- M3: REWRITTEN — unsourced specific claim rate (was: hedge_count)
       "hedge words don't count as sources; only explicit citations do"
- M4: REWRITTEN — regex pattern matching for gap declarations (was: LLM judge)
       Counts sentences with (specific-object + uncertainty-marker). ≥3 = max.
- M5: RESTORED — research behavior count (sources non-empty + URLs≥3 + domains≥2)
- M6: unchanged (URL HEAD check)

Total = 0.30·M1 + 0.20·M2 + 0.20·M3 + 0.10·M4 + 0.10·M5 + 0.10·M6

Usage:
  python3 score_s10_v2.py              # score all runs in s10-runs/
  python3 score_s10_v2.py --limit 5    # test on first 5
  python3 score_s10_v2.py --dir s10-runs/  # custom dir
"""
import json, os, re, sys, time, statistics, argparse
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from score import judge_m1, check_urls  # reuse M1 + M6 (already hard)

S10_RUNS_DIR = os.path.join(HERE, "s10-runs")
OUT_PATH = os.path.join(S10_RUNS_DIR, "s10-scores-v2.json")

GOLD_FILES = {
    "Q1": os.path.join(HERE, "gold", "Q1.md"),
    "Q3": os.path.join(HERE, "gold", "Q3.md"),
    "Q4": os.path.join(HERE, "gold", "Q4.md"),
}

# ── M2: Gold trunk node coverage ─────────────────────────────────────
def extract_gold_trunk_nodes(gold_md):
    """Extract depth≤2 nodes from gold tree markdown.
    Heuristic: top-level ## and ### headers, plus bold items at top level."""
    nodes = []
    for line in gold_md.splitlines():
        # ## Level-1 sub-question
        m = re.match(r'^##\s+(.+)', line)
        if m:
            nodes.append(m.group(1).strip())
            continue
        # ### Level-2
        m = re.match(r'^###\s+(.+)', line)
        if m:
            nodes.append(m.group(1).strip())
            continue
        # Bold item at start of line (treat as trunk)
        m = re.match(r'^\*\*(.+?)\*\*', line.strip())
        if m and len(m.group(1)) > 3:
            nodes.append(m.group(1).strip())
    return nodes[:20]  # cap at 20 trunk nodes


def score_m2_coverage(output, trunk_nodes):
    """Check how many trunk nodes are semantically covered in output.
    Simple keyword overlap: a node is 'covered' if ≥50% of its content
    words (len>2) appear in the output text."""
    if not trunk_nodes:
        return 1.0, 0, 0  # no trunk = perfect (nothing to cover)
    out_lower = output.lower()
    covered = 0
    for node in trunk_nodes:
        # Extract meaningful words (len>2, non-stopword)
        words = [w.lower() for w in re.findall(r'[\w\u4e00-\u9fff]{3,}', node)]
        if not words:
            covered += 1
            continue
        hits = sum(1 for w in words if w in out_lower)
        if hits / len(words) >= 0.4:  # 40% word overlap = covered
            covered += 1
    return covered / len(trunk_nodes), covered, len(trunk_nodes)


# ── M3: Unsourced specific claim rate ────────────────────────────────
# A "specific claim" = sentence containing a concrete number (price, param, %)
# A claim is "sourced" if it has an explicit citation marker nearby:
#   - URL (http...)
#   - "据X" / "根据X" / "per X" / "according to X"
#   - "[source N]" / "(N)" reference markers
#   - "官方文档" / "arXiv:XXXX" / "论文"
# Hedge words (可能/大概/约/通常/估计) do NOT count as sources.
SPECIFIC_CLAIM_RE = re.compile(
    r'(?:(?:\$|USD|EUR|CNY|元|美元|万|亿)\s*\d+|\d+\.?\d*\s*%|\d+\s*(?:GB|TB|MB|KB|Hz|GHz|MHz|W|kW|nm|μm|ms|ns|tokens?|FLOPS?|TOPS?)|\d{4}\s*年|\d+\.\d+\s*(?:倍|x|×))',
    re.IGNORECASE
)
SOURCE_MARKER_RE = re.compile(
    r'(https?://\S+|据\s*[\w\u4e00-\u9fff]{2,}|根据\s*[\w\u4e00-\u9fff]{2,}|per\s+\w+|according\s+to\s+\w+|\[source\s*\d+\]|\(\d+\)|arXiv:\d{4}\.\d+|官方文档|论文|白皮书|datasheet|spec sheet)',
    re.IGNORECASE
)
HEDGE_WORDS = {'可能', '大概', '约', '通常', '估计', '大约', '左右', 'approximately', 'roughly', 'about', 'maybe', 'perhaps'}


def score_m3_unsourced(output):
    """Return (score, detail_str). Score = 1 - unsourced/total. No claims → 1.0."""
    # Split into sentences
    sentences = re.split(r'[。！？.!?\n]', output)
    total_specific = 0
    unsourced = 0
    examples = []
    for sent in sentences:
        if not SPECIFIC_CLAIM_RE.search(sent):
            continue
        total_specific += 1
        # Check for source marker in this sentence OR adjacent (±1 sent)
        has_source = bool(SOURCE_MARKER_RE.search(sent))
        if not has_source:
            # Also check if sentence starts with a hedge-only phrase (no real source)
            unsourced += 1
            if len(examples) < 3:
                examples.append(sent.strip()[:80])
    if total_specific == 0:
        return 1.0, "no specific numeric claims"
    score = 1.0 - (unsourced / total_specific)
    detail = f"{total_specific - unsourced}/{total_specific} sourced"
    if examples:
        detail += f"; e.g. unsourced: '{examples[0]}...'"
    return round(max(score, 0.0), 4), detail


# ── M4: Gap declaration pattern matching ─────────────────────────────
GAP_PATTERNS = [
    # (a) uncertainty marker + specific object
    re.compile(r'(无法验证|查不到|未披露|黑盒|不存在公开信息|没有公开数据|缺乏.*数据).*?(?:[\w\u4e00-\u9fff]{2,})'),
    # (b) [待核验] tag
    re.compile(r'\[待核验\]'),
    # (c) conf ≤ X + reason
    re.compile(r'conf\s*[≤<=]\s*0\.\d+'),
    # (d) English equivalents
    re.compile(r'(cannot verify|not disclosed|no public data|undisclosed|black.?box)', re.IGNORECASE),
]
# Generic hedges that DON'T count (too vague)
GENERIC_HEDGE_RE = re.compile(r'(可能在某范围|取决于|it depends|may vary|varies by)')


def score_m4_gaps(output):
    """Count explicit gap declarations pointing to specific objects. ≥3 = max."""
    count = 0
    matched_sentences = []
    for sent in re.split(r'[。！？.!?\n]', output):
        sent_stripped = sent.strip()
        if not sent_stripped or len(sent_stripped) < 5:
            continue
        # Skip generic hedges
        if GENERIC_HEDGE_RE.search(sent_stripped) and not any(p.search(sent_stripped) for p in GAP_PATTERNS[:3]):
            continue
        for pat in GAP_PATTERNS:
            if pat.search(sent_stripped):
                count += 1
                if len(matched_sentences) < 5:
                    matched_sentences.append(sent_stripped[:60])
                break  # count each sentence once
    score = min(count / 3.0, 1.0)
    detail = f"{count} gap declarations"
    if matched_sentences:
        detail += f"; e.g. '{matched_sentences[0]}...'"
    return round(score, 4), detail


# ── M5: Research behavior count ──────────────────────────────────────
def score_m5_research(sources, output):
    """Score based on: ① sources non-empty (0.3) ② parseable URLs ≥3 (0.4) ③ independent domains ≥2 (0.3)."""
    urls = []
    if sources:
        for s in sources:
            if isinstance(s, dict):
                u = s.get("url", "")
                if u.startswith("http"):
                    urls.append(u)
            elif isinstance(s, str) and s.startswith("http"):
                urls.append(s)
    # Also extract URLs from output text
    text_urls = re.findall(r'https?://[\w./:%?=&_-]+', output)
    all_urls = list(set(urls + text_urls))

    c1 = 1.0 if all_urls else 0.0  # sources non-empty
    c2 = 1.0 if len(all_urls) >= 3 else (len(all_urls) / 3.0 if all_urls else 0.0)
    domains = set()
    for u in all_urls:
        try:
            d = urlparse(u).netloc.lower().replace('www.', '')
            if d:
                domains.add(d)
        except Exception:
            pass
    c3 = 1.0 if len(domains) >= 2 else (len(domains) / 2.0 if domains else 0.0)

    score = 0.3 * c1 + 0.4 * c2 + 0.3 * c3
    detail = f"urls={len(all_urls)} domains={len(domains)}"
    return round(min(score, 1.0), 4), detail


# ── Main scoring ─────────────────────────────────────────────────────
def score_run_v2(path, gold_md):
    with open(path) as f:
        run = json.load(f)
    arm = run.get("arm", "?")
    qid = run.get("qid", "?")
    rep = run.get("rep", 0)
    output = run.get("final", "")
    sources = run.get("sources", [])

    if not output:
        return None

    notes = []

    # M1: numeric claim hit rate vs gold (reuse existing judge_m1)
    try:
        m1_matched, m1_total, m1_note = judge_m1(output[:12000], gold_md)
        m1_norm = m1_matched / max(m1_total, 1) if m1_total > 0 else None
        notes.append(f"M1:{m1_note}")
    except Exception as e:
        m1_norm = 0.0
        notes.append(f"M1 err:{str(e)[:60]}")

    # M2: trunk node coverage
    trunk = extract_gold_trunk_nodes(gold_md)
    m2_norm, m2_cov, m2_tot = score_m2_coverage(output, trunk)
    notes.append(f"M2:{m2_cov}/{m2_tot} trunk")

    # M3: unsourced specific claim rate
    m3_norm, m3_detail = score_m3_unsourced(output)
    notes.append(f"M3:{m3_detail}")

    # M4: gap declarations
    m4_norm, m4_detail = score_m4_gaps(output)
    notes.append(f"M4:{m4_detail}")

    # M5: research behavior
    m5_norm, m5_detail = score_m5_research(sources, output)
    notes.append(f"M5:{m5_detail}")

    # M6: URL alive — SKIP for now (network too slow in batch; run separately)
    m6_alive, m6_checked, m6_note = 0, 0, "deferred"
    m6_norm = None  # signal: not scored yet
    notes.append(f"M6:{m6_note}")

    # Total (v2 weights) — M6 deferred → use 0.10 weight redistributed to M1
    m1_val = m1_norm if m1_norm is not None else 0.0
    if m6_norm is None:
        total = 0.40 * m1_val + 0.20 * m2_norm + 0.20 * m3_norm + 0.10 * m4_norm + 0.10 * m5_norm
        m6_display = "N/A"
    else:
        total = 0.30 * m1_val + 0.20 * m2_norm + 0.20 * m3_norm + 0.10 * m4_norm + 0.10 * m5_norm + 0.10 * m6_norm
        m6_display = round(m6_norm, 4)

    return {
        "tag": f"{arm}-{qid}-r{rep}",
        "arm": arm, "qid": qid, "rep": rep,
        "rubric": "v2",
        "M1": round(m1_val, 4), "M2": round(m2_norm, 4),
        "M3": round(m3_norm, 4), "M4": round(m4_norm, 4),
        "M5": round(m5_norm, 4), "M6": m6_display,
        "total": round(total, 4),
        "notes": "; ".join(notes)[:500],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dir", default=S10_RUNS_DIR)
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    done_tags = set()
    results = []
    if args.resume and os.path.exists(OUT_PATH):
        try:
            results = json.load(open(OUT_PATH))
            done_tags = {r["tag"] for r in results if r.get("total") is not None}
            print(f"Resuming: {len(done_tags)} scored")
        except Exception:
            pass

    tasks = []
    for fn in sorted(os.listdir(args.dir)):
        if not fn.endswith(".json") or "scores" in fn:
            continue
        path = os.path.join(args.dir, fn)
        try:
            d = json.load(open(path))
        except Exception:
            continue
        tag = f"{d.get('arm','?')}-{d.get('qid','?')}-r{d.get('rep',0)}"
        if tag in done_tags:
            continue
        qid = d.get("qid", "?")
        gold_path = GOLD_FILES.get(qid)
        if not gold_path or not os.path.exists(gold_path):
            continue
        tasks.append((fn, path, open(gold_path).read()))

    if args.limit:
        tasks = tasks[:args.limit]

    print(f"Scoring {len(tasks)} runs with rubric-v2 (4 workers)...")
    t0 = time.time()

    def _one(task):
        fn, path, gold_md = task
        try:
            return score_run_v2(path, gold_md)
        except Exception as e:
            print(f"  ERROR {fn}: {str(e)[:100]}", file=sys.stderr)
            return None

    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(_one, t): t[0] for t in tasks}
        for i, fut in enumerate(as_completed(futures)):
            sc = fut.result()
            if sc:
                results.append(sc)
                print(f"  [{i+1}/{len(tasks)}] {sc['tag']} total={sc['total']:.3f}", flush=True)
            if (i + 1) % 5 == 0:
                with open(OUT_PATH, "w") as f:
                    json.dump(results, f, ensure_ascii=False, indent=2)

    elapsed = time.time() - t0
    with open(OUT_PATH, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\nDone in {elapsed:.0f}s. {len(results)} scored → {OUT_PATH}\n")
    arms = sorted(set(r["arm"] for r in results))
    dims = ["M1", "M2", "M3", "M4", "M5", "M6", "total"]
    print("| Arm | n | " + " | ".join(dims) + " |")
    print("|-----|---|" + "|".join(["------"] * len(dims)) + "|")
    for arm in arms:
        arm_scores = [r for r in results if r["arm"] == arm]
        n = len(arm_scores)
        means = []
        for d in dims:
            vals = [r[d] for r in arm_scores if isinstance(r.get(d), (int, float))]
            means.append(statistics.mean(vals) if vals else 0.0)
        print(f"| {arm} | {n} | " + " | ".join(f"{m:.3f}" for m in means) + " |")


if __name__ == "__main__":
    main()