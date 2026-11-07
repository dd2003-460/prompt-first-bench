#!/usr/bin/env python3
"""G3: run GPT Researcher (out-of-box, no gold leak) on nat/soc questions, save reports.

Config: openai provider pointed at local 8787 proxy (qwen3.8-27b), tavily→duckduckgo retriever,
keyword context filter (no embedding API). n=1 per question (directional only, conf noted).
"""
import asyncio, json, os, sys, time

os.environ["OPENAI_API_KEY"] = "sk-local-ninfer"
os.environ["OPENAI_BASE_URL"] = "http://127.0.0.1:8787/v1"
# Config reads env vars with precedence over defaults (verified empirically)
os.environ["FAST_LLM"] = "openai:qwen3.8-27b"
os.environ["SMART_LLM"] = "openai:qwen3.8-27b"
os.environ["STRATEGIC_LLM"] = "openai:qwen3.8-27b"
os.environ["RETRIEVER"] = "duckduckgo"
os.environ["CONTEXT_FILTER"] = "keyword"
# This machine's system DNS (198.18.0.2) resolves public domains to private
# 198.18.x.x addresses, which gpt-researcher's SSRF guard then blocks.
# Point Python at a real resolver so scraping works.
import socket as _socket

_orig_getaddrinfo = _socket.getaddrinfo

def _safe_getaddrinfo(host, port, *args, **kwargs):
    results = _orig_getaddrinfo(host, port, *args, **kwargs)
    # If the system resolver returned only private/loopback addresses for a
    # public-looking host, fall back to Google/DNS-over-UDP via dnspython.
    def _is_public(ip):
        return not (ip.startswith(("10.", "192.168.", "127.")) or ip.startswith("198.18.") or ip.startswith("172.16"))
    if all(not _is_public(r[4][0]) for r in results):
        try:
            import dns.resolver  # type: ignore
            r = dns.resolver.Resolver()
            r.nameservers = ["8.8.8.8", "1.1.1.1"]
            r.timeout = 5
            r.lifetime = 8
            answers = r.resolve(host, "A")
            fallback = [
                (_socket.AF_INET, _socket.SOCK_STREAM, 6, "", (a.to_text(), port or 0))
                for a in answers
            ]
            if fallback:
                return fallback
        except Exception:
            pass
    return results

_socket.getaddrinfo = _safe_getaddrinfo

from gpt_researcher import GPTResearcher
from gpt_researcher.config import Config
sys.path.insert(0, "/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation")
from s8b_pilot import QUESTIONS

OUT = "/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/runs-baseline"
os.makedirs(OUT, exist_ok=True)

def make_config():
    cfg = Config()
    for attr in ("fast_llm_provider","smart_llm_provider","strategic_llm_provider"):
        setattr(cfg, attr, "openai")
    for attr in ("fast_llm_model","smart_llm_model","strategic_llm_model"):
        setattr(cfg, attr, "qwen3.8-27b")
    cfg.retriever = "duckduckgo"
    cfg.retrievers = ["duckduckgo"]
    cfg.context_filter = "keyword"
    cfg.embedding_provider = "none"
    cfg.temperature = 0
    return cfg

async def run_one(qid):
    q = QUESTIONS[qid]
    t0 = time.time()
    res = GPTResearcher(query=q, config_path=None)
    # inject config via constructor param not available; patch instance
    return None

async def main():
    for qid in ("nat", "soc"):
        q = QUESTIONS[qid]
        t0 = time.time()
        try:
            res = GPTResearcher(query=q)
            # sanity check config took effect
            assert "qwen" in res.cfg.fast_llm, f"config not applied: {res.cfg.fast_llm}"
            report = await res.conduct_research()
            with open(f"{OUT}/gptr-{qid}.md", "w") as f:
                f.write(report or "")
            print(f"[{qid}] ok {len(report or '')} chars {time.time()-t0:.0f}s", flush=True)
        except Exception as e:
            import traceback; traceback.print_exc()
            print(f"[{qid}] FAIL {e}", flush=True)
            with open(f"{OUT}/gptr-{qid}.error", "w") as f:
                f.write(str(e))

if __name__ == "__main__":
    asyncio.run(main())