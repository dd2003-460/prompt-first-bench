#!/usr/bin/env python3
"""S8G pilot: S5 全流程 prompt + P1 patch (A1/A2/A3) — v3 gold-gap 任务卡.

S8G = build_prompt("S5", qid) + 三条通用质量规则（维度完备性/空缺强制/交叉验证口径）。
规则文本见 arms_new/S8G-p1-patch.md；措辞为通用原则，不含 gold 维度名或结构。

用法:
    python s8g_pilot.py --qs Q5 --reps 1              # 带 research hook（S5 同款）
    python s8g_pilot.py --qs Q5 --reps 1 --no-hook    # 纯 prompt 效果测试
    python s8g_pilot.py --qs Q5 --dry-run

输出: runs-r293/S8G-{qid}-r{rep}.json（schema 与 ablation_harness run 文件一致）
"""
import argparse, json, os, sys, time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ablation_harness import (
    QUESTIONS, LLM_MODEL, LLM_MAX_TOKENS,
    read_file, extract_question, call_llm, inject_sources_into_prompt,
    build_prompt, research_hook as _hook,
)

RUNS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "runs-r293")

# ── P1 patch：三条通用规则（无答案泄漏——不引用任何 gold 维度名/结构）──────
P1_PATCH = """
【补充质量规则 — 在给出最终回答前必须逐条执行】

规则 A1 — 维度完备性检查（分解树前置）：
在做分解树之前，先列出该问题域标准理论框架中的全部候选维度类别
（例如：决策论的损失分解、贝叶斯更新的误差来源分类、成本-收益-风险三分等，
按问题域选择对应框架），然后逐项核对「我的分解树是否覆盖了每一类」。
缺失的类别必须补入，或显式说明为何在该场景不适用。禁止自由发挥维度集。

规则 A2 — 空缺强制 + 数值断言二选一：
- 场景中未给定数值的参数，必须列入「空缺清单」并标注「需实测 / 需外部数据」，
  禁止填入默认值或估计值。
- 每个数值断言必须满足二选一：
  (a) 给出可定位的真实来源 URL；
  (b) 显式标注「理论推导，无实测依据」。
- 两者都不满足的数值断言必须删除，或降级为定性描述。

规则 A3 — 交叉验证口径：
声称「两个独立来源一致」时，两个来源必须来自不同知识类型
（如：理论推导 vs 模拟结果；文献 A vs 文献 B 且主题角度不同）。
同一文档的不同章节不算两个来源。

规则 A4 — 检索结果引用强制：
如果本题提供了外部检索结果 (research digest), 你必须在输出的「来源」或「参考文献」章节中逐条列出实际使用的来源 (标题 + URL), 并在正文相应断言处标注 [S1][S2]... 对应编号。检索结果中的每一条都必须被显式处理: 要么被引用, 要么说明为何不采用。未提供检索结果时, 此规则不适用, 所有数值断言按 A2 处理。
"""


def build_s8g_prompt(qid, question, sources=None):
    """S5 全流程 prompt + P1 patch（插在阶段 04.5 之后、【待解问题】之前）。"""
    base = build_prompt("S5", qid)
    marker = "\n【待解问题】\n"
    idx = base.find(marker)
    if idx >= 0:
        patched = base[:idx] + P1_PATCH + base[idx:]
    else:
        patched = base + P1_PATCH
    if sources:
        patched = inject_sources_into_prompt(patched, sources)
    return patched


def run_one(qid, rep, dry_run=False, use_hook=True):
    tag = f"S8G-{qid}-r{rep}"
    q = QUESTIONS[qid]
    question = extract_question(read_file(q["prompt_file"]))

    sources = []
    if use_hook and not dry_run:
        search_q = q.get("search_query") or question
        print(f"[{tag}] running research_hook...", flush=True)
        t_r = time.time()
        try:
            sources = _hook(qid, search_q)
            from research_hook import filter_sources
            n_raw = len(sources)
            sources = filter_sources(sources, qid)
            print(f"[{tag}] research done in {time.time()-t_r:.1f}s: {n_raw} raw → {len(sources)} filtered", flush=True)
        except Exception as e:
            print(f"[{tag}] research_hook failed ({e}), continuing with empty sources", file=sys.stderr)
            sources = []

    prompt = build_s8g_prompt(qid, question, sources)
    print(f"[{tag}] prompt={len(prompt)} chars, calling {LLM_MODEL}...", flush=True)

    record = {
        "arm": "S8G", "qid": qid, "rep": rep,
        "model": LLM_MODEL, "params": {"temp": 0, "max_tokens": LLM_MAX_TOKENS},
        "output_text": "", "sources": sources,
        "wall_s": 0, "tokens": {"in": 0, "out": 0},
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    if dry_run:
        print(f"[{tag}] DRY RUN — prompt head:\n{prompt[:400]}...")
        return record

    t0 = time.time()
    output, tokens = call_llm(prompt, seed=None, temperature=0)
    wall = round(time.time() - t0, 1)
    print(f"[{tag}] done in {wall}s, {tokens['out']} tokens out", flush=True)
    record.update({"output_text": output, "wall_s": wall, "tokens": tokens})

    os.makedirs(RUNS_DIR, exist_ok=True)
    path = os.path.join(RUNS_DIR, f"{tag}.json")
    with open(path, "w") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
    print(f"[{tag}] saved → {path}", flush=True)
    return record


def main():
    ap = argparse.ArgumentParser(description="S8G pilot (S5 + P1 patch)")
    ap.add_argument("--qs", default="Q5", help="comma-separated: Q1,Q4,Q5")
    ap.add_argument("--reps", type=int, default=1)
    ap.add_argument("--rep", type=int, default=None, help="run only this specific rep")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-hook", action="store_true", help="skip research hook (pure prompt test)")
    args = ap.parse_args()

    qs = [q.strip().upper() for q in args.qs.split(",")]
    reps = [args.rep] if args.rep else list(range(1, args.reps + 1))
    print(f"S8G pilot: {len(qs)} questions × {len(reps)} reps, hook={'off' if args.no_hook else 'on'}")
    for qid in qs:
        for rep in reps:
            run_one(qid, rep, dry_run=args.dry_run, use_hook=not args.no_hook)
    print("S8G pilot complete.")


if __name__ == "__main__":
    main()