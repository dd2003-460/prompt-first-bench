"""D1-deep baseline: GPT Researcher Deep Research mode (recursive tree).

与 run_d1.py 的区别: report_type="deep" → 递归 breadth×depth 树形展开,
每个节点生成 follow-up questions 再深入。这是 GR 的完整能力, 不是默认的
一次检索+综合。

用法:
  .venv-d1/bin/python run_d1_deep.py --qs Q1 --n 3
环境变量: DEEP_BREADTH (默认4), DEEP_DEPTH (默认2)
"""
import argparse, asyncio, json, os, sys, time
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ablation_harness import QUESTIONS, extract_question, read_file  # noqa: E402

RUNS_DIR = os.environ.get("RUNS_DIR", os.path.join(HERE, "runs"))
MODEL = os.environ.get("D1_MODEL", "qwen3.8-27b")
BASE_URL = os.environ.get("OPENAI_BASE_URL", "http://127.0.0.1:8787/v1")
BREADTH = int(os.environ.get("DEEP_BREADTH", "4"))
DEPTH = int(os.environ.get("DEEP_DEPTH", "2"))


def setup_env():
    os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "sk-local-ninfer")
    os.environ["OPENAI_BASE_URL"] = BASE_URL
    os.environ["FAST_LLM"] = f"openai:{MODEL}"
    os.environ["SMART_LLM"] = f"openai:{MODEL}"
    os.environ["STRATEGIC_LLM"] = f"openai:{MODEL}"
    os.environ["RETRIEVER"] = "duckduckgo"
    os.environ["CONTEXT_FILTER"] = "keyword"
    os.environ["CURATE_SOURCES"] = "False"
    os.environ["ALLOW_PRIVATE_URLS"] = "true"
    os.environ["LANGUAGE"] = "chinese"
    os.environ["TOTAL_WORDS"] = "3000"
    os.environ["DEEP_RESEARCH_BREADTH"] = str(BREADTH)
    os.environ["DEEP_RESEARCH_DEPTH"] = str(DEPTH)
    os.environ["DEEP_RESEARCH_CONCURRENCY"] = "2"


async def run_one(qid: str, rep: int) -> dict:
    from gpt_researcher import GPTResearcher

    q = QUESTIONS[qid]
    question = extract_question(read_file(q["prompt_file"]))
    t0 = time.time()
    researcher = GPTResearcher(query=question, report_type="deep")
    try:
        context = await researcher.conduct_research()
        report = await researcher.write_report()
    finally:
        wall = time.time() - t0
    import re as _re
    sources = []
    for m in _re.finditer(r'https?://[^\s\)\]>"\']+', report or ""):
        u = m.group(0).rstrip(".,")
        if not any(u == s["url"] for s in sources):
            sources.append({"title": "", "url": u})
    return {
        "arm": "D1-deep", "qid": qid, "rep": rep,
        "model": MODEL,
        "params": {
            "retriever": "duckduckgo",
            "system": "gpt-researcher-deep",
            "breadth": BREADTH, "depth": DEPTH,
        },
        "output_text": report or "",
        "sources": sources,
        "wall_s": round(wall, 1),
        "tokens": {},
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qs", default="Q1")
    ap.add_argument("--n", type=int, default=1)
    args = ap.parse_args()
    qs = [x.strip() for x in args.qs.split(",")]
    n_reps = args.n

    setup_env()
    print(f"D1-deep: breadth={BREADTH} depth={DEPTH} model={MODEL}", flush=True)
    for qid in qs:
        for rep in range(1, n_reps + 1):
            out_path = os.path.join(RUNS_DIR, f"D1deep-{qid}-r{rep}.json")
            if os.path.exists(out_path):
                print(f"[skip] {qid} r{rep} exists", flush=True)
                continue
            print(f"[d1-deep] {qid} r{rep}/{n_reps} ...", flush=True)
            try:
                result = await run_one(qid, rep)
            except Exception as e:
                print(f"  ERROR: {str(e)[:300]}", flush=True)
                result = {"arm": "D1-deep", "qid": qid, "rep": rep, "model": MODEL,
                          "output_text": "", "sources": [], "wall_s": 0, "tokens": {},
                          "error": str(e)[:500],
                          "timestamp": datetime.now(timezone.utc).isoformat()}
            with open(out_path, "w") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"  done {qid} r{rep}: {len(result.get('output_text',''))} chars, "
                  f"{len(result.get('sources',[]))} sources, {result.get('wall_s')}s", flush=True)
    print(f"\nAll D1-deep runs written ({len(qs)} × {n_reps}).")


if __name__ == "__main__":
    asyncio.run(main())