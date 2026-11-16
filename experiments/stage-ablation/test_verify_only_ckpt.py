#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_verify_only_ckpt.py — verify-only checkpoint 落盘最小自测（2026-11-16）。

背景：verify-only 模式跑 1h+ 到 verified 75/108，但 checkpoints/sm-soc-r1.json
mtime 没变、内容还是旧计数——进度没落盘，进程死掉/下次 resume 全丢。
根因：旧 _save_checkpoint 用 len(self.rounds_log) 当 rnd，verify-only 下
rounds_log 永远为空 → 每批都写 sm-{qid}-r0.json，而 resume 读的是 r1。

本测试用 3 个假节点 + monkeypatch 掉联网/LLM 调用（verify_node 直接判 verified，
search_node 不触网），跑一小批 verify-only，断言：
  1. checkpoint 文件真的落盘（mtime 比测试开始时间新）
  2. verified 计数从 0 变 3（落盘内容反映真实进度）
  3. 文件名带批次号（r{base}-{k}），resume 探测逻辑能找到它
  4. 原子写：磁盘上不存在 .tmp 残留

跑法：cd experiments/stage-ablation && python3 test_verify_only_ckpt.py
"""
import json
import os
import shutil
import sys
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)

# ── 先 patch 掉联网/LLM，再 import（import 只定义函数，patch 在调用时生效）──
import s5_pipeline
import s5_state_machine
from s5_state_machine import DecompStateMachine, NodeRecord

# 假 verify：全部判 verified（测试只关心落盘链路，不关心核验质量）
def _fake_verify(node, srcs):
    return "verified", f"test-evidence for {node['id']}", node["claim"], "{}"

def _fake_search(node, qid="gpu"):
    return [], None  # 不触网

s5_state_machine.verify_node = _fake_verify
s5_state_machine.search_node = _fake_search
# _verify_batch 内部 from s5_pipeline import 的名字是模块级引用，
# s5_state_machine 顶层 from s5_pipeline import verify_node, search_node → patch 模块属性即可
import s5_state_machine as sm_mod
sm_mod.verify_node = _fake_verify
sm_mod.search_node = _fake_search

QID = "test-vonly"
CKPT_DIR = "checkpoints"
CKPT_BASE = f"{CKPT_DIR}/sm-{QID}-r1.json"

# ── 清理旧测试产物 ──
for p in [CKPT_BASE, f"{CKPT_DIR}/sm-{QID}-r2.json"]:
    if os.path.exists(p):
        os.remove(p)

# ── 准备：一个 r1 checkpoint（1 个 verified 节点），resume 后 verify-only 验 3 个 pending ──
seed_nodes = [
    {"id": "N1", "claim": "seed verified node", "level": "L1", "source": "knowledge",
     "status": "verified", "evidence": "seed", "corrected_claim": "seed verified node",
     "rework_count": 0, "parent_ids": [], "objective": None, "edge_type": "cartesian",
     "search_query": "", "retrieval_sources": []},
    {"id": "N2", "claim": "fake node A to verify", "level": "L2", "source": "knowledge",
     "status": "pending", "evidence": "", "corrected_claim": "",
     "rework_count": 0, "parent_ids": ["N1"], "objective": None, "edge_type": "cartesian",
     "search_query": "", "retrieval_sources": []},
    {"id": "N3", "claim": "fake node B to verify", "level": "L2", "source": "knowledge",
     "status": "pending", "evidence": "", "corrected_claim": "",
     "rework_count": 0, "parent_ids": ["N1"], "objective": None, "edge_type": "cartesian",
     "search_query": "", "retrieval_sources": []},
    {"id": "N4", "claim": "fake node C to verify", "level": "L2", "source": "knowledge",
     "status": "pending", "evidence": "", "corrected_claim": "",
     "rework_count": 0, "parent_ids": ["N1"], "objective": None, "edge_type": "cartesian",
     "search_query": "", "retrieval_sources": []},
]
os.makedirs(CKPT_DIR, exist_ok=True)
with open(CKPT_BASE, "w") as f:
    json.dump({"qid": QID, "question": "test question", "round": 1, "state": "verify",
               "dropped_redundant": 0, "leak_hits_total": 0, "network_degraded": False,
               "objective": None, "objective_mode": "formula", "challenge_log": [],
               "rework_events": [], "contradiction_events": [],
               "nodes": seed_nodes}, f, ensure_ascii=False, indent=2)

# ── 跑 verify-only（monkeypatch 掉 _probe_network，不触网）──
sm = DecompStateMachine("test question", qid=QID)
sm._probe_network = lambda: None
sm._scan_contradictions = lambda rnd: None  # 不烧 LLM
for nd in seed_nodes:
    sm.nodes.append(NodeRecord(**nd))
sm.ckpt_round = 1  # 模拟 resume 自 r1 ckpt

t0 = time.time()
mtime_before = time.time()
result = sm.run(skip_l1=True, verify_only=True)
mtime_after = time.time()

# ── 断言 ──
errors = []

# 1. 批次 ckpt 存在（r2：base=1 + 批号 1，3 节点 = 1 批）
batch_path = f"{CKPT_DIR}/sm-{QID}-r2.json"
if not os.path.exists(batch_path):
    errors.append(f"批次 checkpoint 不存在: {batch_path}（ls: {os.listdir(CKPT_DIR)}）")
else:
    mt = os.path.getmtime(batch_path)
    if mt < mtime_before:
        errors.append(f"checkpoint mtime {mt} 早于测试开始 {mtime_before}——没落盘")
    d = json.load(open(batch_path))
    cnt = Counter(n["status"] for n in d["nodes"])
    if cnt.get("verified", 0) != 4:  # 1 seed + 3 新验
        errors.append(f"checkpoint verified 计数 = {cnt.get('verified')}，期望 4（内容: {dict(cnt)}）")
    if d.get("round") != 2:  # base 1 + batch 1
        errors.append(f"checkpoint round = {d.get('round')}，期望 2")

# 2. 内存结果一致
mem_cnt = Counter(n.status for n in result.nodes)
if mem_cnt.get("verified", 0) != 4:
    errors.append(f"内存 verified 计数 = {mem_cnt.get('verified')}，期望 4")

# 3. 原子写：无 .tmp 残留
tmps = [p for p in os.listdir(CKPT_DIR) if p.endswith(".tmp")]
if tmps:
    errors.append(f"原子写残留 .tmp 文件: {tmps}")

# 4. resume 探测：模拟 main() 的逻辑（glob sm-{qid}-r*.json，round > base 的最大者）
import re as _re
import glob as _glob
_base = 1
found = []
for _p in _glob.glob(f"{CKPT_DIR}/sm-{QID}-r*.json"):
    _m = _re.search(r"r(\d+)\.json$", _p)
    if _m:
        _k = int(_m.group(1)) - _base
        if _k > 0:
            found.append(_k)
if not found or max(found) != 1:
    errors.append(f"resume 探测找不到批次 ckpt（glob 命中: {found}）")

# ── 清理 ──
for p in [CKPT_BASE, batch_path]:
    if os.path.exists(p):
        os.remove(p)

if errors:
    print("FAIL:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"PASS: verify-only 落盘正常（{mtime_after - t0:.1f}s）")
print(f"  - 批次 ckpt {batch_path} 落盘且 mtime 更新")
print(f"  - verified 计数 1 → 4（seed 1 + 新验 3）")
print(f"  - 无 .tmp 残留，resume 探测命中批次 k=1")
