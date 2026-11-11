"""r7 现象复现探针：同题 L1 skeleton 跑 N 次，看「不确定性/横切维度」是否自发出现。
单步脚本（非状态机 run），落盘 research/l1-repro-probe.jsonl。"""
import sys, json, time
sys.path.insert(0, 'experiments/stage-ablation')
from s5_pipeline import P1_L1_SKELETON, _extract_json
from s8b_pilot import QUESTIONS
from ablation_harness import call_llm

N_RUNS = int(sys.argv[1]) if len(sys.argv) > 1 else 3
q = QUESTIONS['gpu']
out_path = 'research/l1-repro-probe.jsonl'
with open(out_path, 'w') as f:
    for i in range(N_RUNS):
        t0 = time.time()
        prompt = P1_L1_SKELETON.format(question=q)
        out, usage = call_llm(prompt, max_tokens=2048, temperature=0.7, top_p=0.95, retries=2)
        d = _extract_json(out or '') or {}
        dims = [x.get('name','') for x in (d.get('dimensions') or []) if isinstance(x, dict)]
        crosscut = [n for n in dims if any(k in n for k in ('不确定','置信','风险','溯源','条件性','敏感'))]
        rec = {'run': i+1, 't_s': round(time.time()-t0,1), 'dims': dims,
               'crosscut_hits': crosscut,
               'objective_composition': str(d.get('objective',{}).get('composition',''))[:120]}
        print(f"[probe {i+1}/{N_RUNS}] {len(dims)} dims, crosscut={crosscut}, {rec['t_s']}s", flush=True)
        for dd in dims: print(f"   - {dd[:60]}", flush=True)
        f.write(json.dumps(rec, ensure_ascii=False)+'\n'); f.flush()
print("saved ->", out_path)
