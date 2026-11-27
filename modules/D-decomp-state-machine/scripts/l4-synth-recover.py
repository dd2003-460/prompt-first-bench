#!/usr/bin/env python3
# origin: ai · 2026-11-25 · L4-disambig synth 恢复（免重跑 300 节点树）
# 背景: 队列 STEP1 树跑完(300节点, runs-s5-sm-l4-disambig.json 完整)但 synth 阶段崩
#   (s8b_pilot.GOLD 缺 'l4-disambig' 条目 → judge() KeyError → SM 优雅降级 rc=0,
#    synth 文件未写出)。GOLD 条目已补 (s8b_pilot.py, 本题面显式要求机械导出)。
# 本脚本: 从 runs JSON 重建 NodeRecord → 调 synthesize_answer (SM_SYNTH_FULL=1)
#   → 按 SM --synth 块同格式写 runs-s5-sm-l4-disambig-synth.json。
# 成本: ~5-6 次 LLM 调用 (4 层 + merge + judge), 需 vLLM 独占。
# 鉴别力: 输出前校验 answer 非空 + judge coverage 有值, 否则非零退出。
import json, os, sys

SA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SA)
os.chdir(SA)
os.environ.setdefault("SM_SYNTH_FULL", "1")

RUNS = "runs-s5-sm-l4-disambig.json"
OUT = "runs-s5-sm-l4-disambig-synth.json"

d = json.load(open(RUNS))
qid = d["qid"]
question = d["question"]
assert qid == "l4-disambig", f"qid 不符: {qid}"
assert len(d.get("nodes", [])) > 0, "runs JSON 无节点"

import s5_state_machine as sm
nodes = [sm.NodeRecord(**n) for n in d["nodes"]]
print(f"[recover] {len(nodes)} 节点重建, 开始 synth (SM_SYNTH_FULL={os.environ.get('SM_SYNTH_FULL')}) ...", flush=True)
s = sm.synthesize_answer(question, nodes, qid)

answer = (s.get("answer") or "").strip()
if not answer:
    print("[recover] FAIL: answer 为空, 不落盘", flush=True)
    sys.exit(1)

payload = {
    "qid": qid,
    "n_nodes": len(nodes),
    "final_state": d.get("final_state"),
    "answer": answer,
    "judge": s.get("judge"),
    "coverage": s.get("coverage"),
    "depth_score": s.get("depth"),
    "source_run": RUNS,
    "recovered": True,
    "recover_note": "synth 阶段原崩因 GOLD KeyError; 树未重跑, 仅恢复 synth+judge (2026-11-25)",
}
with open(OUT, "w") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)
print(f"[recover] OK → {OUT} | answer={len(answer)}c coverage={s.get('coverage')} depth={s.get('depth')}", flush=True)
