#!/usr/bin/env python3
"""60.6% URL retention gap 固化 (T-JUDGE-1-L3 §3, draft §6 provenance gap)

承重数字: 全 19 树 2196 个 search 节点, 1330 个无 URL (60.6% 缺口)。
口径 (与 source_verify.collect_trees 一致):
  19 树 = 6 idea2 (data/idea2/idea2-*.json, 排除 scores/run)
        + 13 K7 budget-* (archive/budget-*/runs-s5-sm-gpu.json)
  "无 URL" = source=='search' 且 retrieval_sources 里没有非空 url
  性质分解 (3b): 无 URL 节点查 evidence/corrected_claim 的引用痕迹
    (来源[n]/参考/根据/检索/搜索/查到) → 80% 管道丢源 vs 20% 疑似虚标
"""
import json, glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
IDEA2 = os.path.join(ROOT, 'modules', 'B-pipeline-ablation', 'data', 'idea2')
K7 = os.path.join(ROOT, 'experiments', 'stage-ablation', 'checkpoints', 'archive')

CITE_RE = re.compile(r'来源\s*\[|参考|根据|检索|搜索|查到|引用')


def collect_trees():
    trees = []
    for f in sorted(glob.glob(os.path.join(IDEA2, 'idea2-*.json'))):
        if 'scores' in f or 'run' in f:
            continue
        trees.append(('idea2', os.path.basename(f).replace('.json', ''), f))
    for f in sorted(glob.glob(os.path.join(K7, 'budget-*/runs-s5-sm-gpu.json'))):
        tag = f.split('/archive/')[1].split('/')[0]
        trees.append(('K7', tag, f))
    return trees


def has_url(nd):
    rs = nd.get('retrieval_sources') or []
    return any(r.get('url') for r in rs if isinstance(r, dict))


def main():
    trees = collect_trees()
    # 双口径:
    #   全量 = 所有现存树 (当前 21 = 6 idea2 + 15 K7)
    #   19 树 = 排除 channel-outage 的 idea2 r3 (A-r3/B-r3, 见 T-JUDGE-1-L3 contamination note)
    #          —— 复现原始 60.6% (1330/2196); r3 是死通道期间跑的, URL retention 低是通道问题
    def is_outage_r3(fam, tag):
        return fam == 'idea2' and (tag.startswith('idea2-A-r3') or tag.startswith('idea2-B-r3'))

    def compute(exclude_outage):
        n_search = n_nourl = cite_trace = 0
        per_tree = []
        for fam, tag, path in trees:
            if exclude_outage and is_outage_r3(fam, tag):
                continue
            try:
                d = json.load(open(path))
            except Exception:
                continue
            ns = [nd for nd in d.get('nodes', []) if nd.get('source') == 'search']
            no = [nd for nd in ns if not has_url(nd)]
            ct = sum(1 for nd in no
                     if CITE_RE.search((nd.get('evidence') or '') + ' ' + (nd.get('corrected_claim') or '')))
            n_search += len(ns)
            n_nourl += len(no)
            cite_trace += ct
            if ns:
                per_tree.append((fam, tag, len(ns), len(no), len(no) / len(ns) * 100))
        return n_search, n_nourl, cite_trace, per_tree

    for label, excl in [("全量 (所有现存树)", False), ("19 树 (排除 outage idea2 r3)", True)]:
        n_search, n_nourl, cite_trace, per_tree = compute(excl)
        print(f"\n=== {label}: {len(per_tree)} 树 ===")
        print(f"search_nodes={n_search}  no_url={n_nourl}  gap={n_nourl / n_search * 100:.1f}%")
        print(f"无URL中: 有引用痕迹(管道丢源)={cite_trace} ({cite_trace / n_nourl * 100:.0f}%)  "
              f"无痕迹(疑似虚标)={n_nourl - cite_trace} ({(n_nourl - cite_trace) / n_nourl * 100:.0f}%)")
        if not excl:
            print("per-tree (search / 无URL / 无URL%):")
            for fam, tag, ns, no, pct in sorted(per_tree, key=lambda r: -r[4]):
                print(f"  {fam}/{tag}: {ns} / {no} / {pct:.0f}%")


if __name__ == '__main__':
    main()
