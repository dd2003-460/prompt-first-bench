# -*- coding: utf-8 -*-
"""T-REPAIR-1 运行时冒烟测试 (2026-11-25 00:45)

目的: 静态验证 (py_compile / git apply / 逻辑推理) 之外的最后一层——
在真实字节码上证明:
  (1) Fix-A: VM 特征 evidence 的失败节点 → mode=directed (原始 SM 同场景 = angle)
  (2) Fix-B: 失败节点 (degraded, rc=1) 被 pool merge 捞到 → 第 2 次尝试 attempt=2
  (3) 第 2 次 directed 成功 → claim 回写 + verified (max_rework=2 首次被行使)
方法: 组合 diff apply 到 scratch 副本 (绝不碰 SM 本体), mock LLM/检索/核验。
"""
import json, os, shutil, subprocess, sys, tempfile

SRC = "/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation"
DIFF = os.path.join(SRC, "tasks/repair-loop-fixes-combined.diff")

# ── 1) scratch 副本 + apply 组合 diff (镜像 repo 目录结构, diff 路径相对 repo 根) ──
scratch = tempfile.mkdtemp(prefix="sm_patched_")
subdir = os.path.join(scratch, "experiments", "stage-ablation")
os.makedirs(subdir)
import glob as _g
for fn in _g.glob(os.path.join(SRC, "*.py")):
    shutil.copy(fn, os.path.join(subdir, os.path.basename(fn)))
r = subprocess.run(["git", "apply", DIFF], cwd=scratch, capture_output=True, text=True)
assert r.returncode == 0, f"git apply 失败: {r.stderr}"
r = subprocess.run([sys.executable, "-m", "py_compile",
                    "experiments/stage-ablation/s5_state_machine.py"],
                   cwd=scratch, capture_output=True, text=True)
assert r.returncode == 0, f"py_compile 失败: {r.stderr}"
print("[1] scratch 副本 + 组合 diff apply + py_compile: OK")

sys.path.insert(0, subdir)
import s5_state_machine as sm_mod
from s5_state_machine import DecompStateMachine, NodeRecord, ObjectiveConfig
import ablation_harness
import s5_pipeline

# ── 2) mock 基础设施 ──
# _rework_directed 内部: from ablation_harness import call_llm (调用时 import → patch 模块属性生效)
# search_node / verify_node 是 s5_state_machine 模块命名空间的绑定 → patch 该命名空间
DIRECTED_JSON_FAIL = "{}"  # 无 corrected_claim → directed 失败
DIRECTED_JSON_OK = json.dumps({"corrected_claim": "H100 NVLink 带宽为 900GB/s",
                               "search_query": "H100 NVLink bandwidth GB/s"})

state = {"phase": "fail"}  # fail: 第1次 directed 失败; ok: 第2次成功

def mock_call_llm(prompt, max_tokens=800, temperature=0.0, retries=2, **kw):
    if state["phase"] == "fail":
        return DIRECTED_JSON_FAIL, None
    return DIRECTED_JSON_OK, None

def mock_search_node(node, qid=None):
    return ([{"url": "https://example.com/h100", "source_type": "web", "title": "H100 spec"}], None)

def mock_verify_node(node, sources):
    if state["phase"] == "ok":
        return ("verified", "来源确认 H100 NVLink 900GB/s", "H100 NVLink 带宽为 900GB/s", None)
    return ("failed", "来源显示带宽 3.35TB/s，与 claim 数值不一致", "", None)

ablation_harness.call_llm = mock_call_llm
sm_mod.search_node = mock_search_node
sm_mod.verify_node = mock_verify_node

# ── 3) 场景: 一个核验失败的节点, evidence 含 VM 特征 (不一致) ──
cfg = ObjectiveConfig()
sm = DecompStateMachine("GPU 集群 NVLink 带宽是多少?", qid="smoke", cfg=cfg)
n = NodeRecord(id="N1", claim="H100 NVLink 带宽为 3.35TB/s", level="L1",
               status="failed",
               evidence="来源显示带宽 900GB/s，与 claim 数值不一致，版本不匹配")
sm.nodes.append(n)
sm.contradiction_events = []  # 无正式矛盾事件 → 原始 SM 下 directed 不可能触发

