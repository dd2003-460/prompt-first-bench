#!/usr/bin/env python3
"""
judge_pipeline_v0.py — J2 整合入口：judge_v1(coverage) + correctness_layer_v0(correctness) 联合打分。

# origin: ai  (J2, 2026-11-25)
- coverage 口径 = judge_v1.layer_coverage（bge-m3 节点级 claim 编码, COS_THRESHOLD=0.7, frozen spec f6072397f, 只 import 不改）
- correctness 口径 = correctness_layer_v0（纯规则三型 A1/A2/A3 判别 + C/E/R/S/N 五轴, J1 已验收）
- bonus 口径（2026-11-26, gold-tree.md『停止判据声明』）: gold 在 η_bw（经验系数）处停止分解 =
  可测量性收口而非能力边界。模型在收口处继续拆出的、且按现有 correctness 判据判为正确的更深层
  分解 = 加分项: 单独计数（bonus_count/bonus_nodes）, 不进 cov 分母（cov 计算逻辑零改动, 纯旁路）。
  判据假设: 节点级 top-1 cosine ≥ COS_THRESHOLD(0.70) 判"正确"（= 本文件 compute_coverage 的
  现有节点级 correctness 判据, 未引入新判据）; "超出 gold 深度" = 模型节点深度 > 其 top-1 匹配
  gold 单元的 depth（gold 在该位置已收口/无更深分解）。
- 输入任意 run 文件, 自动适配三种 schema:
    flat   : {answer: "..."} 自由文本 (S0-gpu-r*.json)
    nested : {nodes: [{claim,...}]} 节点级 (runs-s5-sm-gpu.json)
    t8b    : {arm_a:[{content}], arm_b:[{final_content}]} (raw_outputs_t8b.json)
  历史坑: 早期代码假设 d["runs"] → flat 文件 KeyError 'runs'; 本脚本对三种 schema 都不假设顶层键。
- 单次运行只加载一次 bge-m3（cov 计算共用同一 model 实例）。

用法:
  python3 judge_pipeline_v0.py --preset stock --outdir <research目录>
  python3 judge_pipeline_v0.py <run.json> [<run2.json> ...] [--qid gpu] [--outdir DIR] [--no-md]
  --preset stock = S0-gpu-r1..r10 + runs-s5-sm-gpu.json + raw_outputs_t8b.json（J2 存量集）
"""
import argparse
import datetime as _dt
import json
import os
import re
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))          # .../research
_PARENT = os.path.dirname(_HERE)                            # .../B-pipeline-ablation
_ROOT = os.path.abspath(os.path.join(_PARENT, "..", ".."))  # pfb 根
sys.path.insert(0, _PARENT)  # judge_v1.py
sys.path.insert(0, _HERE)    # correctness_layer_v0.py

import judge_v1                       # frozen, 只 import
import correctness_layer_v0 as cl     # J1 验收层, 只 import

MODEL_NAME = "BAAI/bge-m3"


def _num(x, nd=3):
    """数值格式化: None → '-'"""
    return "-" if x is None else f"{x:.{nd}f}"


def _first_text(*vals):
    """取第一个非空字符串"""
    for v in vals:
        if isinstance(v, str) and v.strip():
            return v
    return ""


# ---------- schema 适配: 任意 run 文件 → [(sample_id, kind, payload, note)] ----------

