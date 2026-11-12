#!/usr/bin/env python3
"""DRB pilot 判分器：官方 criteria.jsonl 逐条 0/1 + dimension_weight 加权。

对齐 Lead L2 指令：DRB 打分必须对齐官方四维 judge（comprehensiveness / insight /
instruction_following / readability），不用我们自己的 gold 量表。
criteria 来自 /tmp/drbench/data/criteria_data/criteria.jsonl（DRB 仓库自带，每 id 一条）。

用法:
    python drb_judge.py --qid 1 --answer runs-s5-sm-drb-1.md
    python drb_judge.py --qid 1,2,16            # 批量（答案文件按约定名找）

输出: drb-pilot/judgments/drb-{id}.json — 每条 criterion 的 0/1 + reason + 维度分 + 总分。
judge = 本地 qwen3.8-27b（同族，仅相对有效；绝对值需 GPT-5.5 复核，见 drb_race_judge.py）。
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, ".."))  # ablation_harness 在上级目录
from ablation_harness import call_llm

CRITERIA_PATH = "/tmp/drbench/data/criteria_data/criteria.jsonl"
JUDGMENTS_DIR = os.path.join(HERE, "judgments")


def load_criteria(qid: int) -> dict:
    with open(CRITERIA_PATH) as f:
        for line in f:
            d = json.loads(line)
            if d.get("id") == qid:
                return d
    raise SystemExit(f"criteria not found for qid={qid}")


def judge_one(qid: int, answer: str) -> dict:
    crit = load_criteria(qid)
    blocks, idx_map = [], []
    i = 0
    for dim, items in (crit.get("criterions") or {}).items():
        for c in items:
            i += 1
            idx_map.append((i, dim))
            blocks.append(f"[{i}] ({dim}) {c.get('criterion','')}\n    说明: {c.get('explanation','')}")
    points = "\n".join(blocks)
    jp = (
        "你是评分员。下面是一道深度研究题的官方评分标准（逐条 criterion）和一份候选研究报告。\n"
        "对每条 criterion 判断候选报告是否实质满足（满足=1，未满足或答错=0；部分满足按 0 计并在 reason 说明）。\n\n"
        f"【评分标准】\n{points}\n\n"
        f"【候选报告】\n{answer[:24000]}\n\n"
        f'输出 JSON：{{"scores": [每条 0/1，共 {len(idx_map)} 条], '
        '"reasons": [每条一句话理由]}}'
    )
    content, _ = call_llm(jp, max_tokens=4096, temperature=0)
    m = re.search(r"\{.*\}", content, re.S)
    try:
        d = json.loads(m.group(0)) if m else {}
    except json.JSONDecodeError:
        d = {"parse_error": content[:500]}
    scores = d.get("scores") or []
    reasons = d.get("reasons") or []
    # 按维度聚合
    dim_scores, dim_total = {}, {}
    for n, (idx, dim) in enumerate(idx_map):
        dim_total[dim] = dim_total.get(dim, 0) + 1
        dim_scores[dim] = dim_scores.get(dim, 0) + (1 if n < len(scores) and scores[n] == 1 else 0)
    weights = crit.get("dimension_weight") or {}
    dim_frac = {dim: dim_scores.get(dim, 0) / tot for dim, tot in dim_total.items()}
    total = sum(weights.get(dim, 0) * frac for dim, frac in dim_frac.items())
    return {
        "qid": qid,
        "total": round(total, 4),
        "dimension_weights": weights,
        "dimension_coverage": {dim: round(v, 4) for dim, v in dim_frac.items()},
        "per_criterion": [
            {"idx": idx, "dim": dim, "score": (1 if n < len(scores) and scores[n] == 1 else 0),
             "reason": reasons[n] if n < len(reasons) else ""}
            for n, (idx, dim) in enumerate(idx_map)
        ],
        "raw": d.get("parse_error"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qid", required=True, help="逗号分隔的 DRB id")
    ap.add_argument("--answer-dir", default=os.path.join(HERE, "..", "..", "..", "archive", "root-runs", "runs-s5-sm-gpu"))
    args = ap.parse_args()
    os.makedirs(JUDGMENTS_DIR, exist_ok=True)
    for qid_s in args.qid.split(","):
        qid = int(qid_s)
        afile = os.path.join(args.answer_dir, f"gptr-bench", f"drb-{qid}.md") \
            if os.path.exists(os.path.join(args.answer_dir, "gptr-bench", f"drb-{qid}.md")) \
            else os.path.join(args.answer_dir, f"drb-{qid}.md")
        if not os.path.exists(afile):
            print(f"[judge] skip qid={qid}: no answer file at {afile}", flush=True)
            continue
        answer = open(afile).read()
        res = judge_one(qid, answer)
        out = os.path.join(JUDGMENTS_DIR, f"drb-{qid}.json")
        with open(out, "w") as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
        dims = " ".join(f"{k}={v:.2f}" for k, v in res["dimension_coverage"].items())
        print(f"[judge] qid={qid} total={res['total']:.3f} | {dims} → {out}", flush=True)


if __name__ == "__main__":
    main()