#!/usr/bin/env python3
"""B4: 跨域 judge_v1 重评 (structural 轴 general 性验证)

逻辑:
  ① Q6 runs × Q6 gold  → 域内分 (预期: 随 budget 升, 复现 gpu 的 3 级台阶)
  ② Q6 runs × GPU gold → 跨域分 (预期: cov 显著低于域内, 证明 gold 域特异性)
  ③ GPU runs × Q6 gold → 反向跨域 (对称检验)
  结论: 若 ① 复现台阶且 ②③ 的 cov 系统性低于 ①, 则 structural 轴的
        budget 响应是 general 的 (跨域), gold 特异性只影响绝对值不影响形状。

口径: judge_v1 冻结版 (0.5*struct+0.5*cov), 不重算公式。
输入: Q6 runs (q6-budget-scan/archive/) + gold-q6-units.json + gold-gpu-units.json
输出: 控制台 + modules/B-pipeline-ablation/data/q6-budget-scan/b4-cross-judge.json
"""
import json, os, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'modules', 'B-pipeline-ablation'))
from judge_v1 import judge_run

Q6 = os.path.join(ROOT, 'modules', 'B-pipeline-ablation', 'data', 'q6-budget-scan')
DATA = os.path.join(ROOT, 'modules', 'B-pipeline-ablation', 'data')
GPU_RUN = os.path.join(ROOT, 'experiments', 'stage-ablation', 'runs-s5-sm-gpu.json')


def load_units(p):
    return json.load(open(p)) if os.path.exists(p) else None


def score(run_json, gold_units):
    try:
        r = judge_run(run_json, gold_units=gold_units)
        L = r.get('layers', {})
        return {
            'total': r.get('total_score'),
            'struct': L.get('structure', {}).get('score'),
            'cov': L.get('coverage', {}).get('score'),
            'depth': L.get('structure', {}).get('depth'),
            'mean_depth': L.get('structure', {}).get('mean_depth'),
        }
    except Exception as e:
        return {'error': str(e)[:120]}


def main():
    gold_q6 = load_units(os.path.join(DATA, 'gold-q6-units.json'))
    gold_gpu = load_units(os.path.join(DATA, 'gold-gpu-units.json'))
    if not gold_q6:
        print("gold-q6-units.json 缺失, 先跑 gold_md_to_units")
        return
    print(f"gold: q6={len(gold_q6)} units, gpu={len(gold_gpu) if gold_gpu else 'MISSING'}")

    q6_runs = sorted(glob.glob(os.path.join(Q6, 'q6-*.json')))  # run json 直接在 Q6/ (非 archive/)
    print(f"Q6 runs: {len(q6_runs)}")
    results = []
    for rf in q6_runs:
        tag = os.path.basename(os.path.dirname(rf))
        s_in = score(rf, gold_q6)
        s_x = score(rf, gold_gpu) if gold_gpu else {'error': 'no gpu gold'}
        results.append({'run': tag, 'in_domain': s_in, 'cross_gpu_gold': s_x})
        print(f"  {tag}: in={s_in.get('total', s_in.get('error'))} "
              f"cross={s_x.get('total', s_x.get('error'))}")

    # 反向: gpu run × q6 gold
    if os.path.exists(GPU_RUN):
        rev = score(GPU_RUN, gold_q6)
        print(f"  gpu-run × q6-gold (反向跨域): {rev}")
        results.append({'run': 'gpu-canonical', 'reverse_cross': rev})

    out = os.path.join(Q6, 'b4-cross-judge.json')
    json.dump(results, open(out, 'w'), ensure_ascii=False, indent=1)
    print(f"\n→ {out}")


if __name__ == '__main__':
    main()
