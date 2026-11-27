# -*- coding: utf-8 -*-
"""M2b V1 冒烟：渲染 P1H_INDEX（v1 注入版），调一次 LLM，验证 JSON 契约不破。
产出: smoke-v1-result.json = {ok, n_nodes, fields_ok, raw_head_200ch}
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))          # ablation_harness.py
sys.path.insert(0, os.path.join(HERE, "v1"))          # v1/prompts.py

from ablation_harness import call_llm
from prompts import P1H_INDEX

QUESTION = "台风在登陆前后强度衰减的主要物理机制是什么？"
PARENTS_BLOCK = "N1 [L1] (edge=cartesian): 台风强度衰减的总能量收支 = 海洋热通量输入 − 摩擦耗散 − 辐射/湍流损耗"


def main():
    prompt = P1H_INDEX.format(
        question=QUESTION,
        confirmed_block="",
        parents_block=PARENTS_BLOCK,
        start=1,
    )
    out = call_llm(prompt, max_tokens=512, timeout=120, retries=1,
                   temperature=0.7, enable_thinking=False)
    raw = out[0] if isinstance(out, tuple) else out
    if not isinstance(raw, str):
        raw = json.dumps(raw, ensure_ascii=False)

    # 剥 markdown fence（若有）
    txt = raw.strip()
    if txt.startswith("```"):
        txt = txt.split("\n", 1)[1] if "\n" in txt else txt
        if txt.endswith("```"):
            txt = txt[:-3]
        txt = txt.strip()

    result = {"ok": False, "n_nodes": 0, "fields_ok": False,
              "raw_head_200ch": raw[:200]}
    try:
        data = json.loads(txt)
    except Exception as e:
        result["error"] = f"json.loads failed: {e}"
        with open(os.path.join(HERE, "smoke-v1-result.json"), "w") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(json.dumps(result, ensure_ascii=False))
        return

    nodes = data.get("nodes")
    if not isinstance(nodes, list):
        result["error"] = "no 'nodes' key or not a list"
        with open(os.path.join(HERE, "smoke-v1-result.json"), "w") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(json.dumps(result, ensure_ascii=False))
        return

    result["n_nodes"] = len(nodes)
    req = {"id", "claim", "level", "source"}
    fields_ok = all(isinstance(n, dict) and req <= set(n.keys()) for n in nodes)
    result["fields_ok"] = fields_ok
    result["ok"] = True
    with open(os.path.join(HERE, "smoke-v1-result.json"), "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
