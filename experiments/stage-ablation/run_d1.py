"""D1 baseline runner: GPT Researcher 端到端跑 Q1-Q5。

配置对齐 S 臂：本地 27b (localhost:8787) + duckduckgo 检索（免 key）。
产出 runs/D1-Q<n>-r<m>.json，字段与 S 臂 run json 同构（output_text/sources/wall_s），
score.py::score_run 可直接评分。

用法:
  .venv-d1/bin/python run_d1.py --qs Q1 --n 3     # 单题 3 rep
  .venv-d1/bin/python run_d1.py --n 3             # 全 5 题 × 3 rep = 15 runs
环境变量覆盖: OPENAI_BASE_URL / D1_MODEL（默认 qwen3.8-27b）
"""
import argparse, asyncio, json, os, sys, time
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ablation_harness import QUESTIONS, extract_question, read_file  # noqa: E402

RUNS_DIR = os.environ.get("RUNS_DIR", os.path.join(HERE, "runs"))
MODEL = os.environ.get("D1_MODEL", "qwen3.8-27b")
BASE_URL = os.environ.get("OPENAI_BASE_URL", "http://127.0.0.1:8787/v1")


def setup_env():
    """GPT Researcher 走 OpenAI-compatible 本地 endpoint + duckduckgo 检索。"""
    os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "sk-local-placeholder")
    os.environ["OPENAI_BASE_URL"] = BASE_URL
    os.environ["FAST_LLM"] = f"openai:{MODEL}"
    os.environ["SMART_LLM"] = f"openai:{MODEL}"
    os.environ["STRATEGIC_LLM"] = f"openai:{MODEL}"
    os.environ["RETRIEVER"] = "duckduckgo"
    os.environ["CONTEXT_FILTER"] = "keyword"
    os.environ["CURATE_SOURCES"] = "False"
    # 本机 DNS 把部分外网域名解析到 198.18.x（代理段），GPT Researcher 的 SSRF 防护会拦掉
    # 这些"非公共地址"；对公开网站放行（只影响 scraper 抓取的 URL 白名单判断）
    os.environ["ALLOW_PRIVATE_URLS"] = "true"
    os.environ["LANGUAGE"] = "chinese"
    os.environ["TOTAL_WORDS"] = "1500"


async def run_one(qid: str, rep: int) -> dict:
    from gpt_researcher import GPTResearcher

    q = QUESTIONS[qid]
    question = extract_question(read_file(q["prompt_file"]))
    t0 = time.time()
    researcher = GPTResearcher(query=question)
    try:
        context = await researcher.conduct_research()
        report = await researcher.write_report()
    finally:
        wall = time.time() - t0
    import re as _re
    sources = []
    for m in _re.finditer(r'https?://[^\s\)\]>"]+', report or ""):
        u = m.group(0).rstrip(".,")
        if not any(u == s["url"] for s in sources):
            sources.append({"title": "", "url": u})
    return {
        "arm": "D1", "qid": qid, "rep": rep,
        "model": MODEL,
        "params": {"retriever": "duckduckgo", "system": "gpt-researcher-default-pipeline"},
        "output_text": report or "",
        "sources": sources,
        "wall_s": round(wall, 1),
        "tokens": {},
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qs", default="Q1,Q2,Q3,Q4,Q5")
    args = ap.parse_args()
    qs = [x.strip() for x in args.qs.split(",")]

    setup_env()
    for qid in qs:
        out_path = os.path.join(RUNS_DIR, f"D1-{qid}.json")
        if os.path.exists(out_path):
            print(f"[skip] {qid} exists", flush=True)
            continue
        print(f"[d1] {qid} ...", flush=True)
        try:
            result = await run_one(qid)
        except Exception as e:
            print(f"  ERROR: {str(e)[:200]}", flush=True)
            result = {"arm": "D1", "qid": qid, "rep": rep, "model": MODEL,
                      "output_text": "", "sources": [], "wall_s": 0, "tokens": {},
                      "error": str(e)[:500],
                      "timestamp": datetime.now(timezone.utc).isoformat()}
        with open(out_path, "w") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"  done {result['qid']}: {len(result.get('output_text',''))} chars, "
              f"{len(result.get('sources',[]))} sources, {result.get('wall_s')}s", flush=True)
    print("\nAll D1 runs written.")


if __name__ == "__main__":
    asyncio.run(main())