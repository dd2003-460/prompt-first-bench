#!/usr/bin/env python3
"""G9 gold 维度集 · 维度间独立性检验（Decision 22 行动项 1 之三）。

背景：U(T)=C·A·S−λ·cost 的 C 项假设 gold 维度集 G 内维度两两正交。
G 不正交 → C 双重计数或漏计 → 乘积语义歪。本脚本做 G 的独立性审计。

判据（Decision 22 补充 2 定稿）：
- 主判据 = LLM-judge 问"能否构造 i 变 j 不变的真实产品/案例"（本体论判断）
  - 能构造（反例存在）→ 独立
  - 不能构造（i 变必牵动 j）→ 相关 → 候选合并
- 层级条件化：同一对维度在不同测量层级可一边独立一边相关
  （容量-带宽：spec 独立、性能耦合）→ 输出按层级标注
- Fisher MI 只当辅助，本脚本不做（LLM 尺子已够）

输入：s8b_pilot.GOLD（每 qid 的 gold 维度文本列表）
输出：g9-independence-{qid}.json + g9-independence.md（合并建议表）

用法: python3 g9_independence.py [--qids gpu,nat,soc] [--workers 3]
"""
import argparse, itertools, json, os, re, sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s8b_pilot import GOLD, QUESTIONS  # noqa: E402
from ablation_harness import call_llm  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

PROMPT = """你是本体论审计员。下面是一道题的两个 gold 评分维度 i 和 j。

题目背景：{question}

维度 i：{dim_i}
维度 j：{dim_j}

任务：判断这两个维度是否【正交】（独立）。判据是本体论的，不是统计的：
问"能否构造一个真实产品/真实案例/真实场景，其中 i 显著变化而 j 基本不变？"
- 能构造（给出具体反例）→ 独立
- 不能构造（i 的变化在物理/经济/逻辑上必然牵动 j）→ 相关

注意：
- 反例必须具体（真实产品名/数字/场景），不接受"理论上可以"
- 相关性可能是层级条件化的：在某个测量层级独立、另一个层级耦合
  （例：容量与带宽在 spec 层独立，在性能层耦合）→ 这种情况标"层级相关"
- 拿不准时往"相关"判（宁合并勿双重计数）

只输出 JSON：
{{"verdict": "独立"|"相关"|"层级相关",
  "counterexample": "具体反例（独立时必填，相关时写 null）",
  "mechanism": "相关机制一句话（相关/层级相关时必填，独立时写 null）",
  "layer": "层级条件化说明（层级相关时必填，否则 null）",
  "confidence": 0.0-1.0}}"""


def robust_parse(out: str):
    """剥 ```json fence + 找完整对象；截断时逐字段救回 verdict。"""
    if not out:
        return None
    t = out.strip()
    t = re.sub(r"^```(?:json)?\s*", "", t)
    t = re.sub(r"\s*```$", "", t)
    m = re.search(r"\{.*\}", t, re.S)
    if m:
        try:
            return json.loads(m.group())
        except Exception:
            pass
    d = {}
    for key in ("verdict", "counterexample", "mechanism", "layer", "confidence"):
        mm = re.search(rf'"{key}"\s*:\s*("(?:[^"\\]|\\.)*"|\d+(?:\.\d+)?|null)', t)
        if mm:
            v = mm.group(1)
            if v == "null":
                d[key] = None
            elif v.startswith('"'):
                try:
                    d[key] = json.loads(v)
                except Exception:
                    d[key] = v.strip('"')
            else:
                d[key] = float(v) if "." in v else int(v)
    return d if d.get("verdict") else None


