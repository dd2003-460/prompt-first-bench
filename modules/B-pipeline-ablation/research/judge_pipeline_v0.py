#!/usr/bin/env python3
"""
judge_pipeline_v0.py — J2 整合入口：judge_v1(coverage) + correctness_layer_v0(correctness) 联合打分。

# origin: ai  (J2, 2026-11-25)
- coverage 口径 = judge_v1.layer_coverage（bge-m3 节点级 claim 编码, COS_THRESHOLD=0.7, frozen spec f6072397f, 只 import 不改）
- correctness 口径 = correctness_layer_v0（纯规则三型 A1/A2/A3 判别 + C/E/R/S/N 五轴, J1 已验收）
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
        for i, a in enumerate(d.get("arm_a", [])):
            out.append((f"{base}.arm_a[{i}]", "t8b_a",
                        {"text": _first_text(a.get("content"), a.get("reasoning")),
                         "qid": "gpu"},
                        f"arm_a[{i}] content[{len(a.get('content',''))}]ch"))
        for i, b in enumerate(d.get("arm_b", [])):
            out.append((f"{base}.arm_b[{i}]", "t8b_b",
                        {"text": _first_text(b.get("final_content"), b.get("final", {}).get("content") if isinstance(b.get("final"), dict) else None,
                                  b.get("final_reasoning")),
                         "qid": "gpu"},
                        f"arm_b[{i}] final_content[{len(b.get('final_content',''))}]ch"))
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
            else:
                out.append((sid, "unknown", {}, "runs item schema 未识别"))
    else:
        out.append((base, "unknown", {}, "schema 未识别(无 answer/nodes/arm_a/arm_b/runs)"))
    return out


# ---------- 单样本联合打分 ----------

def compute_coverage(payload, qid, model):
    """judge_v1 口径 coverage。nested→节点级; flat/t8b→整篇当单节点(1-node 退化, 口径对齐 S5 的节点级)。"""
    if payload["kind"] == "nested":
        nodes = [{"id": n.get("id", f"N{i}"), "claim": n.get("claim", ""), "depth": 1}
                 for i, n in enumerate(payload["nodes"])]
    else:
        nodes = [{"id": "SINGLE", "claim": payload["text"], "depth": 1}]
    gold_units = judge_v1.load_gold(qid)
    cov, det = judge_v1.layer_coverage(nodes, gold_units, model, judge_v1.COS_THRESHOLD)
    return cov, det


def compute_correctness(text, qid):
    """correctness_layer_v0 口径: 五轴 + P_A1/P_A3/C2BP + 三型 verdict (纯规则, 无模型)。"""
    ax = cl.compute_axes(text, qid)
    p_a1, p_a3 = cl.prior_a1(text, qid), cl.prior_a3(text, qid)
    c2bp = cl.count_c2bp(text)
    verdict, ev = cl.classify_verdict(text, qid, p_a1, p_a3, c2bp)
    corr = cl.correctness_score(ax)
    return ax, p_a1, p_a3, c2bp, verdict, ev, corr


def score_sample(sample_id, payload, qid, model):
    """一个样本 → 联合结果 dict。"""
    cov, det = compute_coverage(payload, qid, model)
    nodes = payload.get("nodes")
    text = ("\n".join(n.get("claim","") for n in nodes) if nodes else payload.get("text",""))
    ax, p_a1, p_a3, c2bp, verdict, ev, corr = compute_correctness(text, qid)
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
    }


# ---------- 存量集 preset ----------

STOCK_S0 = [f"{_ROOT}/experiments/stage-ablation/runs-prod/S0-gpu-r{i}.json" for i in range(1, 11)]
STOCK_S5 = f"{_ROOT}/experiments/stage-ablation/runs-s5-sm-gpu.json"
STOCK_T8B = f"{_ROOT}/tasks/think-trigger/exp-results/raw_outputs_t8b.json"


def preset_paths(preset):
    if preset == "stock":
        return STOCK_S0 + [STOCK_S5, STOCK_T8B]
    raise SystemExit(f"未知 preset: {preset}")


# ---------- 表格渲染 ----------

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
             "flat/t8b 样本无节点结构 → cov 按整篇当单节点计算（1-node 退化口径，非节点级）。")
    L.append("")
    L.append("| sample | cov | CORR | 三轴关键值(C/E/R/S/N + P_A1/P_A3/C2BP) | verdict | 备注 |")
    L.append("|---|---|---|---|---|---|")
    for r in results:
        L.append(fmt_row(r))
    L.append("")
    L.append("## 口径对齐证据")
    L.extend(evidence_lines)
    L.append("")
    return "\n".join(L) + "\n"


# ---------- 主入口 ----------

def run(paths, qid_default, outdir, write_md=True, md_title=None):
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
            qid = payload.get("qid", qid_default)
            r = score_sample(sid, payload, qid, model)
            r["note"] = note
            results.append(r)
            print(f"  {r['sample']:28s} cov={_num(r['cov'])} CORR={_num(r['CORR'])} "
                  f"P_A1={_num(r['P_A1'])} P_A3={_num(r['P_A3'])} C2BP={r['C2BP']} verdict={r['verdict']}",
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


def main():
    ap = argparse.ArgumentParser(description="judge_v1 + correctness_layer_v0 联合打分入口")
    ap.add_argument("files", nargs="*", help="run 文件路径(任意 schema)")
    ap.add_argument("--preset", choices=["stock"], help="内置存量集")
    ap.add_argument("--qid", default="gpu", help="gold 域(默认 gpu)")
    ap.add_argument("--outdir", default=_HERE, help="输出目录")
    ap.add_argument("--no-md", action="store_true", help="不写 md")
    ap.add_argument("--md-title", default=None)
    a = ap.parse_args()
    paths = list(a.files)
    if a.preset:
        paths += preset_paths(a.preset)
    if not paths:
        ap.error("需要 files 或 --preset")
    run(paths, a.qid, a.outdir, write_md=not a.no_md, md_title=a.md_title)


if __name__ == "__main__":
    main()