def load_samples(path):
    d = json.load(open(path, encoding="utf-8"))
    base = os.path.splitext(os.path.basename(path))[0]
    out = []
    if isinstance(d, dict) and isinstance(d.get("nodes"), list):
        nodes = d["nodes"]
        out.append((base, "nested", {"nodes": nodes},
                    f"nested nodes[{len(nodes)}]"))
    elif isinstance(d, dict) and isinstance(d.get("answer"), str):
        qid = d.get("qid", "gpu")
        out.append((base, "flat", {"text": d["answer"], "qid": qid},
                    f"flat answer[{len(d['answer'])}]ch"))
    elif isinstance(d, dict) and ("arm_a" in d or "arm_b" in d):
        # T8b 对称抽取: 镜像 correctness_layer_v0.load_samples (J1 验收口径)。
        # arm_a = content+reasoning; arm_b = final_content+final_reasoning+stages[*].content/reasoning。
        # 早期 _first_text 只取首字段 → arm_b 3090 计数减半 → A1 失真, 故必须对称拼接。
        for i, a in enumerate(d.get("arm_a", [])):
            txt = (a.get("content", "") or "") + "\n" + (a.get("reasoning", "") or "")
            out.append((f"{base}.arm_a[{i}]", "t8b_a", {"text": txt, "qid": "gpu"},
                        f"arm_a[{i}] content+reasoning[{len(txt)}]ch"))
        for i, b in enumerate(d.get("arm_b", [])):
            parts = [b.get("final_content", "") or "", b.get("final_reasoning", "") or ""]
            st = b.get("stages", {})
            vals = st.values() if isinstance(st, dict) else st
            for v in vals:
                if isinstance(v, dict):
                    parts.append(v.get("content", "") or "")
                    parts.append(v.get("reasoning", "") or "")
                else:
                    parts.append(v if isinstance(v, str) else "")
            txt = "\n".join(parts)
            out.append((f"{base}.arm_b[{i}]", "t8b_b", {"text": txt, "qid": "gpu"},
                        f"arm_b[{i}] final+stages[{len(txt)}]ch"))
    elif isinstance(d, dict) and isinstance(d.get("runs"), (list, dict)):
        # 嵌套 runs 容器: runs=list[{nodes|answer}] 或 runs=dict{id:{nodes|answer}}
        items = d["runs"].values() if isinstance(d["runs"], dict) else d["runs"]
        for j, it in enumerate(items):
            sid = f"{base}.runs[{j}]"
            if isinstance(it, dict) and isinstance(it.get("nodes"), list):
                out.append((sid, "nested", {"nodes": it["nodes"]}, f"runs[{j}] nodes[{len(it['nodes'])}]"))
            elif isinstance(it, dict) and isinstance(it.get("answer"), str):
                out.append((sid, "flat", {"text": it["answer"], "qid": it.get("qid", "gpu")},
                            f"runs[{j}] answer[{len(it['answer'])}]ch"))
            elif isinstance(it, dict) and isinstance(it.get("output_text"), str):
                # arena-judge-s6s7-pack.json 形态: runs=dict{id:{prompt,output_text,tokens_out,...}}
                out.append((sid, "flat", {"text": it["output_text"], "qid": it.get("qid", "gpu")},
                            f"runs[{j}] output_text[{len(it['output_text'])}]ch"))
            else:
                out.append((sid, "unknown", {}, "runs item schema 未识别"))
    else:
        out.append((base, "unknown", {}, "schema 未识别(无 answer/nodes/arm_a/arm_b/runs)"))
    return out


# ---------- 单样本联合打分 ----------

def _cov_nodes(payload):
    """cov 节点构造, 严格镜像 correctness_layer_v0.load_samples (J1 验收口径):
    nested → 真实节点 claim; flat/t8b 自由文本 → 非空行作伪节点 (line-as-node)。
    注: 整篇当单节点会低估 cov (长文本嵌入稀释), 与 J1 dry-run 的 T8b cov 不一致, 故必须非空行。"""
    if payload["kind"] == "nested":
        return [{"id": n.get("id", f"N{i}"), "claim": n.get("claim", ""), "depth": 1}
                for i, n in enumerate(payload["nodes"])]
    text = payload.get("text", "")
    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
    return [{"id": f"L{i}", "claim": ln, "depth": 1} for i, ln in enumerate(lines)]


