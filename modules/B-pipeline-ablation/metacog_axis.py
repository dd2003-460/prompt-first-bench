#!/usr/bin/env python3
"""Metacognition Axis — 自我认识维度（正交于 judge_v1.py，不碰冻结层）

AGI 完整定义三段: (a) 判断信息是否充分 + (b) 获取缺失信息 + (c) 推理到答案
  (a)+(b) = 元认知 (monitoring + control)
  (c) = 推理（27b 基线能力，非增量）

"至少有自我认识" 的可测线 = (a)+(b) 被机械测到:
  - gap_rate: 防御性标记节点占比（标了缺口 = monitoring 在工作）
  - retrieval_rate: source=search 且 status=verified 占比（真的去查了 = control 在工作）
  - post_retrieval_accuracy: search 节点中 verified/degraded 比（查完质量）
  - metacog_total: 综合分

确定性计算，不依赖 LLM，same input → same output。
输入: run json（含 nodes 字段: id/claim/evidence/source/status/search_query/retrieval_sources）
用法:
  python3 metacog_axis.py --runs-dir <dir> [--out JSON]
  python3 metacog_axis.py --run <single_run.json>
"""
import argparse, glob, json, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))

# 防御性语言标记（D 设计: 防御性语言 = 调研入口）
DEFENSIVE_PATTERNS = [
    r'\[待核验\]',
    r'不确定',
    r'未验证',
    r'待确认',
    r'需要验证',
    r'无法确定',
    r'缺乏数据',
    r'信息不足',
]
DEFENSIVE_RE = re.compile('|'.join(DEFENSIVE_PATTERNS))


def load_run_nodes(run_json_path):
    """从 run json 加载节点列表。"""
    with open(run_json_path) as f:
        d = json.load(f)
    nodes = d.get('nodes', [])
    return nodes


def compute_metacog(nodes):
    """从节点列表计算自我认识轴各指标。"""
    n_total = len(nodes)
    if n_total == 0:
        return {"n_total": 0, "gap_rate": 0, "retrieval_rate": 0,
                "post_retrieval_accuracy": 0, "metacog_total": 0,
                "n_defensive": 0, "n_search": 0, "n_search_verified": 0,
                "n_search_degraded": 0}

    # (a) monitoring: 防御性标记（标了缺口）
    n_defensive = 0
    for n in nodes:
        text = (n.get('claim', '') + ' ' + n.get('evidence', '') +
                ' ' + n.get('corrected_claim', ''))
        if DEFENSIVE_RE.search(text):
            n_defensive += 1
    gap_rate = n_defensive / n_total

    # (b) control: 真的去检索了
    source_counts = Counter(n.get('source', '') for n in nodes)
    n_search = source_counts.get('search', 0)

    # search 节点中 verified vs degraded
    n_search_verified = 0
    n_search_degraded = 0
    for n in nodes:
        if n.get('source') == 'search':
            if n.get('status') == 'verified':
                n_search_verified += 1
            elif n.get('status') == 'degraded':
                n_search_degraded += 1

    retrieval_rate = n_search / n_total  # 检索覆盖率
    # 查完质量: verified / (verified + degraded)
    n_search_resolved = n_search_verified + n_search_degraded
    post_retrieval_accuracy = (n_search_verified / n_search_resolved
                               if n_search_resolved > 0 else 0)

    # 综合: 0.4*gap + 0.3*retrieval + 0.3*post_acc
    # 权重 [待标定] — 初值拍的，补重复后用消融验证
    metacog_total = 0.4 * gap_rate + 0.3 * retrieval_rate + 0.3 * post_retrieval_accuracy

    return {
        "n_total": n_total,
        "n_defensive": n_defensive,
        "gap_rate": round(gap_rate, 4),
        "n_search": n_search,
        "retrieval_rate": round(retrieval_rate, 4),
        "n_search_verified": n_search_verified,
        "n_search_degraded": n_search_degraded,
        "post_retrieval_accuracy": round(post_retrieval_accuracy, 4),
        "metacog_total": round(metacog_total, 4),
        "source_counts": dict(source_counts),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--runs-dir', help='目录，含多个 run json')
    ap.add_argument('--run', help='单个 run json 路径')
    ap.add_argument('--out', help='输出 JSON 路径')
    args = ap.parse_args()

    if args.run:
        paths = [args.run]
    elif args.runs_dir:
        # 递归找 runs-s5-sm-*.json（archive 嵌套: budget-B-rR-*/runs-s5-sm-gpu.json）
        paths = sorted(glob.glob(os.path.join(args.runs_dir, '**', 'runs-s5-sm-*.json'), recursive=True))
        paths = [p for p in paths if 'synth' not in p and json.load(open(p)).get('nodes')]
    else:
        ap.error('需要 --runs-dir 或 --run')

    results = []
    for p in paths:
        nodes = load_run_nodes(p)
        r = compute_metacog(nodes)
        r['file'] = os.path.basename(p)
        results.append(r)
        print(f"{os.path.basename(p):50s} metacog={r['metacog_total']:.4f} "
              f"gap={r['gap_rate']:.3f} ret={r['retrieval_rate']:.3f} "
              f"post={r['post_retrieval_accuracy']:.3f} "
              f"(n={r['n_total']}, search={r['n_search']})")

    if args.out:
        with open(args.out, 'w') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\n→ {args.out} ({len(results)} runs)")


if __name__ == '__main__':
    main()
