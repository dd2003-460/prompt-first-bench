#!/usr/bin/env python3
"""claim vs evidence 字段分离 — (a)→(b) 触发链检验 (补充40)

背景: 补充29/31/36 把 DEFENSIVE_RE 命中当整体信号, 得出"(a)→(b) 触发链不存在,
方向是 (b)→(a)"。这是错的 — 混淆了 decompose 时(检索前)写的 claim 和 verify 时
(检索后)写的 evidence。

本脚本分离:
- claim 里的缺口标记 (decompose 时写, 检索前) = (a) 信号
- evidence 里的缺口标记 (verify 时写, 检索后) = (b)→(a) 批判信号
- search_query 非空 (decompose 时生成) = 真正的 (a)→(b) 触发器

时序 (s5_state_machine.py line 590/593): 模型 decompose 时一次性写
claim + source + search_query, 之后才检索, verify 写 evidence。
所以 claim 缺口标记是检索前写的。

prompt 混杂 (prompts.py):
- line 78/312: 定性结论标 [待核验]
- line 332: claim 含 [待核验] 且存在可检索来源 → 必须给 search_query
- line 109/337: 每个节点带检索词
所以 [待核验]→search_query 是 prompt 机械触发, 不是模型自发决定。
"""
import json, glob, os, re, sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from metacog_axis import DEFENSIVE_RE

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
TAG = re.compile(r'\[待核验\]')
OTHER = re.compile(r'不确定|未验证|待确认|需要验证|无法确定|缺乏数据|信息不足')


def load_rep():
    nodes = []
    for f in glob.glob(os.path.join(ROOT, 'modules/B-pipeline-ablation/data/rep-scan/rep-*.json')):
        if f.endswith('scores.json'):
            continue
        t = json.load(open(f))
        nodes += t if isinstance(t, list) else t.get('nodes', [])
    return nodes


def load_dom(dom):
    seen = set()
    nodes = []
    for f in glob.glob(os.path.join(ROOT, f'experiments/stage-ablation/checkpoints/archive/sm-{dom}-*/sm-{dom}-r*/**/node.json'), recursive=True):
        try:
            n = json.load(open(f))
        except Exception:
            continue
        k = (n.get('id'), str(n.get('level', '')), n.get('source'), n.get('status'), str(n.get('claim', ''))[:60])
        if k in seen:
            continue
        seen.add(k)
        nodes.append(n)
    return nodes


def z2(p1, n1, p2, n2):
    if n1 == 0 or n2 == 0:
        return float('nan')
    p = (p1 * n1 + p2 * n2) / (n1 + n2)
    if not 0 < p < 1:
        return float('nan')
    return (p1 - p2) / (p * (1 - p) * (1 / n1 + 1 / n2)) ** 0.5


def main():
    print('=== claim vs evidence 字段分离 (补充40) ===\n')
    for label, nodes in [('GPU', load_rep()), ('NAT', load_dom('nat')), ('SOC', load_dom('soc'))]:
        cd = [n for n in nodes if DEFENSIVE_RE.search(str(n.get('claim', '')))]
        nd = [n for n in nodes if not DEFENSIVE_RE.search(str(n.get('claim', '')))]
        ed = [n for n in nodes if DEFENSIVE_RE.search(str(n.get('evidence', '')))]
        print(f'{label}: n={len(nodes)}')
        print(f'  claim 缺口标记 (decompose, 检索前): {len(cd)} ({len(cd)/len(nodes)*100:.1f}%)')
        print(f'  evidence 缺口标记 (verify, 检索后): {len(ed)} ({len(ed)/len(nodes)*100:.1f}%)')

        def hasq(ns):
            return sum(1 for n in ns if str(n.get('search_query', '')).strip())
        cq = hasq(cd) / len(cd) if cd else 0
        nq = hasq(nd) / len(nd) if nd else 0
        z = z2(cq, len(cd), nq, len(nd))
        print(f'  claim缺口 search_query 率: {cq*100:.0f}% vs 无缺口 {nq*100:.0f}% (z={z:+.2f})')
        # 排除混杂: [待核验] vs 其余
        tag = [n for n in nodes if TAG.search(str(n.get('claim', '')))]
        oth = [n for n in nodes if OTHER.search(str(n.get('claim', ''))) and not TAG.search(str(n.get('claim', '')))]
        for lab, ns in [('[待核验] prompt指示', tag), ('其余7词 自发', oth)]:
            q = hasq(ns) / len(ns) if ns else 0
            print(f'  {lab}: n={len(ns)}, search_query 率={q*100:.0f}%')
        print()


if __name__ == '__main__':
    main()
