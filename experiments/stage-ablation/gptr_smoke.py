#!/usr/bin/env python3
"""GPT-Researcher smoke test: point at local Qwen3-27B @8787, run one bench question."""
import asyncio, os, sys, time

os.environ["OPENAI_API_KEY"] = "local-not-needed"
os.environ["OPENAI_BASE_URL"] = "http://127.0.0.1:8787/v1"
# free retrievers only (no paid API keys)
os.environ["RETRIEVER"] = "arxiv"

from gpt_researcher import GPTResearcher
from gpt_researcher.config import Config


async def main():
    query = "What is the TDP (thermal design power) of the NVIDIA H200 GPU in watts, and how does it compare to the H100 SXM?"
    t0 = time.time()
    r = GPTResearcher(query=query, config_path=None)
    # patch instance cfg after construction (agent builds its own Config)
    for attr in ("smart_llm", "fast_llm", "strategic_llm"):
        setattr(r.cfg, f"{attr}_provider", "openai")
        setattr(r.cfg, f"{attr}_model", "qwen3.8-27b")
    await r.conduct_research()
    report = await r.write_report()
    dt = time.time() - t0
    print(f"\n=== REPORT ({dt:.0f}s) ===")
    print(report[:3000])
    # save full
    with open("archive/root-runs/runs-s5-sm-gpu/gptr-smoke-h200.md", "w") as f:
        f.write(f"# GPT-Researcher smoke: H200 TDP\n# model=qwen3.8-27b@8787 elapsed={dt:.0f}s\n\n{report}\n")
    print("\n[saved] runs-s5-sm-gpu/gptr-smoke-h200.md")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        import traceback; traceback.print_exc()
        sys.exit(1)