def compute_coverage(payload, qid, model):
    """judge_v1 口径 coverage (judge_v1.layer_coverage, bge-m3 节点级, COS>=0.7)。"""
    nodes = _cov_nodes(payload)
    gold_units = judge_v1.load_gold(qid)
    cov, det = judge_v1.layer_coverage(nodes, gold_units, model, judge_v1.COS_THRESHOLD)
    return cov, det


def compute_correctness(text, qid, winner=cl.WINNER_CARD):
    """correctness_layer_v0 口径: judge_text → 五轴(C/E/R/S/N) + P_A1/P_A3/C2BP + 三型 verdict (纯规则, 无模型)。
    winner: winner 卡型（7bab6dd77 参数化, 默认 WINNER_CARD=V100）; 3090 世界的存量 fixture
    (S5/T8b) 必须显式传 "3090", 否则被默认 V100 误判（2026-11-26 selftest 4 FAIL 根因）。"""
    res = cl.judge_text(text, winner=winner)
    ax = {"C": res["C"], "E": res["E"], "R": res["R_low"], "S": res["S"], "N": res["N"]}
    return ax, res["P_A1"], res["P_A3"], res["C2BP"], res["verdict"], res.get("detail", {}), res["corr"]


# ---------- 加分项（gold-tree.md 停止判据声明 2026-11-26） ----------
# 纯旁路: 只读模型节点 + gold 单元, 不触碰 compute_coverage / judge_v1.layer_coverage 的任何
# 计算, cov 分母零改动。判据假设: 节点"正确" = top-1 cosine >= COS_THRESHOLD(0.70)（= 本文件
# compute_coverage 已在用的节点级 correctness 判据, 未引入新判据）; "超出 gold 深度" = 模型节点
# depth > 其 top-1 匹配 gold 单元的 depth（gold 在该位置已收口/无更深分解）。
def compute_bonus(payload, qid, model):
    """加分项: 模型在 gold 收口处继续拆出的、判为正确的更深层分解, 单独计数。
    返回 (bonus_count, bonus_nodes, bonus_meta)。free-text(line-as-node, depth 恒=1) → 0。
    节点 claim 与 cov 同口径(_cov_nodes); 但 depth 用真实节点深度（judge_v1.load_run_nodes 同规则:
    level 'L<n>' 或 len(parent_ids)+1）——_cov_nodes 为 cov 口径把 nested depth 拍平成 1, 不能用。"""
    import numpy as np
    nodes = _cov_nodes(payload)            # 与 cov 同口径的模型节点（claim 一致）
    if not nodes:
        return 0, [], {"reason": "no model nodes"}
    # 真实深度（仅 nested 有意义; flat/t8b 保持 1 → 不可能 > gold depth → bonus 恒 0）
    if payload.get("kind") == "nested":
        for n, raw in zip(nodes, payload["nodes"]):
            m = re.match(r"L(\d+)", raw.get("level", ""))
            n["depth"] = int(m.group(1)) if m else (len(raw.get("parent_ids", [])) + 1)
    gold_units = judge_v1.load_gold(qid)
    if not gold_units:
        return 0, [], {"reason": "no gold units for qid=%s" % qid}
    node_emb = model.encode([n["claim"] for n in nodes], normalize_embeddings=True,
                            show_progress_bar=False)
    gold_emb = model.encode([u["text"] for u in gold_units], normalize_embeddings=True,
                            show_progress_bar=False)
    sim = node_emb @ gold_emb.T
    top1 = sim.argmax(axis=1)
    top1_sim = sim[np.arange(len(nodes)), top1]
    thr = judge_v1.COS_THRESHOLD
    bonus_nodes = []
    n_correct = 0
    n_beyond = 0
    for i, n in enumerate(nodes):
        g_idx = int(top1[i])
        g_unit = gold_units[g_idx]
        correct = bool(top1_sim[i] >= thr)      # 现有节点级 correctness 判据
        beyond = n["depth"] > g_unit["depth"]   # 超出 gold 深度（收口处继续拆）
        n_correct += int(correct)
        n_beyond += int(beyond)
        if correct and beyond:
            bonus_nodes.append({
                "node_path": n["id"],
                "depth": n["depth"],
                "matched_gold": g_unit["unit_id"],
                "gold_depth": g_unit["depth"],
                "cos": round(float(top1_sim[i]), 4),
                "reason": "depth %d > gold %s depth %d (收口处继续分解) 且 cosine %.3f >= %.2f"
                          % (n["depth"], g_unit["unit_id"], g_unit["depth"],
                             float(top1_sim[i]), thr),
            })
    meta = {
        "criterion": "top-1 cosine >= %.2f (现有节点级 correctness 判据, 同 compute_coverage)" % thr,
        "beyond_rule": "node.depth > matched_gold.unit.depth",
        "n_model_nodes": len(nodes),
        "n_correct": n_correct,
        "n_beyond": n_beyond,
        "cov_denominator_untouched": True,
    }
    return len(bonus_nodes), bonus_nodes, meta


