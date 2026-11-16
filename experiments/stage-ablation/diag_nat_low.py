# nat 低分诊断（2026-11-16）：重跑 2 个低分 run，落盘 answer + judge 逐点，定位漏哪些要点
# 背景：10-run mean=0.5166 gate FAIL（0.5801），分数双峰（0.833×3 / 0.667×2 / 0.333×3 / 0.167×2），
#       低分 run 的 hallucination_flags 更高（3-13 vs 2-3）。10-run 没存 answer，无法逐点归因。
# 方法：复用 synthesize_answer（返回 judge 含逐点 scores+reasons），跑 2 次，落盘完整 judge。
import json, time
from s5_state_machine import NodeRecord, synthesize_answer
from s5_pipeline import QUESTIONS

QID = "nat"
d = json.load(open(f'runs-s5-sm-{QID}.json'))
nodes = [NodeRecord(**n) for n in d['nodes']]
print(f'diag: {QID} {len(nodes)} nodes, 2 runs', flush=True)

out = []
for i in range(2):
    t0 = time.time()
    s = synthesize_answer(QUESTIONS[QID], nodes, QID)
    out.append({
        'run': i + 1,
        'coverage': s['coverage'],
        'depth': s['depth'],
        'judge': s['judge'],
        'answer': s['answer'],
        'wall_s': round(time.time() - t0),
    })
    j = s['judge']
    scores = j.get('scores') or []
    print(f'run {i+1}: cov={s["coverage"]} scores={scores} hf={len(j.get("hallucination_flags") or [])} {time.time()-t0:.0f}s', flush=True)
    for k, (sc, rs) in enumerate(zip(scores, j.get('reasons') or [])):
        print(f'  要点{k+1}: {sc} | {rs}', flush=True)

json.dump(out, open('runs-s5-sm-nat-lowdiag.json', 'w'), ensure_ascii=False, indent=2)
print('saved → runs-s5-sm-nat-lowdiag.json', flush=True)
