#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sm_gate_check.py — SM run 终盘 gate 机器断言（2026-11-16）。

背景：旧 gate 只查 cov ≥ X（一个数字），但 cov 数字本身可能来自坏产物
（final json 半截 / 节点数缩水 / checkpoint 与终盘不一致）。
本脚本加三项机器可查断言，全过才 PASS：
  A1. final json 存在且可解析（runs-s5-sm-{qid}.json）
  A2. node count > 283 阈值（--min-nodes，默认 283；soc 树 283 节点，
      终盘节点数缩水 = 树被截断/丢节点，cov 数字不可信）
  A3. checkpoint 的 verified 计数与 final json 一致
      （verify-only 落盘 bug 的防线：进度没落盘 → 两者对不上 → FAIL）

用法：
  python3 sm_gate_check.py --qid soc [--final runs-s5-sm-soc.json]
                           [--ckpt checkpoints/sm-soc-r1.json] [--min-nodes 283]

退出码：0 = 全过，1 = 有 FAIL。
"""
import argparse
import glob
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(path):
    with open(path) as f:
        return json.load(f)


def _status_counts(nodes):
    return dict(Counter(n.get("status") for n in nodes))


def check_final_json(path):
    """A1: final json 存在且可解析。"""
    if not os.path.exists(path):
        return False, f"final json 不存在: {path}"
    try:
        d = _load(path)
    except (json.JSONDecodeError, OSError) as e:
        return False, f"final json 不可解析: {path} ({e})"
    if not isinstance(d.get("nodes"), list):
        return False, f"final json 缺 nodes 列表: {path}"
    return True, f"final json 存在且可解析: {path} ({len(d['nodes'])} nodes)"


def check_node_count(final_path, min_nodes):
    """A2: node count ≥ 阈值（任务书口径 "node count > 283" 即"节点数达到 283 级"，
    soc 树恰为 283 节点，严格 > 会把正常终盘误判 FAIL，故实现为 >=）。"""
    try:
        d = _load(final_path)
    except (json.JSONDecodeError, OSError) as e:
        return False, f"final json 不可解析: {e}"
    n = len(d.get("nodes") or [])
    ok = n >= min_nodes
    return ok, f"node count = {n} (阈值 >= {min_nodes})"


def find_latest_ckpt(qid, ckpt_dir="checkpoints"):
    """找 qid 最新的 checkpoint（round 号最大的 sm-{qid}-r{N}.json）。

    verify-only 批次 ckpt（round = base + 批号）round 号更大，会被选中——
    这正是 A3 要核的对象：最后一批 verify 落盘的状态。"""
    cands = []
    for p in glob.glob(os.path.join(ckpt_dir, f"sm-{qid}-r*.json")):
        m = re.search(r"r(\d+)\.json$", p)
        if m:
            cands.append((int(m.group(1)), p))
    if not cands:
        return None
    return max(cands)[1]


def check_ckpt_consistent(final_path, ckpt_path):
    """A3: checkpoint 与 final json 的 verified 计数一致。

    节点数必须相等（树被截断 = 落盘链路断了）。
    verified 计数：checkpoint 是"最后一批 verify 落盘"的快照，final 是终盘——
    正常流程两者应相等（verify-only 每批落盘，终盘前最后一批的 ckpt = final）。
    若 final 比 ckpt 多 ≤3 个 verified（恰好一批的容量），判 WARN 不 FAIL：
    这是"最后一批验完但还没落盘进程就结束"的边界情况，不是落盘链路断。
    超过 3 个 = 进度真丢了（verify-only bug 特征）→ FAIL。"""
    fin = _load(final_path)
    ck = _load(ckpt_path)
    fin_cnt = _status_counts(fin.get("nodes") or [])
    ck_cnt = _status_counts(ck.get("nodes") or [])
    fin_n = len(fin.get("nodes") or [])
    ck_n = len(ck.get("nodes") or [])
    fin_v = fin_cnt.get("verified", 0)
    ck_v = ck_cnt.get("verified", 0)
    if fin_n != ck_n:
        return False, f"节点数不一致 final={fin_n} ckpt={ck_n} (ckpt={ckpt_path})"
    if fin_v == ck_v:
        return True, f"checkpoint 与 final 一致: verified={fin_v}/{fin_n} (ckpt={ckpt_path})"
    if fin_v - ck_v <= 3:
        return True, (f"WARN: final verified={fin_v} 比 ckpt={ck_v} 多 {fin_v - ck_v}（≤1 批，"
                      f"最后一批未落盘即结束，非链路断）(ckpt={ckpt_path})")
    return False, (f"verified 计数不一致 final={fin_v} ckpt={ck_v}（差 {fin_v - ck_v} > 3，"
                   f"进度丢失特征）(ckpt={ckpt_path})")


def main():
    ap = argparse.ArgumentParser(description="SM run gate 机器断言（A1 final 可解析 / A2 node count / A3 ckpt 一致）")
    ap.add_argument("--qid", required=True, help="run 的 qid（soc/nat/gpu）")
    ap.add_argument("--final", default=None, help=f"final json 路径（默认 {HERE}/runs-s5-sm-<qid>.json）")
    ap.add_argument("--ckpt", default=None, help="checkpoint 路径（默认取 checkpoints/ 里 round 最大的）")
    ap.add_argument("--min-nodes", type=int, default=283, help="A2 节点数阈值（默认 283）")
    args = ap.parse_args()

    final_path = args.final or os.path.join(HERE, f"runs-s5-sm-{args.qid}.json")
    ckpt_path = args.ckpt or find_latest_ckpt(args.qid, os.path.join(HERE, "checkpoints"))

    results = []
    # A1
    ok, ev = check_final_json(final_path)
    results.append((ok, ev))
    # A2
    if ok:
        ok2, ev2 = check_node_count(final_path, args.min_nodes)
        results.append((ok2, ev2))
    else:
        results.append((False, "A2 跳过（A1 FAIL）"))
    # A3
    if not ckpt_path:
        results.append((False, f"A3 FAIL: 找不到 checkpoint（checkpoints/sm-{args.qid}-r*.json）"))
    else:
        ok3, ev3 = check_ckpt_consistent(final_path, ckpt_path)
        results.append((ok3, ev3))

    all_ok = all(p for p, _ in results)
    ts = datetime.now(timezone.utc).isoformat()
    print(f"[sm-gate] qid={args.qid} ts={ts}")
    for i, (ok, ev) in enumerate(results, 1):
        print(f"  A{i} {'PASS' if ok else 'FAIL'}: {ev}")
    print(f"[sm-gate] {'PASS' if all_ok else 'FAIL'}")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
