#!/usr/bin/env python3
"""T53 SOTA baseline: run all 5 bench questions through GPT-Researcher.

Local Qwen3-27B @8787 + arxiv retriever (ddg/mojeek unreachable from this network,
verified). Serial execution — single local GPU, concurrency would contend for VRAM.
Each question gets its own .md report + console log under runs-s5-sm-gpu/gptr-bench/.
"""
import asyncio, os, sys, time, traceback

os.environ["OPENAI_API_KEY"] = "local-not-needed"
os.environ["OPENAI_BASE_URL"] = "http://127.0.0.1:8787/v1"
os.environ["RETRIEVER"] = "arxiv"

from gpt_researcher import GPTResearcher

QUESTIONS = [
    ("Q1", "What is the TDP (thermal design power) of the NVIDIA H200 GPU in watts, and how does it compare to the H100 SXM?"),
    ("Q2", "How many attention heads did the original Transformer paper (Attention Is All You Need, 2017) use in its base and big models, and how does that compare to GPT-3's 175B model head count?"),
    ("Q3", "How many annotated question-answer pairs does the HotpotQA dataset contain, and what percentage are compositional (multi-hop) questions?"),
    ("Q4", "How many parameters does LLaMA 2 70B have, and how many tokens was it trained on?"),
    ("Q5", "For DeepSeek-V3, what are the total parameter count, the active parameter count per token, and the ratio between them?"),
]

OUT = "archive/root-runs/runs-s5-sm-gpu/gptr-bench"


async def run_one(qid, query):
    t0 = time.time()
    r = GPTResearcher(query=query, config_path=None)
    for attr in ("smart_llm", "fast_llm", "strategic_llm"):
        setattr(r.cfg, f"{attr}_provider", "openai")
        setattr(r.cfg, f"{attr}_model", "qwen3.8-27b")
    await r.conduct_research()
    report = await r.write_report()
    dt = time.time() - t0
    os.makedirs(OUT, exist_ok=True)
    with open(f"{OUT}/{qid}.md", "w") as f:
        f.write(f"# {qid}\n# query: {query}\n# model=qwen3.8-27b@8787 retriever=arxiv elapsed={dt:.0f}s\n\n{report}\n")
    print(f"[{qid}] done in {dt:.0f}s, {len(report)} chars", flush=True)
    return qid, dt, len(report)


async def main():
    results = []
    for qid, query in QUESTIONS:
        try:
            results.append(await run_one(qid, query))
        except Exception as e:
            traceback.print_exc()
            print(f"[{qid}] FAILED: {e}", flush=True)
            results.append((qid, -1, 0))
    # summary
    with open(f"{OUT}/summary.json", "w") as f:
        import json
        json.dump([{"qid": q, "elapsed_s": d, "chars": c} for q, d, c in results], f, indent=2)
    print("\n=== ALL DONE ===")
    for q, d, c in results:
        print(f"  {q}: {d:.0f}s / {c} chars" if d > 0 else f"  {q}: FAILED")


if __name__ == "__main__":
    asyncio.run(main())