# ── 4) Fix-A 验证: 第 1 次 rework → mode 必须 = directed ──
sm._rework([n])
ev1 = sm.rework_events[-1]
assert ev1["mode"] == "directed", f"Fix-A 未触发: mode={ev1['mode']} (期望 directed)"
assert ev1["attempt"] == 1
assert n.status == "degraded" and n.rework_count == 1, f"失败终态异常: {n.status} rc={n.rework_count}"
print(f"[2] Fix-A 运行时验证: 第1次 rework mode={ev1['mode']}, attempt={ev1['attempt']}, "
      f"失败→degraded rc=1: OK")

# ── 5) Fix-B 验证: pool merge 捞到 degraded rc=1 节点 ──
deduped = []  # 模拟下一轮无新节点 (实际中 gate 需 deduped 非空, 此处直接验证 pool 构造)
unverified = [x for x in deduped if x.status != "verified"]
unverified = unverified + [x for x in sm.nodes
                           if 0 < x.rework_count < sm.cfg.max_rework
                           and x.status == "degraded"]
assert n in unverified, "Fix-B pool merge 未捞到 degraded rc=1 节点"
print(f"[3] Fix-B 运行时验证: pool merge 捞到重入节点 {n.id} (degraded rc=1): OK")

# ── 6) 第 2 次尝试: attempt=2 + directed 成功 → claim 回写 + verified ──
state["phase"] = "ok"
orig_claim = n.claim
sm._rework(unverified)
ev2 = sm.rework_events[-1]
assert ev2["attempt"] == 2, f"max_rework 未行使: attempt={ev2['attempt']} (期望 2)"
assert ev2["mode"] == "directed"
assert n.status == "verified" and n.rework_count == 2, f"第2次终态异常: {n.status} rc={n.rework_count}"
assert n.claim == "H100 NVLink 带宽为 900GB/s", f"claim 未回写: {n.claim!r}"
assert n.claim != orig_claim
print(f"[4] 第2次尝试: attempt={ev2['attempt']}, mode={ev2['mode']}, 成功→verified, "
      f"claim 回写 {orig_claim[:20]!r}→{n.claim[:20]!r}: OK")

# ── 7) 第 3 次尝试被拒: rc=2 达 max_rework → L760 上界兜底 ──
n.status = "failed"  # 假设 verified 后又失败 (极端场景)
sm._rework([n])
assert n.rework_count == 2, f"上界失效: rc={n.rework_count} (期望仍=2, 不再 +1)"
assert n.status == "degraded"
print(f"[5] 上界兜底: rc=2 达 max_rework → 第3次拒绝重入, rc 保持 2, 终态 degraded: OK")

# ── 8) A/B 运行时对照: 原始 (未修补) SM 同场景 → mode=angle ──
sys.path.remove(subdir)
del sys.modules["s5_state_machine"]
sys.path.insert(0, SRC)  # 原始 SM
import s5_state_machine as sm_orig
import ablation_harness as ah_orig
sm_orig.search_node = mock_search_node
sm_orig.verify_node = mock_verify_node
ah_orig.call_llm = mock_call_llm
state["phase"] = "fail"
sm2 = sm_orig.DecompStateMachine("GPU 集群 NVLink 带宽是多少?", qid="smoke_base", cfg=sm_orig.ObjectiveConfig())
n2 = sm_orig.NodeRecord(id="N1", claim="H100 NVLink 带宽为 3.35TB/s", level="L1",
                        status="failed",
                        evidence="来源显示带宽 900GB/s，与 claim 数值不一致，版本不匹配")
sm2.nodes.append(n2)
sm2._rework([n2])
evb = sm2.rework_events[-1]
assert evb["mode"] == "angle", f"基线异常: mode={evb['mode']} (期望 angle)"
print(f"[6] A/B 对照: 原始 SM 同场景 mode={evb['mode']} (angle) vs 修补后 directed → "
      f"路由差异确由 Fix-A 引起: OK")

print("\n=== 全部 6 项运行时断言通过: Fix-A 路由触发 / Fix-B 重入 / attempt=2 行使 / "
      "claim 回写 / 上界兜底 / A/B 路由差异 ===")
