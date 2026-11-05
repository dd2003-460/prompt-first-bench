"""T22 conservative post-checks. Heuristics are not evidence verification."""
import re
from collections import defaultdict

# Numbers with explicit quantitative units only: conservative high precision, incomplete recall.
NUMBER = re.compile(r'(?<![\w.])(?:[<>≤≥~≈约]?\s*)?(\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?)(?:\s*[-–—至~]\s*(\d+(?:\.\d+)?))?\s*(TFLOPS|TOPS|TB/s|GB/s|tok(?:ens)?/s|tokens?|GB|TB|ms|秒|毫秒|瓦|W|%|％|元|美元|倍|x|X|万|亿)(?![a-zA-Z])', re.I)
ANCHOR = re.compile(r'https?://[^\s)）\]】>]+|\[[^\]]+\]\(https?://[^)]+\)|datasheet|数据手册|规格书|核验日期\s*[:：]?\s*\d{4}[-/]\d{1,2}[-/]\d{1,2}', re.I)
# 不可定位来源：跳转链接/聚合页，不算有效锚点（T23 gold-gap-diagnosis 行动项）
BAD_ANCHOR = re.compile(r'bing\.com/ck/a|google\.com/url\?|bit\.ly/|t\.co/', re.I)
HEDGE = re.compile(r'可能|大概|或许')
BOUND = re.compile(r'如果|若|条件|场景|情况下|前提|当.{0,20}时|未验证|不确定|需要.{0,8}(?:验证|实测|核验)|取决于')
LABEL = re.compile(r'\b(?:fact|inference)\b|事实\s*[:：]|推断\s*[:：]', re.I)
LIMIT = re.compile(r'限制|不确定|未验证|未核验|无法|未知|缺少|缺乏|不足|风险')
CONCLUSION = re.compile(r'^\s*#{1,6}\s*.*(?:结论|总结|建议|推荐|conclusion|summary)', re.I)
HEADER = re.compile(r'^\s*#{1,6}\s')
SKU = re.compile(r'(?<![a-z])(?:pcie|sxm)(?![a-z])', re.I)
PROPERTY = re.compile(r'显存带宽|内存带宽|memory bandwidth|hbm(?:2e|3)?\s*带宽', re.I)


def lines_for(text):
    return [line for line in text.splitlines() if line.strip()]


def analyze(text):
    lines = text.splitlines()
    candidates = []
    propositions = defaultdict(list)
    hedges = 0
    unbounded = 0
    labelled = 0
    fact_candidates = 0
    for index, line in enumerate(lines):
        found = list(NUMBER.finditer(line))
        if found:
            # Claim-level anchor: 只有同一行出现锚点才算该数字有来源（T23-v2 gate defect fix）
            anchored = bool(ANCHOR.search(line)) and not BAD_ANCHOR.search(line)
            for match in found:
                item = {"line": index + 1, "text": match.group(0).strip(),
                        "anchor_present": anchored, "source_verified": False}
                candidates.append(item)
                if PROPERTY.search(line) and match.group(3).lower() in ('tb/s', 'gb/s'):
                    sku = SKU.findall(line)
                    if len(set(s.lower() for s in sku)) == 1 and not match.group(2):
                        value = float(match.group(1).replace(',', ''))
                        if match.group(3).lower() == 'gb/s':
                            value /= 1000
                        propositions[(sku[0].lower(), 'memory_bandwidth_tb_s')].append((value, index + 1))
        hits = HEDGE.findall(line)
        hedges += len(hits)
        if hits and not BOUND.search(line):
            unbounded += len(hits)
        # Candidate factual statements: limited to lines containing detected quantities.
        if found:
            fact_candidates += 1
            labelled += bool(LABEL.search(line))
    conflicts = []
    for (sku, prop), entries in propositions.items():
        values = sorted(set(value for value, _ in entries))
        if len(values) > 1:
            for i, a in enumerate(values):
                for b in values[i+1:]:
                    conflicts.append({"key": f"{sku}.{prop}", "values": [a, b],
                                      "lines": sorted({line for value, line in entries if value in (a, b)})})
    nonempty = lines_for(text)
    first_third = max(1, (len(nonempty) + 2) // 3)
    limits = [i for i, line in enumerate(nonempty) if LIMIT.search(line)]
    return {"numeric_claims": candidates, "numeric_count": len(candidates),
            "unanchored_count": sum(not x['anchor_present'] for x in candidates),
            "unanchored_rate": (sum(not x['anchor_present'] for x in candidates) / len(candidates)) if candidates else None,
            "conflicts": conflicts, "conflict_pair_count": len(conflicts),
            "hedge_count": hedges, "unbounded_hedge_count": unbounded,
            "bare_hedge_rate": unbounded / hedges if hedges else None,
            "fact_candidate_lines": fact_candidates, "labelled_fact_candidate_lines": labelled,
            "fact_label_coverage": labelled / fact_candidates if fact_candidates else None,
            "limit_statements": len(limits), "limit_in_first_third": sum(i < first_third for i in limits),
            "limit_first_third_rate": sum(i < first_third for i in limits) / len(limits) if limits else None,
            "accuracy": None, "accuracy_reason": "manual independently verified atomic gold mapping not implemented",
            "limitations": ["numeric regex incomplete; no semantic claim segmentation", "URL/anchor existence and relevance not verified", "conflicts limited to explicit same-SKU memory bandwidth, not all semantic conflicts", "fact label and hedge detectors are lexical proxies"]}


def apply(text, arm):
    """A untouched; B all gates; C numeric gate only. Conservative quarantine is reversible."""
    raw = analyze(text)
    if arm == 'A':
        return {"raw": raw, "published": text, "quarantine": [], "post": raw}
    lines = text.splitlines()
    conflicted = {n for c in raw['conflicts'] for n in c['lines']} if arm == 'B' else set()
    output, quarantine = [], []
    conclusion = False
    for index, line in enumerate(lines, 1):
        if HEADER.match(line):
            conclusion = bool(CONCLUSION.match(line))
        reasons = []
        if NUMBER.search(line) and not ANCHOR.search(line):
            reasons.append('unverified')
        if index in conflicted:
            reasons.append('conflict')
        if reasons:
            quarantine.append({"line": index, "text": line, "status": reasons, "was_conclusion": conclusion})
            output.append(f"[隔离：{'/'.join(reasons)}；原文见 quarantine 第 {index} 行]")
        else:
            output.append(line)
    if arm == 'B':
        output.insert(0, '限制：以下检查仅识别部分模式；来源、冲突和事实需独立核验。')
    published = '\n'.join(output)
    return {"raw": raw, "published": published, "quarantine": quarantine, "post": analyze(published),
            "checklist": {"fact_inference_labels": "observed lexical counts only; no fabricated labels",
                          "boundary": "heuristic only", "limitation_front": arm == 'B'}}
