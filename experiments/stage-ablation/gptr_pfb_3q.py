#!/usr/bin/env python3
"""GPT-Researcher 三题 × 3 rep，官方参数 + pfb 检索层（s5 同款）。

2026-11-19：控制变量修订。
- 上一版 gptr_official_3q.py 用 retriever=arxiv，9/9 全检索失败
  （根因：8787 qwen JSON 遵循不稳 → subtopic 分解失败 → 超长中文 query
  打 arxiv 500/503 → 无兜底。诊断见 runs-gptr-official/README.md）。
- 本版注入 PfbRetriever（pfb_retriever.py），底层 = s5 的
  research_hook（wiki/ddg/bing/arxiv/webfetch/webllm 多通道）
  + _ego_direct_fetch（wiki API + ego-browser 直访权威站）兜底。
- 与 s5/langgraph 臂共享同一检索层，消融对比只测 pipeline 结构差异。

官方参数（gpt_researcher v0.16.1）+ depth/breadth 6/6（D 2026-11-18 指令）。
model=qwen3.8-27b @ 127.0.0.1:8787
"""
import asyncio, os, sys, time, json, traceback

os.environ["OPENAI_API_KEY"] = "local-not-needed"
os.environ["OPENAI_BASE_URL"] = "http://127.0.0.1:8787/v1"
os.environ["RETRIEVER"] = "pfb"

# 注入 pfb 检索层（必须在 import gpt_researcher 之前 patch 模块属性）
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pfb_retriever import install_pfb_retriever
install_pfb_retriever()

from gpt_researcher import GPTResearcher
from s8b_pilot import QUESTIONS

QIDS = ["nat", "soc", "gpu"]
REPS = 3
OUT = "runs-gptr-pfb"
os.makedirs(OUT, exist_ok=True)

OFFICIAL = {
    "temperature": 0.4,
    "max_iterations": 3,
    "max_search_results_per_query": 5,
    "total_words": 1200,
    "max_subtopics": 3,
    "deep_research_breadth": 6,
    "deep_research_depth": 6,
    "deep_research_concurrency": 4,
    "fast_token_limit": 6000,
    "smart_token_limit": 12000,
    "strategic_token_limit": 8000,
}


async def run_one(qid: str, rep: int, query: str):
    tag = f"{qid}-r{rep}"
    t0 = time.time()
    os.environ["PFB_QID"] = qid  # 通道选择按题域（gpu 题启用 local_corpus）
    r = GPTResearcher(query=query, config_path=None)
    for attr in ("smart_llm", "fast_llm", "strategic_llm"):
        setattr(r.cfg, f"{attr}_provider", "openai")
        setattr(r.cfg, f"{attr}_model", "qwen3.8-27b")
    for k, v in OFFICIAL.items():
        setattr(r.cfg, k, v)
    await r.conduct_research()
    report = await r.write_report()
    dt = time.time() - t0
    fp = f"{OUT}/{tag}.md"
    with open(fp, "w") as f:
        f.write(f"# {tag}\n# query: {query[:120]}\n# model=qwen3.8-27b@8787 retriever=pfb(s5-layer)\n")
        f.write(f"# params: {json.dumps(OFFICIAL)}\n# elapsed={dt:.0f}s\n\n{report}\n")
    print(f"[{tag}] done {dt:.0f}s {len(report)} chars -> {fp}", flush=True)
    return {"qid": qid, "rep": rep, "elapsed_s": round(dt, 1), "chars": len(report), "file": fp}


async def main():
    results = []
    if os.path.exists(f"{OUT}/summary.json"):
        try:
            with open(f"{OUT}/summary.json") as f:
                results = json.load(f)
            print(f"[resume] 读回 {len(results)} 条已有结果", flush=True)
        except Exception:
            results = []
    done_set = {(r.get("qid"), r.get("rep")) for r in results if r.get("elapsed_s", -1) > 0}
    for qid in QIDS:
        query = QUESTIONS[qid]
        for rep in range(1, REPS + 1):
            tag = f"{qid}-r{rep}"
            fp = f"{OUT}/{tag}.md"
            if (qid, rep) in done_set or (os.path.exists(fp) and os.path.getsize(fp) > 100):
                print(f"[{tag}] SKIP (已完成，断点续跑)", flush=True)
                continue
            try:
                res = await run_one(qid, rep, query)
                results.append(res)
            except Exception as e:
                print(f"[{tag}] ERROR: {e}\n{traceback.format_exc()}", flush=True)
                results.append({"qid": qid, "rep": rep, "elapsed_s": 0, "chars": 0, "file": fp, "error": str(e)})
            with open(f"{OUT}/summary.json", "w") as f:
                json.dump(results, f, ensure_ascii=False, indent=1)
    print(f"\n=== ALL DONE ({len(results)}/9) ===", flush=True)
    for r in results:
        print(f"  {r['qid']}-r{r['rep']}: {r.get('elapsed_s')}s {r.get('chars')}chars {r.get('error','')}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
