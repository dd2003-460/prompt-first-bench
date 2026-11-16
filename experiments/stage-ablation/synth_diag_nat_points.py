# nat 逐点诊断（2026-11-16）
# 目的：跑 N 次综合，保存逐点 0/1 打分，看漏点分布
# 判定 nat gate FAIL 是系统性问题（GOLD 措辞/judge 理解）还是方差问题（综合深度/扰动）
import json, time, sys
from s5_state_machine import NodeRecord, synthesize_answer
from s5_pipeline import QUESTIONS
from s8b_pilot import GOLD

QID = "nat"
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3
d = json.load(open(f'runs-s5-sm-{QID}.json'))
nodes = [NodeRecord(**n) for n in d['nodes']]
gold = GOLD[QID]
print(f'nat per-point diag: {len(nodes)} nodes, N={N}, {len(gold)} gold points', flush=True)

results = []
for i in range(N):
    t0 = time.time()
    try:
        s = synthesize_answer(QUESTIONS[QID], nodes, QID)
        scores = s['judge'].get('scores', [])
        reasons = s['judge'].get('reasons', [])
        results.append({'run': i+1, 'coverage': s['coverage'], 'scores': scores,
                        'reasons': reasons, 'wall': round(time.time()-t0, 1)})
        print(f'run {i+1}/{N}: cov={s["coverage"]} scores={scores} {time.time()-t0:.0f}s', flush=True)
    except Exception as e:
        print(f'run {i+1}/{N} FAILED: {type(e).__name__}: {e}', flush=True)
        results.append({'run': i+1, 'error': f'{type(e).__name__}: {e}'})

# 漏点分布
print('\n=== 漏点分布（X/N 次漏） ===', flush=True)
for gi, gp in enumerate(gold):
    miss_runs = [r['run'] for r in results
                 if r.get('scores') and gi < len(r['scores']) and r['scores'][gi] == 0]
    print(f'要点{gi+1}（{len(miss_runs)}/{len(results)} 次漏）: {gp[:70]}', flush=True)
    if miss_runs:
        for r in results:
            if r['run'] in miss_runs and r.get('reasons') and gi < len(r['reasons']):
                print(f'   judge 理由(run {r["run"]}): {r["reasons"][gi][:160]}', flush=True)
                break

json.dump(results, open('runs-s5-sm-nat-points-diag.json', 'w'), ensure_ascii=False, indent=2)
print('\nsaved → runs-s5-sm-nat-points-diag.json', flush=True)