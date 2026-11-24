#!/usr/bin/env python3
"""build_q9_units.py — 从 gold/Q9-v2.md 确定性解析 Q9-agi gold units (judge_v1 可消费).

为什么是脚本不是 LLM: units 是 gold md 树的机械转换 (37 节点 → schema),
无判断成分; 27b subagent 做这事撞输出 token 上限 (22:26 实测), 脚本可复现.

用法: /usr/bin/python3 build_q9_units.py
输入: experiments/stage-ablation/gold/Q9-v2.md (arena 交付 + Lead 侧 2/2 交叉核验)
输出: modules/B-pipeline-ablation/data/gold-q9-units.json

schema 对标 gold-q7-units.json (judge_v1.layer_coverage 只用 text 做 embedding 匹配,
unit_id/depth/kind/stop_marker/share 供记账). 额外字段 (gate/weight/conf/src/j_id)
judge_v1 忽略, 供 E 预算实验按 v2 lexicographic 语义做 gate 分析.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
GOLD_MD = os.path.join(HERE, '..', '..', 'experiments', 'stage-ablation', 'gold', 'Q9-v2.md')
OUT = os.path.join(HERE, 'data', 'gold-q9-units.json')

ROW = re.compile(r'^\|\s*(N-[0-9.]+)\s*\((\d+)\)\s*\|([^|]*)\|(.*)\|\s*$')
LEAF = re.compile(r'(J\d+)\s+(S-[abc])\s+w=([.0-9]+)\s+conf=([.0-9]+)\s+src=([^；]+)；(.*)', re.S)

def main():
    units = []
    n_leaf = n_split = 0
    with open(GOLD_MD) as f:
        for line in f:
            m = ROW.match(line.rstrip('\n'))
            if not m:
                continue
            uid, depth, parent, content = m.group(1), int(m.group(2)), m.group(3).strip(), m.group(4).strip()
            lm = LEAF.search(content)
            if lm:
                kind, stop = 'leaf', lm.group(2)
                j_id, weight, conf, src, desc = lm.group(1), float(lm.group(3)), float(lm.group(4)), lm.group(5).strip(), lm.group(6).strip()
                n_leaf += 1
            elif 'children' in content:
                kind, stop, j_id, weight, conf, src, desc = 'split', None, None, None, None, None, content
                n_split += 1
            else:
                kind, stop, j_id, weight, conf, src, desc = None, None, None, None, None, None, content
            u = {
                'unit_id': uid, 'depth': depth, 'raw': content, 'text': content,
                'kind': kind, 'stop_marker': stop, 'share': None,
                'j_id': j_id, 'weight': weight, 'conf': conf, 'src': src,
                'gate': bool(kind == 'leaf' and (uid.startswith('N-1.') or uid.startswith('N-3.'))),
            }
            units.append(u)
    assert len(units) == 37, f'expect 37 nodes, got {len(units)}'
    assert n_leaf == 21, f'expect 21 leaves, got {n_leaf}'
    js = sorted((u['j_id'] for u in units if u['j_id']), key=lambda s: int(s[1:]))
    assert js == [f'J{i}' for i in range(1, 22)], f'J ids mismatch: {js}'
    wsum = round(sum(u['weight'] for u in units if u['weight']), 4)
    gates = [u['j_id'] for u in units if u['gate']]
    doc = {
        '_schema': 'gold-md-units/v1',
        '_doc': 'build_q9_units.py 确定性解析自 gold/Q9-v2.md (37 节点/21 叶). 取代 gold/Q9.md v0 判定点段 (J1-J12 扁平加权, 已过期).',
        'source': 'experiments/stage-ablation/gold/Q9-v2.md',
        'semantics': {
            'objective': 'lexicographic: 先过硬门 (capability N-1 / reliability N-3, 不可补偿), 再在可行集内 min T/C',
            'weights': 'v2 五维 0.20 为描述性 dashboard 权重, 非优化目标; 叶权重合计 ' + str(wsum),
            'gate_units': 'gate=true 的叶 = 硬门 (J1-J5 capability, J9-J14 reliability, 按树结构 N-1.*/N-3.* 派生). lexicographic 下任一 gate 叶未命中 = 方案不可行.',
            'judge_v1_caveat': 'judge_v1.judge_run 是加权求和 (补偿性), 与 v2 lexicographic 语义不一致: 低预算 run 可能在 cost/time 叶高分掩盖 gate 失败. E 预算实验须单独分析 gate 叶命中率曲线 (gate-passing 阈值), 不能只看 judge_total 曲线.',
            'pending_D': 'tau_cap/tau_rel/可发表级/无需逐步指导 接受阈值待 D 确认, 未预设数值 (J4/J5 等 S-c 叶).',
        },
        'n_units': len(units), 'n_leaves': n_leaf, 'n_splits': n_split,
        'weight_sum': wsum, 'gate_units': gates,
        'units': units,
    }
    with open(OUT, 'w') as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(f'OK: {len(units)} units ({n_leaf} leaf / {n_split} split), weight_sum={wsum}, gates={gates}')
    print(f'written: {OUT}')

if __name__ == '__main__':
    main()
