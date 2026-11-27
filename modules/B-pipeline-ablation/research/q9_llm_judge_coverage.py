#!/usr/bin/env python3
"""Q9 gate 覆盖判定 — 换仪器: LLM judge 替代 bge-m3 cosine。

动机 (2026-11-27): cosine 负对照证明正负分布重叠 (p50 均 0.588), 仪器失效。
LLM judge 直接判"节点 claim 是否语义覆盖 gold unit", 不受公式/权重/conf 标注干扰。

输入: data/q9-budget-scan/q9-*-2026*.json (已完成 run, 不重跑 SM)
      data/gold-q9-units.json (gate units, j_id 映射)
输出: data/q9-budget-scan/llm-judge-coverage-<date>.json
      {budget: {gate_jid: {hit_runs: [..], hit_rate, per_run: {rid: bool}}}}

口径: 一个 run 对某 gate 命中 = 该 run 任一节点被判 covered=true。
     judge 输入 = node claim 原文 (截断 400 字) + gold unit 核心内容 (截断 300 字)。
     每 batch 20 节点, 单 LLM 调用, 输出 JSON 数组。
"""
import json, os, re, sys, time, urllib.request
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # modules/B-pipeline-ablation
DATA = os.path.join(BASE, "data", "q9-budget-scan")
GOLD = os.path.join(BASE, "data", "gold-q9-units.json")
LLM_URL = "http://127.0.0.1:8787/v1/chat/completions"
BATCH = 20
CACHE = os.path.join(DATA, ".llm-judge-cache")

def call_llm(prompt, max_tokens=2048, timeout=300):
    payload = json.dumps({"model": "qwen3.8-27b",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens, "temperature": 0.0}).encode()
    req = urllib.request.Request(LLM_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        d = json.loads(r.read())
    return d["choices"][0]["message"].get("content", "")

def load_gate_units():
    g = json.load(open(GOLD))
    gates = set(g.get("gate_units", []))
    out = []
    for u in g["units"]:
        if u.get("j_id") in gates:
            out.append((u["j_id"], u.get("text") or u.get("claim") or ""))
    return out

def judge_batch(units, nodes):
    """units: [(jid, text)], nodes: [(nid, claim)] -> {nid: {jid: bool}}"""
    upart = "\n".join(f"[{j}] {t[:300]}" for j, t in units)
    npart = "\n".join(f"[{nid}] {c[:400]}" for nid, c in nodes)
    prompt = (
        "任务: 覆盖判定。下面是 GOLD 单元列表和 NODE 列表。\n"
        "对每个 NODE, 判断它是否语义覆盖了某个 GOLD 单元的核心内容"
        "(数值/公式可不同, 但所述概念/约束/指标必须实质对应; 仅词面重叠不算)。\n"
        "输出要求(严格遵守): 只输出一个 JSON 数组, 不要任何解释/前言/思考文字, "
        "每项 {\"node\":\"<nid>\",\"covers\":[\"<jid>\",...]}, 无覆盖则 covers 为空数组。\n\n"
        f"GOLD:\n{upart}\n\nNODES:\n{npart}"
    )
    out = call_llm(prompt, max_tokens=8192)
    # 模型夹带思考文字时取最后一个能解析的 JSON 数组: 从末尾 ] 向前配平
    res = {}
    end = out.rfind("]")
    while end > 0:
        depth = 0; start = -1
        for i in range(end, -1, -1):
            ch = out[i]
            if ch == "]": depth += 1
            elif ch == "[":
                depth -= 1
                if depth == 0: start = i; break
        if start >= 0:
            try:
                arr = json.loads(out[start:end+1])
                if isinstance(arr, list) and arr and isinstance(arr[0], dict) and "node" in arr[0]:
                    for it in arr:
                        res[it.get("node")] = it.get("covers", [])
                    break
            except Exception:
                pass
        end = out.rfind("]", 0, end)
    if not res:
        print(f"WARN parse-fail, raw head: {out[:200]!r}", flush=True)
    return res

def main():
    units = load_gate_units()
    jids = [j for j, _ in units]
    print(f"gates: {len(jids)} {jids}", flush=True)
    runs = sorted(f for f in os.listdir(DATA)
                  if re.match(r"q9-\d+-r\d+-2026.*\.json$", f))
    result = {}
    for fn in runs:
        m = re.match(r"q9-(\d+)-r(\d+)", fn)
        budget, rid = m.group(1), m.group(2)
        d = json.load(open(os.path.join(DATA, fn)))
        nodes = [(n["id"], n.get("claim", "")) for n in d.get("nodes", [])]
        per_node = {}
        for i in range(0, len(nodes), BATCH):
            ck = f"{fn}_{i}"
            cf = os.path.join(CACHE, ck + ".json")
            if os.path.exists(cf):
                per_node.update(json.load(open(cf)))
                continue
            try:
                r = judge_batch(units, nodes[i:i+BATCH])
                per_node.update(r)
                os.makedirs(CACHE, exist_ok=True)
                json.dump(per_node, open(cf, "w"), ensure_ascii=False)
            except Exception as e:
                print(f"WARN {fn} batch{i}: {e}", flush=True)
            time.sleep(0.5)
        # per-gate: 任一节点覆盖 = 命中
        gate_hit = {j: False for j in jids}
        for nid, covers in per_node.items():
            for j in covers:
                if j in gate_hit:
                    gate_hit[j] = True
        result.setdefault(budget, {})[f"r{rid}"] = {
            "n_nodes": len(nodes), "judged_nodes": len(per_node),
            "gate_hit": gate_hit,
            "n_gates_hit": sum(gate_hit.values()),
        }
        print(f"{fn}: nodes={len(nodes)} judged={len(per_node)} gates_hit={sum(gate_hit.values())}/{len(jids)}", flush=True)
    # 汇总
    summary = {}
    for b, rs in sorted(result.items(), key=lambda x: int(x[0])):
        rates = [r["n_gates_hit"] / len(jids) for r in rs.values()]
        summary[b] = {"mean_gate_hit_rate": round(sum(rates)/len(rates), 3),
                      "per_run": {k: v["n_gates_hit"] for k, v in rs.items()}}
    out = {"instrument": "llm-judge (qwen3.8-27b via 8787, temp=0)",
           "observed_at": datetime.now(timezone.utc).astimezone().isoformat(),
           "jids": jids, "summary": summary, "detail": result}
    fp = os.path.join(DATA, f"llm-judge-coverage-{datetime.now().strftime('%Y%m%d')}.json")
    json.dump(out, open(fp, "w"), ensure_ascii=False, indent=1)
    print("SUMMARY:", json.dumps(summary, ensure_ascii=False), flush=True)
    print("saved:", fp, flush=True)

if __name__ == "__main__":
    main()
