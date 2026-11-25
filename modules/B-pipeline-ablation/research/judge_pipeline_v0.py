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