def check_pair(qid: str, gi: int, di: str, gj: int, dj: str) -> dict:
    q = QUESTIONS.get(qid, "")
    prompt = PROMPT.format(question=q[:800], dim_i=di, dim_j=dj)
    out, _ = call_llm(prompt, max_tokens=2000, temperature=0, retries=2)
    rec = {"i": gi, "j": gj, "dim_i": di[:60], "dim_j": dj[:60]}
    d = robust_parse(out)
    if d:
        rec.update({
            "verdict": d.get("verdict", "未解析"),
            "counterexample": d.get("counterexample"),
            "mechanism": d.get("mechanism"),
            "layer": d.get("layer"),
            "confidence": d.get("confidence"),
        })
    else:
        rec["verdict"] = "未解析"
        rec["raw"] = (out or "")[:300]
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qids", default="gpu,nat,soc")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--rerun-unparsed", action="store_true",
                    help="只重跑已有 JSON 里 verdict==未解析 的对（省 LLM 调用）")
    args = ap.parse_args()
    qids = args.qids.split(",")

    all_results = {}
    for qid in qids:
        if qid not in GOLD:
            print(f"[skip] {qid} 不在 GOLD", file=sys.stderr)
            continue
        dims = GOLD[qid]
        existing_path = os.path.join(HERE, f"g9-independence-{qid}.json")
        existing = {}
        if args.rerun_unparsed and os.path.exists(existing_path):
            ex = json.load(open(existing_path))
            existing = {(p["i"], p["j"]): p for p in ex["pairs"]
                        if p["verdict"] != "未解析"}
            print(f"[{qid}] 复用已解析 {len(existing)} 对", file=sys.stderr)
        pairs = [(i, j) for i, j in itertools.combinations(range(len(dims)), 2)
                 if (i, j) not in existing]
        print(f"[{qid}] 待跑 {len(pairs)} 对", file=sys.stderr)
        from concurrent.futures import ThreadPoolExecutor
        results = list(existing.values())
        if pairs:
            with ThreadPoolExecutor(max_workers=args.workers) as ex:
                futs = {ex.submit(check_pair, qid, i, dims[i], j, dims[j]): (i, j)
                        for i, j in pairs}
                for fut in futs:
                    r = fut.result()
                    results.append(r)
                    print(f"  [{qid}] g{r['i']}-g{r['j']}: {r['verdict']}",
                          file=sys.stderr)
        all_results[qid] = results

    # 落盘
    stamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    for qid, results in all_results.items():
        with open(os.path.join(HERE, f"g9-independence-{qid}.json"), "w") as f:
            json.dump({"qid": qid, "timestamp": stamp,
                       "n_dims": len(GOLD[qid]), "pairs": results},
                      f, ensure_ascii=False, indent=2)

    # 合并建议表
    lines = ["# G9 维度独立性检验", "",
             f"生成: {stamp} | 判据: Decision 22 本体论反例检验", ""]
    for qid, results in all_results.items():
        dims = GOLD[qid]
        lines.append(f"## {qid}（{len(dims)} 维度）")
        lines.append("")
        lines.append("| 对 | 判定 | 反例/机制 | 层级 | conf |")
        lines.append("|---|---|---|---|---|")
        for r in sorted(results, key=lambda x: (x["i"], x["j"])):
            if r["verdict"] == "独立":
                detail = (r.get("counterexample") or "")[:50]
            else:
                detail = (r.get("mechanism") or "")[:50]
            lines.append(
                f"| g{r['i']}×g{r['j']} | {r['verdict']} | {detail} "
                f"| {r.get('layer') or '—'} | {r.get('confidence') or '—'} |")
        # 合并建议
        merge = [r for r in results if r["verdict"] in ("相关", "层级相关")]
        lines.append("")
        if merge:
            lines.append(f"**合并候选（{len(merge)} 对）**：")
            for r in merge:
                lines.append(f"- g{r['i']}×g{r['j']}：{r.get('mechanism')}")
        else:
            lines.append("**无合并候选——G 正交性通过**")
        lines.append("")

    md = "\n".join(lines)
    print(md)
    with open(os.path.join(HERE, "g9-independence.md"), "w") as f:
        f.write(md + "\n")
    print(f"\n[written] g9-independence.md + {len(all_results)} 个 per-qid JSON",
          file=sys.stderr)


if __name__ == "__main__":
    main()
