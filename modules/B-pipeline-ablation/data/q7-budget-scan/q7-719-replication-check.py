#!/usr/bin/env python3
"""719 r1 vs r2 机制复现核验 — 单 rep 悬念的直接答案.

上轮 (q7-719-marginal-mechanism-20261124.md) 的 L5 发现是单 rep (r1) 对单 rep (300-r1),
标了诚实边界: "若 r2/r3 也没长出 L5, 则'719 长出 L5'是 r1 偶然, 机制结论要降级".
本脚本在 r2 落盘后一键判定: r2 是否复现 ① 长出 L5 ② 核验稀释 ③ 冗余暴涨.

用法: python3 q7-719-replication-check.py
  - r2 不存在 → 打印 r1 基线 + "r2 pending", 退出码 0
  - r2 存在   → 打印 r1/r2 对比 + 复现判定, 退出码 0
不写文件, 纯读. r1/r2 文件名自动 glob (q7-719-r{1,2}-*.json).
"""
import glob, json, os, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(tag, budget=719):
    """tag='r1' → q7-{budget}-r1-*.json; tag='300-r1' → q7-300-r1-*.json (跨 budget 基线)."""
    if '-' in tag:
        pat = f'q7-{tag}-*.json'
    else:
        pat = f'q7-{budget}-{tag}-*.json'
    fs = sorted(glob.glob(os.path.join(HERE, pat)))
    if not fs:
        return None
    return json.load(open(fs[-1]))


def _lvl(v):
    """'L5' -> 5, 5 -> 5, None -> 0"""
    if v is None:
        return 0
    if isinstance(v, int):
        return v
    s = str(v).upper().replace('L', '').strip()
    return int(s) if s.isdigit() else 0


def struct(d):
    nodes = d['nodes']
    n = len(nodes)
    st = Counter(nd['status'] for nd in nodes)
    lv = Counter(_lvl(nd.get('level')) for nd in nodes)
    ver_by_lv = {}
    for nd in nodes:
        l = _lvl(nd.get('level'))
        ver_by_lv.setdefault(l, [0, 0])
        ver_by_lv[l][1] += 1
        if nd['status'] == 'verified':
            ver_by_lv[l][0] += 1
    dr = sum(r.get('dropped_redundant', 0) for r in d.get('rounds', []))
    return {
        'n': n,
        'max_level': max(lv) if lv else 0,
        'l5_nodes': lv.get(5, 0),
        'l5_verified': ver_by_lv.get(5, [0, 0])[0],
        'verified_rate': st.get('verified', 0) / n,
        'l4_verified_rate': (ver_by_lv.get(4, [0, 0])[0] / ver_by_lv.get(4, [0, 0])[1]) if ver_by_lv.get(4, [0, 0])[1] else float('nan'),
        'dropped_redundant': dr,
    }


def judge_of(tag):
    """judge 分在 q7-scan-scores.json, 按 run 名匹配; 找不到返回 None."""
    sp = os.path.join(HERE, 'q7-scan-scores.json')
    if not os.path.exists(sp):
        return None
    scores = json.load(open(sp))
    entries = scores if isinstance(scores, list) else scores.get('entries', [])
    for e in entries:
        if not isinstance(e, dict):
            continue
        if e.get('budget') == 719 and e.get('rep') == int(tag[1:]):
            for k in ('judge_total', 'judge', 'score'):
                v = e.get(k)
                if isinstance(v, dict):
                    return v.get('total')
                if v is not None:
                    return v
    return None


def main():
    r1 = load('r1')
    if r1 is None:
        print('r1 不存在, 无法核验'); sys.exit(1)
    s1 = struct(r1)
    j1 = judge_of('r1')
    print('== 719 机制复现核验 ==')
    print(f"r1: n={s1['n']} max_L=L{s1['max_level']} L5={s1['l5_nodes']}({s1['l5_verified']}ver) "
          f"ver_rate={s1['verified_rate']:.3f} L4_ver={s1['l4_verified_rate']:.2f} "
          f"redundant={s1['dropped_redundant']} judge={j1}")
    r2 = load('r2')
    if r2 is None:
        print('r2 pending — r1 基线已打印, r2 落盘后重跑本脚本.')
        sys.exit(0)
    s2 = struct(r2)
    j2 = judge_of('r2')
    print(f"r2: n={s2['n']} max_L=L{s2['max_level']} L5={s2['l5_nodes']}({s2['l5_verified']}ver) "
          f"ver_rate={s2['verified_rate']:.3f} L4_ver={s2['l4_verified_rate']:.2f} "
          f"redundant={s2['dropped_redundant']} judge={j2}")
    # 复现判定: 三个机制特征 (跨预算签名, 基线=300 独立 run, 非 r1 同 budget 内比较)
    # 机制结论 (marginal-mechanism 文档) 是 300→719 的签名: ver 0.720→0.647, redundant 43→371.
    # 复现问题 = "r2@719 相对 300 基线是否也有同样签名", 不是 "r2 是否比 r1 更稀释".
    base = load('300-r1')  # 300 独立 run (ver=0.720, redundant=43)
    if base is not None:
        sb = struct(base)
        base_ver, base_red = sb['verified_rate'], sb['dropped_redundant']
    else:
        base_ver, base_red = s1['verified_rate'], s1['dropped_redundant']  # 300 缺失时退回 r1 (有偏差)
    l5_replicates = s2['l5_nodes'] > 0 and s2['max_level'] >= 5
    dilution_replicates = s2['verified_rate'] < base_ver
    redundancy_replicates = s2['dropped_redundant'] > base_red
    if base is not None:
        print(f"[基线=300-r1: ver={base_ver:.3f} redundant={base_red}]")
    verdicts = {
        'L5 长出': l5_replicates,
        '核验稀释(verified率降)': dilution_replicates,
        '冗余暴涨': redundancy_replicates,
    }
    n_pass = sum(verdicts.values())
    print(f"\n机制复现: L5={verdicts['L5 长出']} 稀释={verdicts['核验稀释(verified率降)']} "
          f"冗余={verdicts['冗余暴涨']}  ({n_pass}/3)")
    if n_pass == 3:
        print('→ 机制复现成立: 719 的 L5 生长+稀释+冗余不是 r1 偶然, 可落 workshop.')
    elif n_pass >= 1:
        print('→ 部分复现: 机制部分稳健, 需人工判读哪些特征成立, 谨慎落文.')
    else:
        print('→ 不复现: r1 的 L5 是偶然, 机制结论降级, 不落 workshop.')


if __name__ == '__main__':
    main()