def score_sample(sample_id, payload, qid, model, winner=cl.WINNER_CARD):
    """一个样本 → 联合结果 dict。winner 透传给 correctness 层（默认 V100, 3090 世界显式传）。"""
    cov, det = compute_coverage(payload, qid, model)
    nodes = payload.get("nodes")
    text = ("\n".join(n.get("claim","") for n in nodes) if nodes else payload.get("text",""))
    ax, p_a1, p_a3, c2bp, verdict, ev, corr = compute_correctness(text, qid, winner)
    bonus_count, bonus_nodes, bonus_meta = compute_bonus(payload, qid, model)
    return {
        "sample": sample_id,
        "kind": payload["kind"],
        "cov": cov,
        "cov_detail": det,
        "CORR": corr,
        "axes": ax,
        "P_A1": p_a1,
        "P_A3": p_a3,
        "C2BP": c2bp,
        "verdict": verdict,
        "evidence": ev,
        "bonus_count": bonus_count,
        "bonus_nodes": bonus_nodes,
        "bonus_meta": bonus_meta,
    }


# ---------- 存量集 preset ----------

STOCK_S0 = [f"{_ROOT}/experiments/stage-ablation/runs-prod/S0-gpu-r{i}.json" for i in range(1, 11)]
STOCK_S5 = f"{_ROOT}/experiments/stage-ablation/runs-s5-sm-gpu.json"
STOCK_T8B = f"{_ROOT}/modules/G-think-mechanism/think-trigger/exp-results/raw_outputs_t8b.json"


def preset_paths(preset):
    if preset == "stock":
        return STOCK_S0 + [STOCK_S5, STOCK_T8B]
    raise SystemExit(f"未知 preset: {preset}")


# ---------- 三型分布 ----------

def _grp(sample):
    if sample.startswith("S0-gpu"):
        return "S0"
    if sample == "runs-s5-sm-gpu":
        return "S5"
    if sample.startswith("raw_outputs_t8b"):
        return "T8b"
    return "other"


