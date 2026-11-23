#!/usr/bin/env python3
"""r8 落地后一键: 评分 → rep-scan-scores.json → era-matched.json → 重跑 analyze。

用法: python3 land_rep_run.py <rep-json 路径>
例:   python3 land_rep_run.py modules/B-pipeline-ablation/data/rep-scan/rep-300-r8-20261123-XXXXXX.json
"""
import json, re, sys, glob, os

PFB = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RDIR = f'{PFB}/modules/B-pipeline-ablation/data/rep-scan'
SCORES = f'{RDIR}/rep-scan-scores.json'
ERA = f'{RDIR}/era-matched.json'

sys.path.insert(0, f'{PFB}/modules/B-pipeline-ablation')
from judge_v1 import judge_run
from metacog_axis import compute_metacog, load_run_nodes

def main(path):
    fn = os.path.basename(path)
    m = re.match(r'rep-(\d+)-r(\d+)-\d{8}-\d{6}\.json$', fn)
    if not m:
        sys.exit(f'文件名不匹配 rep-<budget>-r<rep>-<ts>.json: {fn}')
    budget, rep = int(m.group(1)), int(m.group(2))

    # 1) 评分
    j = judge_run(path)
    nodes = load_run_nodes(path)
    met = compute_metacog(nodes)
    n_nodes = len(nodes)

    depth = j['layers']['structure']['depth_score']
    cov = j['layers']['coverage']['score']

    # 2) 追加 scores (dedupe by budget+rep)
    sc = json.load(open(SCORES))
    sc = [r for r in sc if not (r['budget'] == budget and r['rep'] == rep)]
    sc.append({
        'budget': budget, 'rep': rep, 'n_nodes': n_nodes,
        'judge': {'total': j['total_score'], 'depth': depth, 'cov': cov},
        'metacog': {'total': met['metacog_total'], 'gap': met['gap_rate'], 'ret': met['retrieval_rate'],
                    'hg': met['healthy_gap_rate'], 'post': met['post_retrieval_accuracy']},
    })
    json.dump(sc, open(SCORES, 'w'), ensure_ascii=False, indent=1)

    # 3) 追加 era-matched (dedupe by budget+rep)
    era = json.load(open(ERA))
    era = [r for r in era if not (r['budget'] == budget and r['rep'] == rep)]
    era.append({'budget': budget, 'rep': rep, 'n_nodes': n_nodes,
                'depth': depth, 'cov': cov,
                'total': j['total_score'], 'era': 'frozen-mech'})
    json.dump(era, open(ERA, 'w'), ensure_ascii=False, indent=1)

    print(f'landed {fn}: n={n_nodes} judge={j["total_score"]:.4f} (depth={depth}, cov={cov:.4f}) '
          f'metacog={met["metacog_total"]:.3f} (gap={met["gap_rate"]:.4f}, ret={met["retrieval_rate"]:.3f})')
    print(f'scores={len(sc)} records, era-matched={len(era)} trees')
    print('下一步: python3 rep_scan_analyze.py  (重跑分析)')

if __name__ == '__main__':
    main(sys.argv[1])
