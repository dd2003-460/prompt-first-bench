#!/usr/bin/env python3
"""source_verify.py — 来源锚定数值校验层（机械，无 LLM）。

D 2026-11-23 重框 L3：核验 = 分解 + 搜集 + 校验。LLM 不可靠的是前两段
（找对来源、拆对量）。但节点已带 retrieval_sources URL = 模型把分解+搜集
做完了，剩下的"这个数在不在来源里"是纯机械校验，脚本可做、确定、可复现。

口径：
  - 候选节点 = claim 含 数值+单位(GB/tokens/s/GB/s/TFLOPS/W/美元) 且
    retrieval_sources 含 ≥1 URL。
  - 取 claim 第一个 数值+单位，取第一个 URL（去 &rut= DDG 尾巴）。
  - 严格命中 = 数值 与 单位在 20 字符窗口内共现（防"24"出现在日期/ID 里）。
  - 宽松命中 = 数值 且 单位 在页任意处。
  - 分类: verified(严格) / weak(仅宽松) / not_verified(可达但两者皆无) /
    unreachable(抓取失败)。
  - verification_success_rate = verified / (verified + weak + not_verified)
    （排除 unreachable；分母=可达节点）。

诊断层，不进 composite（同 L2/L4）。可达性偏差须标注：zhihu/csdn 反爬挡住，
而它们是模型主要来源 → 不可达集偏向模型真实来源，非随机。
"""
import sys, os, glob, json, re, time, urllib.request

BASE = '/Users/a1-6/Desktop/workspace/pfb'
CACHE = os.path.join(BASE, 'modules/B-pipeline-ablation/data/source-verify-cache.json')
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/120.0 Safari/537.36')
NUM_RE = re.compile(r'(\d+\.?\d*)\s*(GB|tokens/s|GB/s|TFLOPS|W|美元)')
TIMEOUT = 6
WINDOW = 20


def load_cache():
    if os.path.exists(CACHE):
        try:
            return json.load(open(CACHE))
        except Exception:
            pass
    return {}


def save_cache(c):
    json.dump(c, open(CACHE, 'w'))


def fetch(url):
    clean = url.split('&rut=')[0]
    try:
        req = urllib.request.Request(clean, headers={'User-Agent': UA, 'Accept': 'text/html'})
        html = urllib.request.urlopen(req, timeout=TIMEOUT).read(300000).decode('utf-8', 'ignore')
        return True, html
    except Exception:
        return False, ''


def verdict(html, num, unit):
    if not html:
        return 'unreachable'
    unit_core = unit.split('/')[0]
    strict = False
    for m in re.finditer(re.escape(num), html):
        if unit_core in html[m.start():m.start() + WINDOW]:
            strict = True
            break
    if strict:
        return 'verified'
    if (num in html) and (unit_core in html):
        return 'weak'
    return 'not_verified'


def collect_trees():
    trees = []
    for f in sorted(glob.glob(os.path.join(BASE, 'modules/B-pipeline-ablation/data/idea2/idea2-*.json'))):
        if 'scores' in f or 'run' in f:
            continue
        trees.append(('idea2', os.path.basename(f).replace('.json', ''), f))
    for f in sorted(glob.glob(os.path.join(BASE, 'experiments/stage-ablation/checkpoints/archive/budget-*/runs-s5-sm-gpu.json'))):
        tag = f.split('/archive/')[1].split('/')[0]
        trees.append(('K7', tag, f))
    return trees


def main():
    cache = load_cache()
    trees = collect_trees()
    print(f"[source_verify] {len(trees)} trees, cache={len(cache)}", flush=True)
    out = []
    for fam, tag, path in trees:
        try:
            d = json.load(open(path))
        except Exception as e:
            print(f"  SKIP {fam}/{tag}: {e}", flush=True)
            continue
        n_nodes = len(d['nodes'])
        n_cand = 0
        v = {'verified': 0, 'weak': 0, 'not_verified': 0, 'unreachable': 0}
        for nd in d['nodes']:
            m = NUM_RE.search(nd['claim'])
            if not m:
                continue
            rs = nd.get('retrieval_sources') or []
            urls = [r.get('url', '') for r in rs if r.get('url')]
            if not urls:
                continue
            n_cand += 1
            num, unit, url = m.group(1), m.group(2), urls[0]
            key = f"{url.split('&rut=')[0]}|{num}|{unit}"
            if key in cache:
                cls = cache[key]
            else:
                ok, html = fetch(url)
                cls = 'unreachable' if not ok else verdict(html, num, unit)
                cache[key] = cls
                time.sleep(0.3)
            v[cls] += 1
        reachable = v['verified'] + v['weak'] + v['not_verified']
        vsr = (v['verified'] / reachable) if reachable else None
        rec = {'fam': fam, 'tag': tag, 'n_nodes': n_nodes, 'n_cand': n_cand, **v,
               'reachable': reachable,
               'vsr': round(vsr, 4) if vsr is not None else None,
               'reach_rate': round(reachable / n_cand, 4) if n_cand else None}
        out.append(rec)
        print(f"  {fam:5s}/{tag:18s} cand={n_cand:3d} reach={reachable:3d} "
              f"V={v['verified']:2d} W={v['weak']:2d} NV={v['not_verified']:2d} UR={v['unreachable']:2d} "
              f"vsr={rec['vsr']}", flush=True)
        save_cache(cache)
    json.dump(out, open(os.path.join(BASE, 'modules/B-pipeline-ablation/data/source-verify.json'), 'w'), indent=1)
    print("DONE", flush=True)


if __name__ == '__main__':
    main()
