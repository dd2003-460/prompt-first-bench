#!/usr/bin/env python3
"""
B1: markdown gold tree → structured units.json (coverage 层用).

从 gold-Q*.md 的 ASCII 全树解析出 unit_id / depth / raw / text / kind(split|leaf) /
stop_marker(S-a/S-b/S-c/B#)。coverage 层只吃 text 做 embedding cosine，够用。

formulas.json (L1 物理层, sympy/ref/bound) 需人工标注，本脚本不产。

用法:
  python3 gold_md_to_units.py bench/rubric-v3/ablation/gold-Q6.md -o gold-q6-units.json
"""
import argparse, json, os, re, sys

# 树行: 前缀(│ ├─ └─ 空格) + N-id + 内容
# depth = 该行的树层级数(缩进组数)。ASCII 树每组占 2 列("│ " 或 "├─" 或 "└─")。
NODE_RE = re.compile(r'^(?P<prefix>(?:[│├└─\s])*)(?P<id>N-\d+(?:\.\d+)*)\s+(?P<rest>.*)$')
# 叶子/分裂标记
KIND_RE = re.compile(r'\b(split|leaf)\b')
STOP_RE = re.compile(r'\b(S-[abc]|B\d)\b')
# SHARE 值
SHARE_RE = re.compile(r'(?:SHARE\s*)?\.(\d{1,2})\b|\bSHARE\s+(\d+\.\d+)\b')


def tree_depth(prefix: str) -> int:
    """ASCII 树前缀 → 层级数。每组 3 列('│  ' / '├─ ' / '└─ ')。"""
    p = prefix.rstrip()
    last = -1
    for i, ch in enumerate(p):
        if ch in '├└':
            last = i
    if last < 0:
        return 0  # 根
    return last // 3 + 1


def parse_gold(md_path: str) -> list:
    units = []
    in_tree = False
    with open(md_path) as f:
        for line in f:
            line = line.rstrip('\n')
            # 进入/离开 ``` 代码块(全树在代码块里)
            if line.strip().startswith('```'):
                in_tree = not in_tree
                continue
            if not in_tree:
                continue
            m = NODE_RE.match(line)
            if not m:
                continue
            nid = m.group('id')
            rest = m.group('rest').strip()
            depth = tree_depth(m.group('prefix'))
            kind_m = KIND_RE.search(rest)
            kind = kind_m.group(1) if kind_m else None
            stop_m = STOP_RE.search(rest)
            stop = stop_m.group(1) if stop_m else None
            # share = split/leaf 关键字前一个 token(固定列), 校验形如 .35 / 1.00
            share = None
            kw = re.search(r'\b(split|leaf)\b', rest)
            if kw:
                before = rest[:kw.start()].rsplit()
                if before:
                    tok = before[-1]
                    if re.fullmatch(r'\d?\.\d{1,2}', tok):
                        share = float(tok)
            # raw = 去掉标记后的主体(取 id 后到第一个标记前)
            raw = rest
            units.append({
                'unit_id': nid,
                'depth': depth,
                'raw': raw,
                'text': raw,  # coverage 层用 raw 做 embedding
                'kind': kind,
                'stop_marker': stop,
                'share': share,
            })
    return units


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('md', help='gold-*.md 路径')
    ap.add_argument('-o', '--out', help='输出 units.json')
    args = ap.parse_args()
    units = parse_gold(args.md)
    out = {
        '_schema': 'gold-md-units/v1',
        '_doc': 'B1 自动解析自 markdown gold tree (coverage 层用). formulas 层需人工标注.',
        'source': os.path.basename(args.md),
        'units': units,
    }
    if args.out:
        json.dump(out, open(args.out, 'w'), ensure_ascii=False, indent=1)
        print(f'→ {args.out} ({len(units)} units)')
    else:
        print(json.dumps(out, ensure_ascii=False, indent=1))
    # 校验: 深度分布 + 叶子/分裂数
    from collections import Counter
    kd = Counter(u['kind'] for u in units)
    dd = Counter(u['depth'] for u in units)
    print(f'  kind={dict(kd)} depth_dist={dict(sorted(dd.items()))}', file=sys.stderr)


if __name__ == '__main__':
    main()
