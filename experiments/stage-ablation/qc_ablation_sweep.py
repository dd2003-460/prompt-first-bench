#!/usr/bin/env python3
"""Prompt 组合消融遍历脚本。

按 ablation-matrix.md 定义的 10 个臂 × 3 道题遍历，每臂每题 1 rep。
每步结果落盘到 step-log/，最终汇总到 summary.md。

用法:
    python3 qc_ablation_sweep.py --arms A0,A6,A7 --qs nat,soc,gpu --reps 1
    python3 qc_ablation_sweep.py --arms all --qs gpu --reps 1  # 冒烟
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from ablation_harness import call_llm, LLM_MODEL
from s8b_pilot import QUESTIONS, judge
from judge_v2_depth import score_run

# ── 臂定义 ──────────────────────────────────────────────────────────
ARMS = {
    "A0": {"d2": "baseline", "d3": "baseline", "d4": "none",    "d5": "off"},
    "A1": {"d2": "no_challenge", "d3": "baseline", "d4": "none", "d5": "off"},
    "A2": {"d2": "baseline", "d3": "simple", "d4": "none",    "d5": "off"},
    "A3": {"d2": "no_challenge", "d3": "simple", "d4": "none", "d5": "off"},
    "A4": {"d2": "baseline", "d3": "baseline", "d4": "Q2_only", "d5": "off"},
    "A5": {"d2": "baseline", "d3": "baseline", "d4": "Q4_only", "d5": "off"},
    "A6": {"d2": "baseline", "d3": "baseline", "d4": "Q2+Q4",  "d5": "off"},
    "A7": {"d2": "baseline", "d3": "baseline", "d4": "Q2+Q4",  "d5": "on"},
    "A8": {"d2": "no_challenge", "d3": "simple", "d4": "Q2+Q4", "d5": "on"},
    "A9": {"d2": "baseline", "d3": "baseline", "d4": "none",    "d5": "on"},
    # 补全二阶交互角点（ablation-matrix-full.md §2：D2×D4/D2×D5/D3×D4/D3×D5）
    "A10": {"d2": "no_challenge", "d3": "baseline", "d4": "Q2+Q4", "d5": "off"},
    "A11": {"d2": "no_challenge", "d3": "baseline", "d4": "none",   "d5": "on"},
    "A12": {"d2": "baseline", "d3": "simple", "d4": "Q2+Q4", "d5": "off"},
    "A13": {"d2": "baseline", "d3": "simple", "d4": "none",   "d5": "on"},
}


def load_prompt(name: str) -> str:
    """从 prompts/ 目录加载 MD 版本 prompt。"""
    path = HERE / "prompts" / f"{name}.md"
    if not path.exists():
        raise FileNotFoundError(f"prompt file not found: {path}")
    return path.read_text(encoding="utf-8")


def run_arm(arm: str, qid: str, rep: int, out_dir: Path) -> dict:
    """跑一个臂 × 一道题 × 1 rep。返回结果 dict。"""
    try:
        return _run_arm_inner(arm, qid, rep, out_dir)
    except Exception as e:
        import traceback
        tag = f"{arm}-{qid}-r{rep}"
        err_result = {
            "tag": tag, "arm": arm, "qid": qid, "rep": rep,
            "error": f"{type(e).__name__}: {e}",
            "traceback": traceback.format_exc()[-500:],
        }
        out_path = out_dir / f"{tag}.json"
        out_path.write_text(json.dumps(err_result, ensure_ascii=False, indent=1))
        print(f"  [{tag}] FAILED: {e}", flush=True)
        return err_result


def _run_arm_inner(arm: str, qid: str, rep: int, out_dir: Path) -> dict:
    """实际执行逻辑（被 run_arm 的 try/except 包裹）。"""
    cfg = ARMS[arm]
    tag = f"{arm}-{qid}-r{rep}"
    out_path = out_dir / f"{tag}.json"
    step_log = out_dir / "step-log" / f"{arm}-{qid}.jsonl"

    if out_path.exists():
        print(f"  [{tag}] cached, skipping")
        return json.loads(out_path.read_text())

    question = QUESTIONS[qid]
    t0 = time.time()
    result = {
        "tag": tag, "arm": arm, "qid": qid, "rep": rep,
        "model": LLM_MODEL, "ts": datetime.now(timezone.utc).isoformat(),
        "config": cfg,
    }

    def log_step(step: str, data: dict):
        """逐步日志：每步一行 JSON。"""
        entry = {"step": step, "ts": datetime.now(timezone.utc).isoformat(), **data}
        with open(step_log, "a") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        print(f"    [{tag}] {step}: {json.dumps(data, ensure_ascii=False)[:120]}", flush=True)

    # ── Step 1: 分解（用 P1H_INDEX 逐层分解，简化版：一次性 decompose）──
    log_step("decompose_start", {"question_len": len(question)})
    from s5_pipeline import decompose, _extract_json, _perturb
    nodes, raw = decompose(question)
    log_step("decompose_done", {
        "n_nodes": len(nodes),
        "levels": {str(n.get("level", "?")): sum(1 for x in nodes if x.get("level") == str(n.get("level", "?"))) for n in nodes},
    })
    if not nodes:
        result["error"] = "decompose returned no nodes"
        result["wall_s"] = round(time.time() - t0, 1)
        out_path.write_text(json.dumps(result, ensure_ascii=False, indent=1))
        return result

    # ── Step 2: 质检门（D4）──
    if cfg["d4"] != "none":
        from s5_state_machine import _ngram_overlap, marginal_gain
        # Q2: 正交性（简化版：n-gram 重叠 > 0.5 的丢弃，不调 LLM）
        if "Q2" in cfg["d4"]:
            n_orth = 0
            kept = []
            for i, n in enumerate(nodes):
                is_dup = any(
                    _ngram_overlap(n["claim"], m["claim"]) > 0.5
                    for m in kept
                )
                if is_dup:
                    n_orth += 1
                else:
                    kept.append(n)
            nodes = kept
            log_step("Q2_orthogonality", {"n_dropped": n_orth, "n_kept": len(nodes)})

        # Q4: 可压缩复杂度（简化版：marginal_gain < 0.3 的丢弃）
        if "Q4" in cfg["d4"]:
            n_comp = 0
            kept = []
            for n in nodes:
                # 简化：对 L1 节点，算其子节点（如果有）的 marginal_gain
                # 这里简化为：claim 与已有节点的平均 n-gram 重叠 > 0.7 → 丢弃
                if kept:
                    avg_sim = sum(_ngram_overlap(n["claim"], k["claim"]) for k in kept) / len(kept)
                    if avg_sim > 0.7:
                        n_comp += 1
                        continue
                kept.append(n)
            nodes = kept
            log_step("Q4_compression", {"n_dropped": n_comp, "n_kept": len(nodes)})

    # ── Step 3: 核验（D2: baseline vs no_challenge）──
    # no_challenge 臂真正去掉反方质询（verify_node_nc 用 P3_VERIFY_NC，
    # 与 verify_node 唯一差异是删掉第一步质询，其余判定逻辑一致 → 单变量对照）。
    # 修复 2026-11-18：旧版两分支都调 verify_node（带质询），D2 主效应恒为 0（假阴性）。
    from s5_pipeline import search_node, verify_node, verify_node_nc
    facts = []
    for node in nodes[:20]:  # 限制 20 节点控制 wall time
        node_rec = {"id": node["id"], "claim": node["claim"],
                    "level": node.get("level", "?"),
                    "source": node.get("source", "search"),
                    "search_query": node.get("search_query", "")}
        if node.get("source") in ("given", "knowledge"):
            node_rec.update(status="verified", evidence="模型先验/题面给定",
                            corrected_claim=node["claim"])
            facts.append(node_rec)
            continue
        srcs, err = search_node(node, qid=qid)
        if err:
            node_rec.update(status="degraded", evidence=f"检索失败: {err}",
                            corrected_claim=node["claim"])
        else:
            if cfg["d2"] == "no_challenge":
                status, evidence, corrected, raw_v = verify_node_nc(node, srcs)
            else:
                status, evidence, corrected, raw_v = verify_node(node, srcs)
            node_rec.update(status=status, evidence=evidence,
                            corrected_claim=corrected or node["claim"])
        facts.append(node_rec)

    n_verified = sum(1 for f in facts if f["status"] == "verified")
    log_step("verify_done", {
        "n_facts": len(facts), "n_verified": n_verified,
        "verified_rate": round(n_verified / max(len(facts), 1), 3),
    })

    # ── Step 4: 矛盾扫描（D5）──
    if cfg["d5"] == "on":
        ver = [f for f in facts if f["status"] == "verified"]
        if len(ver) >= 4:
            block = "\n".join(f"{f['id']}: {f['corrected_claim'][:120]}" for f in ver[:30])
            prompt = (
                "下面是一棵研究分解树里已核验的事实节点。请检查其中是否存在【互相矛盾】的数值或定义。"
                "只报真矛盾，没有就返回空列表。\n\n" + block +
                '\n输出 JSON：{"contradictions": [{"a": "Nxx", "b": "Nyy", "desc": "一句话"}]}')
            try:
                out, _ = call_llm(prompt, max_tokens=2000, temperature=0.0, retries=2)
                d = _extract_json(out or "") or {}
                contradictions = d.get("contradictions") or []
                log_step("contradiction_scan", {
                    "n_found": len(contradictions),
                    "details": [f"{c.get('a')} vs {c.get('b')}: {c.get('desc','')[:60]}" for c in contradictions[:5]],
                })
            except Exception as e:
                log_step("contradiction_scan", {"error": str(e)})
        else:
            log_step("contradiction_scan", {"skipped": f"only {len(ver)} verified nodes"})

    # ── Step 5: 综合（D3: baseline vs simple）──
    table = "\n".join(
        f"{f['id']}: {f['corrected_claim']}  [status={f['status']}; evidence: {f['evidence'][:120]}]"
        for f in facts)

    if cfg["d3"] == "simple":
        # 简化版 P4：去掉分析层
        prompt = (
            f"你是严谨的研究员。基于下面已核验的事实节点表，回答问题。"
            f"先给结论，再给因果链。每个数字写量纲和口径。\n\n"
            f"【问题】\n{question}\n\n【事实表】\n{table}") + _perturb()
    else:
        from s5_pipeline import P4_SYNTHESIZE
        prompt = P4_SYNTHESIZE.format(question=question, fact_table=table) + _perturb()

    answer, usage = call_llm(prompt, max_tokens=8000, temperature=0.7, top_p=0.95)
    result["answer"] = answer or ""
    result["usage"] = usage or {}
    log_step("synthesize_done", {"answer_len": len(result["answer"])})

    # ── Step 6: 打分 ──
    j = judge(qid, answer or "")
    cov = round(j.get("coverage") or 0, 3)
    try:
        dv = score_run(qid, answer or "")
        depth = dv.get("overall")
    except Exception:
        depth = None

    result.update({
        "judge": j, "coverage": cov, "depth_score": depth,
        "n_nodes": len(facts), "n_verified": n_verified,
        "verified_rate": round(n_verified / max(len(facts), 1), 3),
        "wall_s": round(time.time() - t0, 1),
    })
    log_step("score_done", {"coverage": cov, "depth": depth,
                             "n_nodes": len(facts), "n_verified": n_verified,
                             "wall_s": result["wall_s"]})

    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=1))
    print(f"  [{tag}] cov={cov} depth={depth} ver={n_verified}/{len(facts)} wall={result['wall_s']}s", flush=True)
    return result


def write_summary(out_dir: Path, results: list[dict]):
    """写汇总表格。"""
    lines = ["# Prompt 组合消融汇总\n",
             f"生成时间: {datetime.now(timezone.utc).isoformat()}\n",
             "| 臂 | 题 | cov | depth | ver_rate | n_nodes | wall_s | Q2_drop | Q4_drop | contra |",
             "|----|----|-----|-------|----------|---------|--------|---------|---------|--------|"]
    for r in results:
        if "error" in r:
            lines.append(f"| {r['arm']} | {r['qid']} | ERROR: {r['error'][:30]} | - | - | - | - | - | - | - |")
            continue
        lines.append(
            f"| {r['arm']} | {r['qid']} | {r.get('coverage', '-')} | {r.get('depth_score', '-')} "
            f"| {r.get('verified_rate', '-')} | {r.get('n_nodes', '-')} | {r.get('wall_s', '-')} "
            f"| - | - | - |")
    (out_dir / "summary.md").write_text("\n".join(lines))
    print(f"  summary written to {out_dir / 'summary.md'}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--arms", default="A0,A6,A7", help="comma-separated arm ids, or 'all'")
    ap.add_argument("--qs", default="nat,soc,gpu", help="comma-separated question ids")
    ap.add_argument("--reps", type=int, default=1)
    ap.add_argument("--out", default="runs-qc-ablation")
    args = ap.parse_args()

    arms = list(ARMS.keys()) if args.arms == "all" else args.arms.split(",")
    qs = args.qs.split(",")
    out_dir = HERE / args.out
    out_dir.mkdir(exist_ok=True)
    (out_dir / "step-log").mkdir(exist_ok=True)

    total = len(arms) * len(qs) * args.reps
    print(f"QC ABLATION SWEEP: {total} runs ({len(arms)} arms × {len(qs)} qs × {args.reps} reps)", flush=True)

    results = []
    done = 0
    for arm in arms:
        for qid in qs:
            for rep in range(1, args.reps + 1):
                done += 1
                print(f"[{done}/{total}] arm={arm} qid={qid} rep={rep}", flush=True)
                r = run_arm(arm, qid, rep, out_dir)
                results.append(r)

    write_summary(out_dir, results)
    print(f"QC ABLATION SWEEP DONE: {len(results)} runs", flush=True)


if __name__ == "__main__":
    main()
