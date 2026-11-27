#!/usr/bin/env python3
"""机制级微架构内容扫描 (三要素判据) — Q9 budget-scan 1198 节点.

LLM 每批 8 节点, 按三要素判据 (参数变化/影响机制/影响量) 打标 mech/spec/other.
产出: data/q9-budget-scan/mech-level-scan-20261127.json
"""
import json, glob, os, re, sys, time, urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))          # .../research
# 2026-11-27 参数化: argv[1]=数据目录 argv[2]=输出 JSON (默认=原 baseline 路径, 向后兼容)
DATA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "..", "data", "q9-budget-scan")
FILES = sorted(glob.glob(os.path.join(DATA, "q9-*-r*.json")))
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(DATA, "mech-level-scan-20261127.json")
ENDPOINT = "http://127.0.0.1:8787/v1/chat/completions"
MODEL = "qwen3.8-27b"
BATCH = 8
CLAIM_CHARS = 300
MAX_RETRY = 3

SYSTEM_PROMPT = """你是计算机体系结构评审员。对每个节点 claim 按三要素判据打标:
1. 参数变化: 含具体参数/配置的变化或对比 (cache 大小/带宽/指令周期/占用率/batch size/量化位宽等的具体数值对比或取值)
2. 影响机制: 真正的因果解释 — 该参数如何影响访存/计算/流水线 (why/how, 不是泛泛"会影响性能")
3. 影响量: 量化结果 — 数值估计/百分比/公式推导 (如 27B×2B/4=13.5GB 这类算术也算)
标签:
- "mech" = 三要素全有
- "spec" = 只有规格值罗列 (①可能有, ②③缺)
- "other" = 与微架构/访存/计算效率无关 (流程/调度/成本/工具链等)
只输出一个 JSON 对象, 键为节点编号, 值为标签, 无任何其他文字。"""


def llm_call(prompt: str) -> str:
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps({"model": MODEL, "temperature": 0,
                         "messages": [{"role": "system", "content": SYSTEM_PROMPT},
                                      {"role": "user", "content": prompt}]}).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.load(r)["choices"][0]["message"]["content"]


def extract_json(text: str):
    t = text.strip()
    t = re.sub(r"^```(?:json)?\s*", "", t)
    t = re.sub(r"\s*```$", "", t)
    i, j = t.find("{"), t.rfind("}")
    if i == -1 or j <= i:
        raise ValueError("no JSON object in output")
    return json.loads(t[i:j + 1])


def main():
    nodes = []  # (key, run_tag, level, claim)
    for f in FILES:
        d = json.load(open(f))
        run_tag = os.path.basename(f).split("-")[1] + "-" + os.path.basename(f).split("-")[2]  # e.g. 50-r1
        for n in d["nodes"]:
            nodes.append((f"{run_tag}:{n['id']}", run_tag, n["level"], n["claim"]))
    print(f"loaded {len(nodes)} nodes from {len(FILES)} files", flush=True)

    labels = {}
    batches = [nodes[i:i + BATCH] for i in range(0, len(nodes), BATCH)]
    for bi, batch in enumerate(batches):
        lines = []
        for k, _, _, claim in batch:
            lines.append(f"[{k}] {claim[:CLAIM_CHARS]}")
        prompt = "对下列节点逐个打标, 输出 JSON 对象 (键=节点编号, 值=mech/spec/other):\n" + "\n".join(lines)
        for attempt in range(1, MAX_RETRY + 1):
            try:
                obj = extract_json(llm_call(prompt))
                missing = [k for k, *_ in batch if k not in obj or obj[k] not in ("mech", "spec", "other")]
                if missing:
                    raise ValueError(f"missing/invalid: {missing}")
                for k, *_ in batch:
                    labels[k] = obj[k]
                print(f"batch {bi + 1}/{len(batches)} ok (attempt {attempt})", flush=True)
                break
            except Exception as e:
                print(f"batch {bi + 1}/{len(batches)} attempt {attempt} failed: {e}", flush=True)
                if attempt == MAX_RETRY:
                    print("FATAL: batch failed after retries", flush=True)
                    sys.exit(1)
                time.sleep(5 * attempt)

    assert len(labels) == len(nodes), f"label count mismatch: {len(labels)} != {len(nodes)}"

    by_level, by_run = {}, {}
    mech_samples, spec_samples = [], []
    for key, run_tag, level, claim in nodes:
        lab = labels[key]
        for agg in (by_level.setdefault(level, {"total": 0, "mech": 0, "spec": 0, "other": 0}),
                    by_run.setdefault(run_tag, {"total": 0, "mech": 0, "spec": 0, "other": 0})):
            agg["total"] += 1
            agg[lab] += 1
        if lab == "mech" and len(mech_samples) < 30:
            mech_samples.append({"run": run_tag, "id": key.split(":")[1], "level": level,
                                 "claim_excerpt": claim[:80]})
        elif lab == "spec" and len(spec_samples) < 10:
            spec_samples.append({"run": run_tag, "id": key.split(":")[1], "level": level,
                                 "claim_excerpt": claim[:80]})

    tot = {"mech": 0, "spec": 0, "other": 0}
    for v in by_level.values():
        for k in tot:
            tot[k] += v[k]
    conclusion = (f"1198 节点中机制级 (三要素全有) {tot['mech']} 个, "
                  f"规格级 {tot['spec']} 个, 无关 {tot['other']} 个; "
                  f"机制级按深度分布 " +
                  ", ".join(f"{lv}: {by_level[lv]['mech']}" for lv in sorted(by_level)))

    out = {"counts_by_level": {lv: by_level[lv] for lv in sorted(by_level)},
           "counts_by_run": {rt: by_run[rt] for rt in sorted(by_run)},
           "mech_samples": mech_samples,
           "spec_samples": spec_samples,
           "conclusion": conclusion,
           "labels": labels}
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print("written:", OUT)
    print(conclusion)


if __name__ == "__main__":
    main()
