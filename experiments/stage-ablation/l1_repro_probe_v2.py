"""r7 现象复现探针 v2：消融「2b 结构性分类」prior，看不确定性维度是否还自发出现。
A 组: 完整 P1_L1_SKELETON (含 2b)   B 组: 去掉 2b 段后的 prompt
各跑 N_RUNS 次，落盘 research/l1-repro-probe-v2.jsonl"""
import sys, json, time, re
sys.path.insert(0, 'experiments/stage-ablation')
from s5_pipeline import P1_L1_SKELETON, _extract_json
from s8b_pilot import QUESTIONS
from ablation_harness import call_llm

N_RUNS = int(sys.argv[1]) if len(sys.argv) > 1 else 3
q = QUESTIONS['gpu']

# B 组: 删除 "2b. 结构性分类..." 到 "此判据对所有题目类型成立。" 整段
full = P1_L1_SKELETON
start = full.find('2b. 结构性分类')
end = full.find('此判据对所有题目类型成立。') + len('此判据对所有题目类型成立。')
assert start != -1 and end > start, 'ablation cut points not found'
abl = full[:start] + full[end:]
print(f'[setup] full len={len(full)}, ablated len={len(abl)}, removed {len(full)-len(abl)} chars', flush=True)

KWS = ('不确定','置信','风险','溯源','条件性','敏感')
def run_one(prompt, label, i, out):
    t0 = time.time()
    o, _ = call_llm(prompt.format(question=q), max_tokens=2048, temperature=0.7, top_p=0.95, retries=2)
    d = _extract_json(o or '') or {}
    dims = [x.get('name','') for x in (d.get('dimensions') or []) if isinstance(x, dict)]
    hits = [n for n in dims if any(k in n for k in KWS)]
    rec = {'group': label, 'run': i+1, 't_s': round(time.time()-t0,1), 'dims': dims, 'crosscut_hits': hits}
    print(f"[{label} {i+1}/{N_RUNS}] {len(dims)} dims, crosscut={hits}", flush=True)
    for dd in dims: print(f"   - {dd[:55]}", flush=True)
    out.write(json.dumps(rec, ensure_ascii=False)+'\n'); out.flush()

out_path = 'research/l1-repro-probe-v2.jsonl'
with open(out_path, 'w') as out:
    for i in range(N_RUNS):
        run_one(full, 'A-full', i, out)
        run_one(abl, 'B-ablated', i, out)
print('saved ->', out_path)
