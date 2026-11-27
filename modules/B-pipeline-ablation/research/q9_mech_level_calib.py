#!/usr/bin/env python3
"""Judge 校准: 对 Lead 手工标注的 16 条边界样例用同一 prompt 判一遍,
算 exact match 一致率 + 混淆矩阵, 写进 mech-level-scan-20261127.json 的 calibration 字段.
一致率 <75% 时在 conclusion 追加松紧未校准声明.
"""
import json, os, re, sys, time, urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "..", "data", "q9-budget-scan")
CALIB = os.path.join(DATA, "judge-calib-set-20261127.json")
RESULT = os.path.join(DATA, "mech-level-scan-20261127.json")
ENDPOINT = "http://127.0.0.1:8787/v1/chat/completions"
MODEL = "qwen3.8-27b"
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
    calib = json.load(open(CALIB))["labels"]
    result = json.load(open(RESULT))
    labels = result["labels"]

    # 拉取 16 条 claim 原文
    claims = {}
    for item in calib:
        run_tag = item["run"].replace("q9-", "").rstrip("-")   # "q9-100-r1-" -> "100-r1"
        key = f"{run_tag}:{item['id']}"
        if key not in labels:
            print(f"WARN: key {key} not in scan labels", flush=True)
            continue
        claims[key] = item

    # 用同一 prompt 判这 16 条 (2 批 × 8)
    fresh = {}
    items = list(claims.items())
    for bi in range(0, len(items), 8):
        batch = items[bi:bi + 8]
        lines = [f"[{k}] {_claim_of(k)[:CLAIM_CHARS]}" for k, _ in batch]
        prompt = "对下列节点逐个打标, 输出 JSON 对象 (键=节点编号, 值=mech/spec/other):\n" + "\n".join(lines)
        for attempt in range(1, MAX_RETRY + 1):
            try:
                obj = extract_json(llm_call(prompt))
                missing = [k for k, _ in batch if k not in obj or obj[k] not in ("mech", "spec", "other")]
                if missing:
                    raise ValueError(f"missing/invalid: {missing}")
                for k, _ in batch:
                    fresh[k] = obj[k]
                print(f"calib batch {bi // 8 + 1} ok (attempt {attempt})", flush=True)
                break
            except Exception as e:
                print(f"calib batch {bi // 8 + 1} attempt {attempt} failed: {e}", flush=True)
                if attempt == MAX_RETRY:
                    sys.exit(1)
                time.sleep(5 * attempt)

    # 一致率 + 混淆矩阵 (judge = 本次 fresh 判定, lead = 人工标注)
    agree = 0
    cm = {a: {b: 0 for b in ("mech", "spec", "other")} for a in ("mech", "spec", "other")}
    details = []
    for key, item in claims.items():
        lead = item["lead_label"]
        judge = fresh.get(key)
        if judge is None:
            continue
        cm[lead][judge] += 1
        if lead == judge:
            agree += 1
        details.append({"run": item["run"], "id": item["id"], "lead_label": lead,
                        "judge_label": judge, "match": lead == judge})
    n = len(details)
    acc = agree / n if n else 0.0

    result["calibration"] = {
        "n": n, "agree": agree, "accuracy": round(acc, 4),
        "confusion_matrix": {"rows_lead_label": list(cm), "cols_judge_label": list(cm), "matrix": cm},
        "details": details}

    if acc < 0.75:
        note = "judge 松紧未校准，绝对值不可信，仅跨档相对值可用"
        if note not in result["conclusion"]:
            result["conclusion"] += f" (一致率 {acc:.0%} <75%: {note})"

    json.dump(result, open(RESULT, "w"), ensure_ascii=False, indent=1)
    print(f"accuracy={agree}/{n}={acc:.4f}")
    print("written calibration into", RESULT)


_CLAIM_CACHE = {}

def _claim_of(key: str) -> str:
    if key in _CLAIM_CACHE:
        return _CLAIM_CACHE[key]
    run_tag, nid = key.split(":")
    import glob
    pat = os.path.join(DATA, f"q9-{run_tag}-*.json")
    f = glob.glob(pat)[0]
    d = json.load(open(f))
    for node in d["nodes"]:
        if node["id"] == nid:
            _CLAIM_CACHE[key] = node["claim"]
            return node["claim"]
    raise KeyError(key)


if __name__ == "__main__":
    main()
