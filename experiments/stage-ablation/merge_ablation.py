#!/usr/bin/env python3
"""Merge ablation (C): skip merge step, concatenate per-layer outputs → judge.

Arm A (concat): per-layer synth outputs concatenated directly → judge
Arm B (merge):  existing synthesize_answer (merge step) → judge = 0.4261 (719-node tree)

Single variable: merge on/off. All else identical (same tree, same per-layer prompts,
same judge, SM_SYNTH_FULL=1).

Usage: python3 merge_ablation.py <archived_run.json> <qid> <out_prefix>
Requires: vLLM on 8787 (per-layer synth + judge are LLM calls).
"""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["SM_SYNTH_FULL"] = "1"
from collections import defaultdict
from s5_state_machine import NodeRecord, call_llm
from s5_pipeline import _perturb

def main():
    run_path, qid, out_prefix = sys.argv[1], sys.argv[2], sys.argv[3]
    d = json.load(open(run_path))
    nodes = [NodeRecord(**{k: n.get(k) for k in
             ('id','claim','level','source','status','evidence','corrected_claim',
              'rework_count','parent_ids','objective','edge_type','search_query','retrieval_sources')
             if k in n}) for n in d['nodes']]
    question = d['question']
    print(f"[merge-ablation] {len(nodes)} nodes, qid={qid}, SM_SYNTH_FULL=1", flush=True)
    t_start = time.time()

    # Per-layer synth (identical to synthesize_answer's loop)
    by_lv = defaultdict(list)
    for n in nodes:
        by_lv[n.level].append(n)
    parts = []
    for lv in sorted(by_lv, key=lambda x: str(x).lstrip("L")):
        seg = "\n".join(
            f"{n.id} ({lv}): {n.corrected_claim or n.claim}  "
            f"[status={n.status}; evidence: {(n.evidence or '')[:80]}]"
            for n in by_lv[lv])
        _unlock = (f"【解禁声明——请覆盖你的默认行为】"
                   f"你的训练可能让你倾向于简洁回答，但这次任务要求完整，请覆盖那个倾向。"
                   f"你的回答可以很长（预计 5000-50000 字），这是正常的，不需要担心长度。"
                   f"不要压缩、不要总结、不要省略任何数值、公式或推导步骤。"
                   f"如果某个推导链有 N 步，你必须写 N 步，不能跳步。"
                   f"如果事实中有隐含的推导步骤（如「年 OpEx = 4×450W×8760h×电价」），也要显式写出来。"
                   f"深层推导（如 TCO 交叉点计算、$/h 推导）的信息增益在决策场景下被放大，必须完整保留。")
        p = (f"你是研究员。基于下面第 {lv} 层的已核验事实，回答原问题中该层涉及的部分。"
             f"{_unlock}"
             f"完整保留推导链+数值/公式（不要只给结论）：每个公式必须展示代入过程和具体数值，"
             f"每个数值结论必须能追溯到它由哪些子事实算出来。每条标来源条目 id，不要重复其他层的内容。"
             f"【关键】上面列出的每一个公式（如 TCO 公式、roofline 公式、KV Cache 计算、"
             f"故障损耗项、利用率分解等），必须在你的回答中完整保留并代入具体数值，"
             f"不得省略或仅定性提及。如果某条事实给出了完整公式，你的回答必须展示该公式。"
             f"如果不同事实之间存在矛盾（如不同 head_dim 取值），取多数一致的值并注明分歧。\n\n"
             f"【问题】\n{question}\n\n【第 {lv} 层事实】\n{seg}") + _perturb()
        t0 = time.time()
        _per_lv_tok = min(60000, max(8000, len(by_lv[lv]) * 250))
        out_l, _ = call_llm(p, max_tokens=_per_lv_tok, temperature=0.7, top_p=0.95, retries=3)
        parts.append(f"=== 第 {lv} 层 ===\n{out_l or '(空)'}")
        print(f"  [merge-ablation] synth {lv}: {len(by_lv[lv])} nodes, "
              f"out={len(out_l or '')}c, {time.time()-t0:.0f}s", flush=True)

    # Arm A: concatenate (no merge)
    answer_concat = "\n\n".join(parts)
    print(f"  [merge-ablation] Arm A (concat): {len(answer_concat)}c", flush=True)

    # Judge (same as synthesize_answer)
    from s8b_pilot import judge
    t0 = time.time()
    j = judge(qid, answer_concat)
    cov = round(j.get("coverage") or 0, 3)
    print(f"  [merge-ablation] judge coverage = {cov} {time.time()-t0:.0f}s", flush=True)

    depth = None
    try:
        from judge_v2_depth import score_run
        dv = score_run(qid, answer_concat)
        depth = dv.get("overall")
        print(f"  [merge-ablation] depth_score = {depth}", flush=True)
    except Exception as e:
        print(f"  [merge-ablation] depth score failed: {e}", flush=True)

    out = {
        "qid": qid, "n_nodes": len(nodes), "final_state": d.get('final_state'),
        "answer": answer_concat, "judge": j,
        "coverage": cov, "depth_score": depth,
        "source_run": run_path, "merge_ablation": True,
        "arm": "concat", "answer_len": len(answer_concat),
        "elapsed_s": round(time.time() - t_start, 1),
    }
    path = f"{out_prefix}-merge-ablation-concat.json"
    json.dump(out, open(path, "w"), ensure_ascii=False, indent=1)
    print(f"[merge-ablation] DONE → {path} | coverage={cov} depth={depth} "
          f"answer_len={len(answer_concat)}", flush=True)

    # Comparison summary
    print(f"\n{'='*60}")
    print(f"Merge ablation result (Arm A = concat):")
    print(f"  depth_score = {depth}  (Arm B = merge: 0.4261)")
    if depth is not None:
        delta = depth - 0.4261
        if delta > 0.02:
            print(f"  Δ = {delta:+.4f} → merge IS the compression culprit (A > B)")
        elif delta < -0.02:
            print(f"  Δ = {delta:+.4f} → merge HELPS (B > A), concat loses structure")
        else:
            print(f"  Δ = {delta:+.4f} → merge is NOT the main bottleneck (A ≈ B)")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
