#!/usr/bin/env python3
"""XREF: gpt-researcher + 本地 27b 跑 Q2 模型选型题（对照 S0-Q2 基线同坐标系）
origin: ai · 2026-11-24 · D 指令「拿成熟的 autoresearch 跑我们的 idea」
端点: 127.0.0.1:8787 (vLLM, OpenAI 兼容, 模型 qwen3.8-27b-mtp)
"""
import os, sys, json, time

os.environ["LLM_PROVIDER"] = "openai"
os.environ["OPENAI_API_KEY"] = "local"
os.environ["OPENAI_BASE_URL"] = "http://127.0.0.1:8787/v1"
os.environ["FAST_LLM"] = "openai:qwen3.8-27b-mtp"
os.environ["SMART_LLM"] = "openai:qwen3.8-27b-mtp"
os.environ["STRATEGIC_LLM"] = "openai:qwen3.8-27b-mtp"
os.environ["EMBEDDING"] = "openai:text-embedding-3-small"  # 仅用于报告结构，不影响研究
os.environ["RETRIEVER"] = "duckduckgo"  # 免费无 key（默认 tavily 无 key）

sys.path.insert(0, "/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/runs/d1-gpt-researcher")

# 2026-11-25 修复: ddgs 默认 backend=mojeek 在本机网络层被封 (curl HTTP 000),
# backend=duckduckgo 亦 No results; backend=bing 可达 (实测 3 results, llm-stats/benchlm)。
# gpt-researcher 的 duckduckgo retriever 内部 `from ddgs import DDGS; DDGS().text(...)`
# (retrievers/duckduckgo/duckduckgo.py L32-49), 故在此对 DDGS.text 注入 backend=bing。
# 搜索不碰 vLLM; 全臂重跑仍需等 pilot 释放 8787。
import ddgs as _ddgs
_orig_ddg_text = _ddgs.DDGS.text

def _ddg_text_bing(self, query, *a, **kw):
    kw.setdefault("backend", "bing")
    return _orig_ddg_text(self, query, *a, **kw)

_ddgs.DDGS.text = _ddg_text_bing

from gpt_researcher import GPTResearcher

QUESTION = """我要为一个内部代码助手选一个开源大模型，主要任务是函数级代码补全（Python/JS）和通用指令跟随，预算是单台双卡 24GB 或等效 API 额度。候选有 Qwen3-32B、Qwen2.5-Coder-32B-Instruct、Mistral-Small-2501-24B、GLM-4-32B-0414、DeepSeek-Coder-V2-33B、Llama-3.3-70B-Instruct(W4) 这几个。
请帮我拆解：决定「每千次合格回答的总成本」的所有因素都有哪些，并判断哪个模型最划算。"""

OUT = "/Users/a1-6/Desktop/workspace/pfb/tasks/XREF-external-reference/gptr-q2-r1.json"

def main():
    import asyncio
    t0 = time.time()
    async def run():
        r = GPTResearcher(query=QUESTION, report_type="research")
        await r.conduct_research()
        report = await r.write_report()
        return r, report
    r, report = asyncio.run(run())
    wall = time.time() - t0
    d = {
        "arm": "GPTResearcher-27b",
        "qid": "Q2",
        "rep": 1,
        "model": "qwen3.8-27b-mtp",
        "system": "gpt-researcher v0.16.0",
        "params": {"max_iterations": 1, "report_type": "research", "retriever": "duckduckgo"},
        "output_text": report,
        "wall_s": round(wall, 1),
    }
    json.dump(d, open(OUT, "w"), ensure_ascii=False, indent=2)
    print(f"OK wall={wall:.0f}s len={len(report)} -> {OUT}")
    print("head:", report[:300].replace("\n", " "))

if __name__ == "__main__":
    main()
