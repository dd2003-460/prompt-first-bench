#!/usr/bin/env python3
"""calibration_check.py — 自评 status 与机械来源核验的校准度（机械，无 LLM）。

问题：模型说 verified 的节点，机械核验（数值真在来源页）是否也更真？
口径：
  - 候选 = 所有带 ≥1 URL 的节点（不限数值 claim，扩大样本）。
  - 数值提取：claim 第一个 数值+单位；无数值的节点只查 URL 可达性（可达性校准）。
  - 机械判定：复用 source_verify 的 cache（key=url|num|unit），miss 的现场抓
    （限 400 次新抓取，防超时；抓完写回 cache）。
  - 校准度 = 各 status 组的机械 verified 率（可达子集内）。
    若 verified 组 > degraded 组 > pending 组，自评有校准；若平，自评失效。
输出: data/calibration-check.json + stdout 交叉表。
"""
import sys, os, json, re, time, urllib.request
from collections import Counter

BASE = '/Users/a1-6/Desktop/workspace/pfb'
MOD = os.path.join(BASE, 'modules/B-pipeline-ablation')
CACHE = os.path.join(MOD, 'data/source-verify-cache.json')
OUT = os.path.join(MOD, 'data/calibration-check.json')
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/120.0 Safari/537.36')
NUM_RE = re.compile(r'(\d+\.?\d*)\s*(GB|tokens/s|GB/s|TFLOPS|W|美元)')
TIMEOUT = 6
WINDOW = 20
MAX_NEW_FETCH = 400


def verdict(html, num, unit):
    if not html:
        return 'unreachable'
    unit_core = unit.split('/')[0]
    for m in re.finditer(re.escape(num), html):
        if unit_core in html[m.start():m.start() + WINDOW]:
            return 'verified'
    if (num in html) and (unit_core in html):
        return 'weak'
    return 'not_verified'


def fetch(url):
    clean = url.split('&rut=')[0]
    try:
        req = urllib.request.Request(clean, headers={'User-Agent': UA, 'Accept': 'text/html'})
        html = urllib.request.urlopen(req, timeout=TIMEOUT).read(300000).decode('utf-8', 'ignore')
        return True, html
    except Exception:
        return False, ''


def main():
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    trees = []
    for f in sorted(__import__('glob').glob(os.path.join(MOD, 'data/idea2/idea2-*.json'))):
        if 'scores' in f or 'run' in f:
            continue
        trees.append(('idea2', f))
    for f in sorted(__import__('glob').glob(os.path.join(BASE, 'experiments/stage-ablation/checkpoints/archive/budget-*/runs-s5-sm-gpu.json'))):
        trees.append(('K7', f))

    n_new = 0
    rows = []  # (fam, status, cls, has_num)
    for fam, path in trees:
        d = json.load(open(path))
        for nd in d['nodes']:
            urls = [r.get('url', '') for r in (nd.get('retrieval_sources') or []) if r.get('url')]
            if not urls:
                continue
            url = urls[0].split('&rut=')[0]
            st = nd.get('status', '?')
            m = NUM_RE.search(nd['claim'])
            has_num = bool(m)
            if m:
                key = f"{url}|{m.group(1)}|{m.group(2)}"
                if key not in cache:
                    if n_new < MAX_NEW_FETCH:
                        ok, html = fetch(url)
                        cache[key] = 'unreachable' if not ok else verdict(html, m.group(1), m.group(2))
                        n_new += 1
                        time.sleep(0.2)
                    else:
                        continue
                cls = cache[key]
            else:
                # 无数值: 只判可达性
                rkey = f"{url}|__reach__"
                if rkey not in cache:
                    if n_new < MAX_NEW_FETCH:
                        ok, _ = fetch(url)
                        cache[rkey] = 'reachable' if ok else 'unreachable'
                        n_new += 1
                        time.sleep(0.2)
                    else:
                        continue
                cls = 'reachable' if cache[rkey] == 'reachable' else 'unreachable'
            rows.append((fam, st, cls, has_num))
    json.dump(cache, open(CACHE, 'w'))

    # 交叉表（仅带数值的节点进 verified/weak/not_verified 口径）
    num_pairs = Counter((r[1], r[2]) for r in rows if r[3])
    st_order = ['verified', 'degraded', 'pending']
    cls_order = ['verified', 'weak', 'not_verified', 'unreachable']
    print(f"带数值候选节点 = {sum(num_pairs.values())} (新抓取 {n_new})")
    print(f"{'status':12s} | " + " ".join(f"{c:>9s}" for c in cls_order) + " | 可达  可达内verified率")
    summary = {}
    for st in st_order:
        row = [num_pairs[(st, c)] for c in cls_order]
        reach = row[0] + row[1] + row[2]
        rate = row[0] / reach if reach else None
        summary[st] = {'counts': dict(zip(cls_order, row)), 'reachable': reach,
                       'verified_rate': round(rate, 4) if rate is not None else None}
        print(f"{st:12s} | " + " ".join(f"{x:9d}" for x in row) +
              f" | {reach:4d}  {rate:.3f}" if rate is not None else
              f"{st:12s} | " + " ".join(f"{x:9d}" for x in row) + f" | {reach:4d}  -")

    # 无数值节点的可达性校准
    reach_pairs = Counter((r[1], r[2]) for r in rows if not r[3])
    print(f"\n无数值节点可达性 (n={sum(reach_pairs.values())}):")
    for st in st_order:
        tot = reach_pairs[(st, 'reachable')] + reach_pairs[(st, 'unreachable')]
        rr = reach_pairs[(st, 'reachable')] / tot if tot else None
        print(f"  {st:12s} reachable={reach_pairs[(st,'reachable')]:4d}/{tot:4d}  rate={rr:.3f}" if rr is not None else f"  {st:12s} n=0")

    json.dump({'summary': summary, 'n_new_fetch': n_new,
               'num_pairs': {f"{k[0]}|{k[1]}": v for k, v in num_pairs.items()},
               'reach_pairs': {f"{k[0]}|{k[1]}": v for k, v in reach_pairs.items()}},
              open(OUT, 'w'), indent=1)
    print(f"\n→ {OUT}")


if __name__ == '__main__':
    main()
