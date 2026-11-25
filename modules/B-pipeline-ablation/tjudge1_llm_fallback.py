#!/usr/bin/env python3
"""T-JUDGE-1 J4: LLM 兜底二元裁决（磁体匹配 + 低 sim 节点）

输入: tjudge1-llm-fallback-gpu.json（embedding 阶段降级 pending_llm 的节点）
调用: 本地 27b (127.0.0.1:8787)，temp=0，每节点 1 次调用
裁决: 二元 yes/no（节点是否真覆盖该 gold 单元），不做 0-1 连续分
输出: tjudge1-llm-fallback-gpu-adjudicated.json
前置: vLLM 空闲（K7 跑完）——脚本启动时探测 /v1/models，不空闲则退出码 2
"""
import json, os, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
FALLBACK = os.path.join(HERE, "tjudge1-llm-fallback-all.json")
OUT = os.path.join(HERE, "tjudge1-llm-fallback-all-adjudicated.json")
MATCH = os.path.join(HERE, "tjudge1-match-all.json")
API = "http://127.0.0.1:8787/v1/chat/completions"

PROMPT = """你是严格的事实核对员。判断【研究节点】的内容是否实质性覆盖了【标准答案单元】所述的事实/结论。
覆盖 = 节点讨论的核心内容就是该单元的事实（数值近似、表述不同都算覆盖）。
不覆盖 = 只是主题相关（如都提到 GPU/显存）但没说该单元的具体事实。
只回答 JSON: {{"yes": true/false, "reason": "一句话"}}

【标准答案单元】
{gold}

【研究节点】
{node}"""


def llm_binary(gold_text, node_text):
    body = json.dumps({
        "model": "default", "temperature": 0, "max_tokens": 120,
        "messages": [{"role": "user", "content": PROMPT.format(gold=gold_text, node=node_text)}],
    }).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)
    txt = data["choices"][0]["message"]["content"].strip()
    i, j = txt.find("{"), txt.rfind("}")
    try:
        verdict = json.loads(txt[i:j + 1])
        return bool(verdict.get("yes")), str(verdict.get("reason", ""))[:100]
    except Exception:
        return ("yes" in txt.lower() and "no" not in txt.lower()), txt[:100]


def main():
    # vLLM 空闲探测
    try:
        urllib.request.urlopen("http://127.0.0.1:8787/v1/models", timeout=5)
    except Exception as e:
        print(f"vLLM 不可用 ({e})，退出（等 K7 释放后重跑）", file=sys.stderr)
        sys.exit(2)

    items = json.load(open(FALLBACK, encoding="utf-8"))
    # gold 单元全文（从 match 明细取）
    match = json.load(open(MATCH, encoding="utf-8"))
    gold_text = {}
    for name, r in match["runs"].items():
        for m in r["matches"]:
            gold_text.setdefault(m["gold_id"], m["gold_text"])

    results = []
    for i, it in enumerate(items):
        yes, reason = llm_binary(gold_text.get(it["candidate_gold"], it["candidate_gold"]),
                                 it["node_text"])
        results.append({**it, "llm_yes": yes, "llm_reason": reason})
        print(f"[{i+1}/{len(items)}] {it['run']} {it['node_id']} → {it['candidate_gold']}: "
              f"{'YES' if yes else 'no'} ({reason[:50]})")
        time.sleep(0.5)

    json.dump(results, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    n_yes = sum(1 for r in results if r["llm_yes"])
    print(f"\n裁决完成: {n_yes}/{len(results)} yes → {OUT}")
    print("（confirmed 指标需重算: 把 llm_yes 的 gold 单元并入 confirmed 集合，见 decomp J5）")


if __name__ == "__main__":
    main()