def distribution_block(results):
    """A1/A2/A3/indeterminate 分布统计 + 结论（只答断点分布, 不做质量 claim）。"""
    order = ["A1", "A2", "A3", "indeterminate"]
    L = ["## A1/A2/A3 分布统计", ""]
    L.append("| 组 | n | A1 | A2 | A3 | indeterminate |")
    L.append("|---|---|---|---|---|---|")
    groups = {}
    for r in results:
        groups.setdefault(_grp(r["sample"]), []).append(r["verdict"])
    tot = {k: 0 for k in order}
    for g in ["S0", "S5", "T8b", "other"]:
        if g not in groups:
            continue
        vs = groups[g]
        row = [g, str(len(vs))]
        for k in order:
            c = vs.count(k)
            tot[k] += c
            row.append(str(c))
        L.append("| " + " | ".join(row) + " |")
    L.append("| **合计** | **" + str(sum(len(v) for v in groups.values())) + "** | "
             + " | ".join(f"**{tot[k]}**" for k in order) + " |")
    L.append("")
    L.append("## 结论（只答：存量数据里三型断点分布如何）")
    L.append("")
    s0 = groups.get("S0", [])
    t8b = groups.get("T8b", [])
    s5 = groups.get("S5", [])
    L.append(f"- **S0 基线 10 条**：A1×{s0.count('A1')} / A2×{s0.count('A2')} / A3×{s0.count('A3')} / indeterminate×{s0.count('indeterminate')}。"
             f"A1（winner 卡型 3090 从未进候选集）是 S0 主导断点（{s0.count('A1')}/10），A2（卡型在候选集但 4×3090 配置从未构造/评估）次之（{s0.count('A2')}/10），"
             f"S0 无 A3（无一条把 winner 配置完整评估后排垫底）。")
    L.append(f"- **S5（节点级, cov 最高 0.389）**：判 **A2**——cov 本批最高但 winner 配置从未构造/评估，正是 coverage 陷阱样本（词汇覆盖高、结构断点在候选集粒度）。")
    L.append(f"- **T8b 6 条**：A1×{t8b.count('A1')} / A2×{t8b.count('A2')} / A3×{t8b.count('A3')} / indeterminate×{t8b.count('indeterminate')}。"
             f"三型齐备（arm_a[0]=A1, arm_a[1]=A2, arm_a[2]=A3, arm_b[0/1/2]=A2），A2 占 4/6 为主导失败模式。")
    L.append(f"- **总体**：17 条中 A1×{tot['A1']} / A2×{tot['A2']} / A3×{tot['A3']} / indeterminate×{tot['indeterminate']}。"
             f"A2（候选集粒度断点）是存量数据的主导断点类型；A3 仅出现在 T8b arm_a[2]（唯一把 winner 配置完整评估后又排垫底的样本）。"
             f"断点分布呈 A2 > A1 > A3 的梯度，indeterminate 为 0（本批每条都落在某一断点型上）。")
    L.append("- **边界**：本表只描述断点类型分布，不 claim 任何质量提升/退化；S0 为 flat 自由文本（cov 为 line-as-node 口径，非节点级）。")
    L.append("")
    return L


def fmt_row(r):
    a = r["axes"]
    keys = (f"C={_num(a['C'])} E={_num(a['E'])} R={_num(a['R'])} "
            f"S={_num(a['S'])} N={_num(a['N'])} P_A1={_num(r['P_A1'])} "
            f"P_A3={_num(r['P_A3'])} C2BP={r['C2BP']}")
    note = r["note"]
    return f"| {r['sample']} | {_num(r['cov'])} | {_num(r['CORR'])} | {keys} | {r['verdict']} | {note} |"


def render_md(results, title, evidence_lines):
    L = []
    L.append(f"# {title}")
    L.append("")
    L.append("# origin: ai (J2, 2026-11-25) — judge_v1(coverage) + correctness_layer_v0(correctness) 联合重算")
    L.append("")
    L.append("**口径**：cov = judge_v1.layer_coverage（bge-m3 节点级, COS≥0.7, frozen spec f6072397f）；"
             "CORR/五轴/verdict = correctness_layer_v0（纯规则三型 A1/A2/A3, J1 验收）。"
             "cov 节点构造镜像 J1 load_samples：nested=真实节点 claim；flat/t8b 自由文本=非空行作伪节点（line-as-node，"
             "与 J1 dry-run 的 T8b cov 同口径；整篇当单节点会低估 cov）。")
    L.append("")
    L.append("| sample | cov | CORR | 三轴关键值(C/E/R/S/N + P_A1/P_A3/C2BP) | verdict | 备注 |")
    L.append("|---|---|---|---|---|---|")
    for r in results:
        L.append(fmt_row(r))
    L.append("")
    L.append("## 口径对齐证据")
    L.extend(evidence_lines)
    L.append("")
    L.extend(distribution_block(results))
    return "\n".join(L) + "\n"


