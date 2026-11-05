#!/usr/bin/env python3
"""T35 S8E pilot: embedded verification (single-pass) vs S7V (two-pass).

S8E = S7F prompt + inline claim-verification instruction, single LLM call.
Hypothesis: embedding the verification rule inside the generation prompt
recovers most of S7V's M1 gain without the second API call.

Usage:
    python s8e_pilot.py --qs Q1,Q4 --reps 2
    python s8e_pilot.py --dry-run --qs Q1

Output: runs/S8E-{qid}-r{rep}.json (same schema as ablation_harness)
"""
import argparse, json, os, sys, time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ablation_harness import (
    QUESTIONS, WORKSPACE, PFB, LLM_MODEL, LLM_MAX_TOKENS,
    read_file, extract_question, call_llm, inject_sources_into_prompt,
    research_hook as _hook,
)

RUNS_DIR = os.path.join(PFB, "experiments", "stage-ablation", "runs")

def build_s8e_prompt(question: str, sources: list) -> str:
    """S7F base + embedded claim-verification rules (single pass)."""
    base = (
        "你是一名资深研究员，以严谨和洞察力著称。\n\n"
        f"问题：{question}\n\n"
        "思考方式建议（不是固定流程，按你的判断用）：\n"
        "- 先回到第一性原理：这个问题的底层物理/经济/数学约束是什么？\n"
        "- 把影响因素分解开，哪些是主导项、哪些可以忽略？\n"
        "- 特别注意表面合理但实际有问题的说法——找到矛盾点，重点查证和推理。\n"
        "- 对关键数字，区分「官方标称值」和「实际表现」，合理推测偏差方向和幅度。\n"
        "- 查不到的就明说是缺口，不要编。\n\n"
        "【工具说明】以下是经过筛选的、与问题直接相关的参考来源。"
        "仅当来源内容明确支持你的某个具体断言时才引用它；"
        "如果来源没有直接回答你的子问题，不要强行关联。\n\n"
        "【验证规则 — 写答案的同时执行，不是事后检查】\n"
        "每当你写出一个具体数字（带宽、吞吐量、百分比、价格等），"
        "立即在脑中核对：这个精确数值是否出现在上面的参考来源原文中？\n"
        "- 来源中有明确对应 → 保留，标注「✓ 来源[N]」\n"
        "- 来源中没有 → 改为定性描述（如「显著高于」「约为…量级」），"
        "或标注「✗ 无来源支持，已改为定性」\n"
        "- 你自己知道但来源没覆盖 → 标注「⚠ 模型知识，非来源」\n"
        "不要先写完再回头改——边写边验，一次成型。\n\n"
        "请基于以上来源回答，引用时标注来源编号并写明该来源具体支持了哪个断言。"
        "给出你的最终回答，把你「不确定、需要进一步查证」的点单独列出来。"
    )
    if sources:
        base += "\n\n" + inject_sources_into_prompt("", sources)
    return base


def run_one(arm: str, qid: str, rep: int, dry_run: bool = False) -> dict:
    tag = f"{arm}-{qid}-r{rep}"
    q = QUESTIONS[qid]
    question = extract_question(read_file(q["prompt_file"]))

    print(f"[{tag}] fetching sources...", flush=True)
    t0 = time.time()
    try:
        raw_sources = _hook(qid, question)
        from research_hook import filter_sources
        sources = filter_sources(raw_sources, qid) if raw_sources else []
    except Exception as e:
        print(f"[{tag}] research_hook failed ({e}), using empty sources", flush=True)
        sources = []
    print(f"[{tag}] {len(sources)} filtered sources ({time.time()-t0:.1f}s)", flush=True)

    prompt = build_s8e_prompt(question, sources)
    print(f"[{tag}] prompt={len(prompt)} chars, calling {LLM_MODEL}...", flush=True)

    if dry_run:
        print(f"[{tag}] DRY RUN — skipping LLM call")
        record = {
            "arm": arm, "qid": qid, "rep": rep,
            "model": LLM_MODEL, "params": {"temp": 0.1, "max_tokens": LLM_MAX_TOKENS},
            "output_text": "[DRY RUN]", "sources": sources,
            "wall_s": 0, "tokens": {"in": 0, "out": 0},
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    else:
        t1 = time.time()
        output, tokens = call_llm(prompt, seed=None, temperature=1)
        wall = round(time.time() - t1, 1)
        print(f"[{tag}] done in {wall}s, {tokens['out']} tokens out", flush=True)
        record = {
            "arm": arm, "qid": qid, "rep": rep,
            "model": LLM_MODEL, "params": {"temp": 0.1, "max_tokens": LLM_MAX_TOKENS},
            "output_text": output, "sources": sources,
            "wall_s": wall, "tokens": tokens,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    os.makedirs(RUNS_DIR, exist_ok=True)
    path = os.path.join(RUNS_DIR, f"{tag}.json")
    with open(path, "w") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
    print(f"[{tag}] saved → {path}", flush=True)
    return record


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qs", default="Q1,Q4")
    ap.add_argument("--reps", type=int, default=2)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    qs = [q.strip() for q in args.qs.split(",")]
    total = len(qs) * args.reps
    print(f"S8E pilot: {total} runs ({', '.join(qs)} × {args.reps} reps)")

    for qid in qs:
        for rep in range(1, args.reps + 1):
            run_one("S8E", qid, rep, args.dry_run)

    print("S8E pilot complete.")


if __name__ == "__main__":
    main()