#!/usr/bin/env python3
"""PoC: 思考→行动接线最小验证 (⑥ 前置探针)。

问题: 模型生成 [质询]/source=search 节点后, 如果 harness 暴露 search 工具,
     它会自发调用吗? (根因假设: harness 没传 tools, 模型有能力但没接口)

设计 (最小, 单变量 = tools 有无):
  A 臂: 无 tools, 现状 prompt → 基线 (预期: 不调用, 只有文字)
  B 臂: 同一 prompt + tools=[search] → 测自发 tool_call 率
  节点来源: Q9 已完成 run 中真实带 [质询] 或 source=search 的节点 (非人造)
  n = 10 节点 × 2 臂 = 20 次调用, 单次 max_tokens 1024

输出: data/q9-budget-scan/tool-poc-<date>.json
  {arm_A: {n_tool_calls, per_node:[...]}, arm_B: {...}, verdict_hint}
"""
import json, os, re, sys, time, urllib.request
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data", "q9-budget-scan")
LLM_URL = "http://127.0.0.1:8787/v1/chat/completions"
N_NODES = 10

TOOLS = [{
    "type": "function",
    "function": {
        "name": "search",
        "description": "检索外部资料。当你不确定某个数值/规格/事实、或生成了 [质询] 标记时, 用此工具查证。",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string", "description": "检索查询语句"}},
            "required": ["query"],
        },
    },
}]

def call(payload):
    req = urllib.request.Request(LLM_URL, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read())["choices"][0]["message"]

def pick_nodes():
    """从 Q9 已完成 run 里挑真实带 [质询] 或 source=search 的节点。"""
    runs = sorted(f for f in os.listdir(DATA) if re.match(r"q9-\d+-r\d+-2026.*\.json$", f))
    picked = []
    for fn in runs:
        d = json.load(open(os.path.join(DATA, fn)))
        for n in d.get("nodes", []):
            claim = n.get("claim", "")
            if "[质询]" in claim or n.get("source") == "search":
                picked.append({"run": fn, "id": n["id"], "claim": claim[:500],
                               "parent": (n.get("parent_claim") or "")[:200]})
        if len(picked) >= N_NODES:
            break
    return picked[:N_NODES]

def run_arm(nodes, with_tools):
    results = []
    for n in nodes:
        prompt = (
            "你是研究员, 正在构建决策树。下面是父节点和你的新节点。\n"
            f"父节点: {n['parent']}\n你的节点: {n['claim']}\n\n"
            "请对这个节点做核验: 检查其中的数值/规格是否可靠, 不确定就查证。"
            "输出你的核验过程和结论。"
        )
        payload = {"model": "qwen3.8-27b", "messages": [{"role": "user", "content": prompt}],
                   "max_tokens": 1024, "temperature": 0.0}
        if with_tools:
            payload["tools"] = TOOLS
        msg = call(payload)
        tc = msg.get("tool_calls") or []
        results.append({"node": n["id"], "run": n["run"],
                        "n_tool_calls": len(tc),
                        "queries": [t["function"]["arguments"] for t in tc],
                        "text_head": (msg.get("content") or "")[:150]})
        time.sleep(0.5)
    return results

def main():
    nodes = pick_nodes()
    print(f"picked {len(nodes)} nodes with [质询]/source=search", flush=True)
    a = run_arm(nodes, with_tools=False)
    b = run_arm(nodes, with_tools=True)
    out = {
        "observed_at": datetime.now(timezone.utc).astimezone().isoformat(),
        "n_nodes": len(nodes),
        "arm_A_no_tools": {"n_with_toolcall": sum(1 for r in a if r["n_tool_calls"]), "per_node": a},
        "arm_B_with_tools": {"n_with_toolcall": sum(1 for r in b if r["n_tool_calls"]), "per_node": b},
    }
    fp = os.path.join(DATA, f"tool-poc-{datetime.now().strftime('%Y%m%d')}.json")
    json.dump(out, open(fp, "w"), ensure_ascii=False, indent=1)
    print(f"A: {out['arm_A_no_tools']['n_with_toolcall']}/{len(nodes)}  "
          f"B: {out['arm_B_with_tools']['n_with_toolcall']}/{len(nodes)}", flush=True)
    print("saved:", fp, flush=True)

if __name__ == "__main__":
    main()