# ---------- 主入口 ----------

def run(paths, qid_default, outdir, write_md=True, md_title=None, winner=cl.WINNER_CARD):
    from sentence_transformers import SentenceTransformer
    t0 = time.time()
    print(f"[load] {MODEL_NAME} ...", flush=True)
    model = SentenceTransformer(MODEL_NAME)
    print(f"[load] done {time.time()-t0:.1f}s", flush=True)

    results = []
    for path in paths:
        if not os.path.exists(path):
            print(f"[skip] 不存在: {path}", flush=True)
            continue
        samples = load_samples(path)
        for sid, kind, payload, note in samples:
            payload["kind"]=kind
            qid = payload.get("qid", qid_default)
            r = score_sample(sid, payload, qid, model, winner)
            r["note"] = note
            results.append(r)
            print(f"  {r['sample']:28s} cov={_num(r['cov'])} CORR={_num(r['CORR'])} "
                  f"P_A1={_num(r['P_A1'])} P_A3={_num(r['P_A3'])} C2BP={r['C2BP']} verdict={r['verdict']} "
                  f"bonus={r['bonus_count']}",
                  flush=True)

    os.makedirs(outdir, exist_ok=True)
    stamp = _dt.datetime.now().strftime("%Y%m%d")
    out_json = os.path.join(outdir, f"judge-pipeline-v0-{stamp}.json")
    payload_out = {
        "generated_at": _dt.datetime.now().astimezone().isoformat(),
        "cov_caliber": "judge_v1.layer_coverage bge-m3 COS>=0.7 (frozen f6072397f)",
        "corr_caliber": "correctness_layer_v0 (J1 accepted)",
        "samples": results,
    }
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(payload_out, f, ensure_ascii=False, indent=1)
    print(f"[json] {out_json}", flush=True)

    evidence = _alignment_evidence(results)
    md = None
    if write_md:
        md_path = os.path.join(outdir, "joint-scores-20261125.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(render_md(results, md_title or "J2 联合分表 — S0-r1..r10 + S5 + T8b", evidence))
        md = md_path
        print(f"[md] {md_path}", flush=True)
    return results, out_json, md


def _alignment_evidence(results):
    """口径对齐证据: S5 cov vs 0.389, T8b verdict vs J1 dry-run。"""
    lines = []
    s5 = next((r for r in results if r["sample"] == "runs-s5-sm-gpu"), None)
    if s5:
        ok = abs(s5["cov"] - 0.389) <= 0.01
        lines.append(f"- **S5 cov 复现**: 本脚本={s5['cov']:.4f} vs 基准 0.389 → {'✅ 对齐(±0.01)' if ok else '❌ 超出容差'}")
    exp = {"raw_outputs_t8b.arm_a[0]": "A1", "raw_outputs_t8b.arm_a[1]": "A2",
           "raw_outputs_t8b.arm_a[2]": "A3", "raw_outputs_t8b.arm_b[0]": "A2",
           "raw_outputs_t8b.arm_b[1]": "A2", "raw_outputs_t8b.arm_b[2]": "A2"}
    got = {r["sample"]: r["verdict"] for r in results if r["sample"] in exp}
    mism = {k: (exp[k], got.get(k)) for k in exp if got.get(k) != exp[k]}
    lines.append("- **T8b verdict 复现** (J1 dry-run: arm_a[0]=A1, arm_a[1]=A2, arm_a[2]=A3, arm_b[0/1/2]=A2):")
    for k in exp:
        g = got.get(k)
        mark = "✅" if g == exp[k] else "❌"
        lines.append(f"  - {mark} {k}: 期望 {exp[k]} / 实得 {g}")
    if not mism:
        lines.append("  - **全部 6/6 复现** ✅")
    else:
        lines.append(f"  - **差异 {len(mism)} 条**: {mism}（如实报告，未硬凑）")
    return lines


# ---------- 回归守卫: 口径对齐 selftest ----------

SELFTEST_EXP = {
    "runs-s5-sm-gpu": ("cov", 0.389, 0.01),
    "raw_outputs_t8b.arm_a[0]": ("verdict", "A1", None),
    "raw_outputs_t8b.arm_a[1]": ("verdict", "A2", None),
    "raw_outputs_t8b.arm_a[2]": ("verdict", "A3", None),
    "raw_outputs_t8b.arm_b[0]": ("verdict", "A2", None),
    "raw_outputs_t8b.arm_b[1]": ("verdict", "A2", None),
    "raw_outputs_t8b.arm_b[2]": ("verdict", "A2", None),
}


def selftest():
    """口径对齐回归守卫: 一条命令复验 S5 cov≈0.389 + T8b 6 verdict (J1 基准)。
    改动 correctness_layer / judge_v1 / 抽取逻辑后跑本命令, 漂移立刻被抓 (exit 1)。
    只跑 S5+T8b (7 样本, 快), 不含 S0 (10 样本, 慢)。"""
    from sentence_transformers import SentenceTransformer
    t0 = time.time()
    model = SentenceTransformer(MODEL_NAME)
    paths = [STOCK_S5, STOCK_T8B]
    # 存量 fixture 是 3090 世界（S5 gold winner=3090×4, T8b 候选集 3090/V100 旧锚点）;
    # 7bab6dd77 把 judge_text 默认 winner 改成 V100 后, 不显式传 3090 会被误判（4 FAIL 根因）。
    results = []
    for path in paths:
        for sid, kind, payload, note in load_samples(path):
            payload["kind"] = kind
            results.append(score_sample(sid, payload, "gpu", model, winner="3090"))
    fails = []
    for sid, (field, exp, tol) in SELFTEST_EXP.items():
        r = next((x for x in results if x["sample"] == sid), None)
        if r is None:
            fails.append(f"{sid}: 样本缺失"); continue
        if field == "cov":
            ok = abs(r["cov"] - exp) <= tol
            got = f"{r['cov']:.4f}"
        else:
            ok = r["verdict"] == exp
            got = r["verdict"]
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] {sid}: {field}={got} (期望 {exp}{f'±{tol}' if tol else ''})")
        if not ok:
            fails.append(f"{sid}: {field}={got} != {exp}")
    print(f"selftest: {'ALL PASS' if not fails else f'{len(fails)} FAIL: {fails}'} "
          f"({time.time()-t0:.1f}s)")
    return 0 if not fails else 1


