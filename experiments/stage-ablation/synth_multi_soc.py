# 多次综合取 mean 判 gate（2026-11-16）
# 背景：单次综合方差大（同树两次 1.0 vs 0.857），gate 必须用 mean（S0 基线是 100 reps mean）。
# 用法：python3 synth_multi_soc.py [N] [qid]   （qid: soc/nat，默认 soc）
# 复用 s5_state_machine.synthesize_answer()，对现有 SM 节点树跑 N 次综合，
# 收集 coverage，算 mean，与 gate / S0 基线对比。
import json, sys, time
from s5_state_machine import NodeRecord, synthesize_answer
from s5_pipeline import QUESTIONS

N = int(sys.argv[1]) if len(sys.argv) > 1 else 10
QID = sys.argv[2] if len(sys.argv) > 2 else "soc"
GATES = {"soc": 0.898, "nat": 0.634}
BASELINES = {"soc": 0.8957, "nat": 0.634}
GATE = GATES[QID]
BASELINE = BASELINES[QID]

d = json.load(open(f'runs-s5-sm-{QID}.json'))
nodes = [NodeRecord(**n) for n in d['nodes']]
print(f'multi-synth: {QID} {len(nodes)} nodes, N={N}', flush=True)

covs, depths, hflags = [], [], []
t_start = time.time()
for i in range(N):
    t0 = time.time()
    try:
        s = synthesize_answer(QUESTIONS[QID], nodes, QID)
        covs.append(s['coverage'])
        depths.append(s['depth'])
        hflags.append(len(s['judge'].get('hallucination_flags') or []))
        print(f'run {i+1}/{N}: coverage={s["coverage"]} depth={s["depth"]} hf={hflags[-1]} {time.time()-t0:.0f}s', flush=True)
    except Exception as e:
        print(f'run {i+1}/{N} FAILED: {type(e).__name__}: {e}', flush=True)
        covs.append(None); depths.append(None); hflags.append(None)

valid = [c for c in covs if c is not None]
mean = sum(valid)/len(valid) if valid else None
import statistics
sd = statistics.pstdev(valid) if len(valid) > 1 else None
print(f'\n=== RESULT ({QID}) ===', flush=True)
print(f'valid runs: {len(valid)}/{N}', flush=True)
print(f'coverage mean = {mean}', flush=True)
print(f'coverage sd   = {sd}', flush=True)
print(f'coverage min/max = {min(valid)}/{max(valid)}', flush=True)
print(f'gate {GATE}: {"PASS" if mean and mean >= GATE else "FAIL"}', flush=True)
print(f'S0 baseline {BASELINE}: {"above" if mean and mean >= BASELINE else "below"}', flush=True)
print(f'total wall = {time.time()-t_start:.0f}s', flush=True)
json.dump({
    'qid': QID, 'n': N, 'valid': len(valid), 'covs': covs, 'depths': depths,
    'hflags': hflags, 'mean': mean, 'sd': sd,
    'gate': GATE, 'gate_pass': bool(mean and mean >= GATE),
    'baseline': BASELINE, 'wall_s': time.time()-t_start,
}, open(f'runs-s5-sm-{QID}-synth-multi.json', 'w'), ensure_ascii=False, indent=2)
print(f'saved → runs-s5-sm-{QID}-synth-multi.json', flush=True)