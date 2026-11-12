"""T53 DRB n=10 subset: run GPT-Researcher on official DRB questions.

These 10 questions have reference articles + criteria in /tmp/drbench,
so results can be scored with the official RACE protocol and compared
directly to Claude-3.7-Sonnet (RACE Overall = 0.4218, 100-question mean).
"""
import asyncio, json, os, sys, time, traceback

os.environ["OPENAI_API_KEY"] = "local-not-needed"
os.environ["OPENAI_BASE_URL"] = "http://127.0.0.1:8787/v1"
os.environ["RETRIEVER"] = "arxiv"
os.environ["LANGCHAIN_OPENAI_STREAM_CHUNK_TIMEOUT_S"] = "600"

from gpt_researcher import GPTResearcher

DRB_DIR = "/tmp/drbench"
OUT = "archive/root-runs/runs-s5-sm-gpu/gptr-drb10"

# Our selected n=10 survey-type subset
OUR_IDS = [1, 2, 16, 41, 50, 52, 57, 62, 67, 78]


def load_queries():
    qs = {}
    with open(f"{DRB_DIR}/data/prompt_data/query.jsonl") as f:
        for line in f:
            q = json.loads(line)
            if q["id"] in OUR_IDS:
                qs[q["id"]] = q["prompt"]
    return qs


async def run_one(qid, query):
    t0 = time.time()
    r = GPTResearcher(query=query, config_path=None)
    for attr in ("smart_llm", "fast_llm", "strategic_llm"):
        setattr(r.cfg, f"{attr}_provider", "openai")
        setattr(r.cfg, f"{attr}_model", "qwen3.8-27b")
    await r.conduct_research()
    report = await r.write_report()
    elapsed = time.time() - t0
    path = f"{OUT}/drb-{qid}.md"
    with open(path, "w") as f:
        f.write(report)
    print(f"[{qid}] done in {elapsed:.0f}s, {len(report)} chars -> {path}", flush=True)
    return {"id": qid, "chars": len(report), "time_s": round(elapsed, 1)}


async def main():
    os.makedirs(OUT, exist_ok=True)
    queries = load_queries()
    print(f"Running {len(queries)} DRB questions via GPT-Researcher (local 27B + arxiv)", flush=True)
    results = []
    for qid in sorted(queries.keys()):
        try:
            res = await run_one(qid, queries[qid])
            results.append(res)
        except Exception as e:
            print(f"[{qid}] FAILED: {e}", flush=True)
            traceback.print_exc()
            results.append({"id": qid, "error": str(e)})
    # Save summary
    with open(f"{OUT}/summary.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nALL_DONE exit=0, {len(results)} questions", flush=True)


if __name__ == "__main__":
    asyncio.run(main())