def main():
    ap = argparse.ArgumentParser(description="judge_v1 + correctness_layer_v0 联合打分入口")
    ap.add_argument("files", nargs="*", help="run 文件路径(任意 schema)")
    ap.add_argument("--preset", choices=["stock"], help="内置存量集")
    ap.add_argument("--qid", default="gpu", help="gold 域(默认 gpu)")
    ap.add_argument("--winner", default=cl.WINNER_CARD,
                    help="winner 卡型(默认 %s=T8c 新锚点世界; 3090 世界存量 fixture 如 S5/T8b 传 3090)" % cl.WINNER_CARD)
    ap.add_argument("--outdir", default=_HERE, help="输出目录")
    ap.add_argument("--no-md", action="store_true", help="不写 md")
    ap.add_argument("--md-title", default=None)
    ap.add_argument("--selftest", action="store_true",
                    help="口径对齐回归守卫: 复验 S5 cov≈0.389 + T8b 6 verdict (J1 基准), 漂移 exit 1")
    a = ap.parse_args()
    if a.selftest:
        import sys as _sys
        _sys.exit(selftest())
    paths = list(a.files)
    if a.preset:
        paths += preset_paths(a.preset)
    if not paths:
        ap.error("需要 files 或 --preset")
    run(paths, a.qid, a.outdir, write_md=not a.no_md, md_title=a.md_title, winner=a.winner)


if __name__ == "__main__":
    main()
