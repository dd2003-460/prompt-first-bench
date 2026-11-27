#!/usr/bin/env python3
# 一次性诊断（2026-11-16）：给 SM 的 283 节点 soc 树补"综合→judge"，产出可比 judge.coverage
#
# 背景：gate "soc cov ≥ 0.898" 的 0.898 是 S0 的 judge.coverage
#       （runs-s5-prod S5-soc 100 reps mean=0.8957，ts=2026-11-08）。
#       SM 管线（s5_state_machine.py）跑完只有节点树、没有 answer 综合步骤，
#       0.781 是节点 verified 率——两个不同指标，没法直接比。
#       阶段定义 phase1-fix-pipeline 明确写着"修复 P4 synthesis gap"，证实这是已知待修项。
#
# 方法：照抄 s5_pipeline.py:883-903 的分段综合（>200 节点按层分段 + merge），
#       再调 s8b_pilot.judge（soc gate 指标）+ judge_v2_depth.score_run（depth 对照）。
#       复用现成代码，不重复造轮子。
#
# 输出：runs-s5-sm-soc-synth.json（answer + judge + coverage + depth_score + gate 判定）
import json, time, sys, random
from collections import defaultdict
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation')
from ablation_harness import call_llm
from s8b_pilot import judge
from judge_v2_depth import score_run

def _perturb():
    # 照抄 s5_pipeline.py:260
    return "".join(random.choice(["\u200b", "\u200c", " ", "\u200d"]) for _ in range(4))

base = '/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation'
QID = sys.argv[1] if len(sys.argv) > 1 else 'soc'
d = json.load(open(f'{base}/runs-s5-sm-{QID}.json'))
nodes = d['nodes']
question = d['question']
n_ver = sum(1 for n in nodes if n['status'] == 'verified')
print(f'load {len(nodes)} nodes (verified {n_ver}), question {len(question)} chars', flush=True)

# ── 按层分段综合（照抄 s5_pipeline.py:883-903）──
by_lv = defaultdict(list)
for n in nodes:
    by_lv[n.get('level', '?')].append(n)
parts = []
for lv in sorted(by_lv, key=lambda x: str(x).lstrip('L')):
    seg = "\n".join(
        f"{n['id']} ({lv}): {n.get('corrected_claim') or n['claim']}  "
        f"[status={n['status']}; evidence: {(n.get('evidence') or '')[:80]}]"
        for n in by_lv[lv])
    p = (f"你是研究员。基于下面第 {lv} 层的已核验事实，回答原问题中该层涉及的部分。"
         f"只写结论+数值/公式，每条标来源条目 id，不要重复其他层的内容。\n\n"
         f"【问题】\n{question}\n\n【第 {lv} 层事实】\n{seg}") + _perturb()
    t0 = time.time()
    out_l, _ = call_llm(p, max_tokens=4000, temperature=0.7, top_p=0.95)
    parts.append(f"=== 第 {lv} 层 ===\n{out_l or '(空)'}")
    print(f'  {lv}: {len(by_lv[lv])} 节点, in={len(seg)}c, out={len(out_l or "")}c, {time.time()-t0:.0f}s', flush=True)

merge_p = (f"你是研究员。下面是同一道问题按目录树分层得到的各层结论摘要。"
           f"请把它们合并成一份完整最终答案：覆盖问题全部子问，保留所有具体数值/公式/排序，"
           f"消除层间重复，最后给一个明确的推荐结论。\n\n【问题】\n{question}\n\n"
           + "\n\n".join(parts)) + _perturb()
t0 = time.time()
answer, usage = call_llm(merge_p, max_tokens=8000, temperature=0.7, top_p=0.95)
print(f'merge: in={len(merge_p)}c, out={len(answer or "")}c, {time.time()-t0:.0f}s', flush=True)

# ── judge（gate 指标：GOLD 要点逐条 0/1 → coverage）──
t0 = time.time()
j = judge(QID, answer)
cov = round(j.get('coverage') or 0, 3)
print(f'judge coverage = {cov} {time.time()-t0:.0f}s', flush=True)

# ── depth score（对照；gpu gate 用 depth ≥ 0.50）──
depth = None
try:
    t0 = time.time()
    dv = score_run(QID, answer)
    depth = dv.get('overall')
    print(f'depth_score = {depth} {time.time()-t0:.0f}s', flush=True)
except Exception as e:
    print(f'depth score failed: {e}', flush=True)

GATES = {'soc': 0.898, 'nat': 0.634}  # S0 基线（judge.coverage mean）
BASELINE = {'soc': 0.8957, 'nat': 0.634}
out = {
    'qid': QID,
    'ts': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
    'source': f'runs-s5-sm-{QID}.json (SM 终盘)',
    'n_nodes': len(nodes),
    'n_verified': n_ver,
    'node_verified_rate': round(n_ver / len(nodes), 4),
    'answer': answer,
    'judge': j,
    'coverage': cov,
    'depth_score': depth,
    's0_baseline_coverage': BASELINE.get(QID),
    'gate': f'{QID} cov >= {GATES.get(QID)} (S0 基线)',
    'gate_pass': (cov >= GATES[QID]) if (cov is not None and QID in GATES) else None,
}
out_path = f'{base}/runs-s5-sm-{QID}-synth.json'
with open(out_path, 'w') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f'DONE → runs-s5-sm-{QID}-synth.json | coverage={cov} | gate_pass={out["gate_pass"]}', flush=True)