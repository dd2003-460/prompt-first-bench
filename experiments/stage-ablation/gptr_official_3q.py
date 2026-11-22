#!/usr/bin/env python3
"""GPT-Researcher 三题 × 3 rep，官方默认参数（v0.16.1）。

三题来源：s8b_pilot.py QUESTIONS（nat/soc/gpu）
官方参数来源：gpt_researcher 0.16.1 默认值（.venv-d1 环境）
  temperature=0.4, max_iterations=3, max_search_results=5,
  total_words=1200, max_subtopics=3, deep_research_breadth=3,
  deep_research_depth=2, deep_research_concurrency=4
  fast_token_limit=6000, smart_token_limit=12000, strategic_token_limit=8000
retriever=arxiv（ddg/mojeek 网络不通，已验证）
model=qwen3.8-27b @ 127.0.0.1:8787
"""
import asyncio, os, sys, time, json, traceback

os.environ["OPENAI_API_KEY"] = "local-not-needed"
os.environ["OPENAI_BASE_URL"] = "http://127.0.0.1:8787/v1"
os.environ["RETRIEVER"] = "arxiv"

from gpt_researcher import GPTResearcher
from s8b_pilot import QUESTIONS

QIDS = ["nat", "soc", "gpu"]
REPS = 3
OUT = "runs-gptr-official"
os.makedirs(OUT, exist_ok=True)

# 官方默认参数（gpt_researcher v0.16.1）+ 深度研究加宽加深（D 2026-11-18：
# 官方默认 depth=2/breadth=3 不是深度研究的最好 baseline，加到 6/6）
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
        f.write(f"# {tag}\n# query: {query[:120]}\n# model=qwen3.8-27b@8787 retriever=arxiv\n")
        f.write(f"# params: {json.dumps(OFFICIAL)}\n# elapsed={dt:.0f}s\n\n{report}\n")
    print(f"[{tag}] done {dt:.0f}s {len(report)} chars -> {fp}", flush=True)
    return {"qid": qid, "rep": rep, "elapsed_s": round(dt, 1), "chars": len(report), "file": fp}


async def main():
    results = []
    # 断点续跑：读已有 summary.json（崩溃后重启跳过已完成的）
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
            # 断点续跑：.md 文件已存在且非空 → 跳过（不依赖 summary.json，更稳）
            if (qid, rep) in done_set or (os.path.exists(fp) and os.path.getsize(fp) > 100):
                print(f"[{tag}] SKIP (已完成，断点续跑)", flush=True)
                if os.path.exists(fp) and (qid, rep) not in done_set:
                    results.append({"qid": qid, "rep": rep, "elapsed_s": -2, "chars": os.path.getsize(fp), "file": fp, "note": "resumed-skip"})
                continue
            try:
                r = await run_one(qid, rep, query)
                results.append(r)
                # 每个 run 完成后立即写 summary.json（断点，崩溃不丢进度）
                with open(f"{OUT}/summary.json", "w") as f:
                    json.dump(results, f, indent=2, ensure_ascii=False)
            except Exception as e:
                traceback.print_exc()
                print(f"[{tag}] FAILED: {e}", flush=True)
                results.append({"qid": qid, "rep": rep, "elapsed_s": -1, "chars": 0, "file": "", "error": str(e)})
    with open(f"{OUT}/summary.json", "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n=== ALL DONE ({len(results)} runs) ===", flush=True)
    for r in results:
        if r["elapsed_s"] > 0:
            print(f"  {r['qid']}-r{r['rep']}: {r['elapsed_s']}s / {r['chars']} chars", flush=True)
        else:
            print(f"  {r['qid']}-r{r['rep']}: FAILED ({r.get('error','')[:80]})", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
