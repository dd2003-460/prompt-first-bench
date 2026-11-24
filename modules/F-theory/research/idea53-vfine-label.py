#!/usr/bin/env python3
"""#53 V_fine 机制级打标 (27b judge, 127.0.0.1:8787).

判据: 节点是否含'具体哪一环'的机制级定位语言 (容量vs带宽 / issue rate vs decode
width / 标量vs张量 / FP16vsFP4占比), 且给定量或方向性判断 (慢40%/占78%/瓶颈80%+)。
仅罗列候选假设 = 0。输出 1/0。

只在 V_coarse=1 (SUPPLY∧JUDGE 命中) 的节点上判 (5291 个); V_coarse=0 节点 F=0
(V_fine ⊆ V_coarse: 机制级瓶颈判定是瓶颈判定的精化子集)。
断点续传: 已判 id 跳过。每 50 条落盘。
"""
import importlib.util, json, os, sys, hashlib, urllib.request, time
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
spec = importlib.util.spec_from_file_location('c', HERE + '/idea53_common.py')
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

API = 'http://127.0.0.1:8787/v1/chat/completions'
MODEL = 'qwen3.8-27b-mtp'
OUT = os.path.join(HERE, 'idea53-vfine-labels.json')
TEXT_CAP = 1000
N_WORKERS = 16

PROMPT = ('判断该GPU推理瓶颈分析节点是否含机制级定位: 明确指出瓶颈具体在哪一环'
          '(如 容量vs带宽/issue rate vs decode width/标量vs张量/FP16vsFP4占比)'
          '并给定量或方向性判断(如 慢40%/占78%时间/瓶颈80%+)。仅罗列候选假设=0。'
          '只输出1或0。\n节点: {t}')


def judge(text, retries=2):
    body = json.dumps({
        'model': MODEL,
        'messages': [{'role': 'user', 'content': PROMPT.format(t=text[:TEXT_CAP])}],
        'max_tokens': 16, 'temperature': 0,
        'chat_template_kwargs': {'enable_thinking': False},
    }).encode()
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(API, data=body,
                                         headers={'Content-Type': 'application/json'})
            r = json.load(urllib.request.urlopen(req, timeout=120))
            out = r['choices'][0]['message']['content'].strip()
            if '1' in out:
                return 1
            if '0' in out:
                return 0
        except Exception:
            time.sleep(0.5)
    return None  # 失败, 重试后仍无 → 标 None (后续补判)


def collect_c1():
    """收集 V_coarse=1 节点, 确定性排序, 赋稳定 id."""
    trees = c.load_trees()
    items = []
    for name, ts in trees.items():
        for tid, root, ns in ts:
            for nd in ns:
                t = c.text_of(nd)
                if c.SUPPLY.search(t) and c.JUDGE.search(t):
                    key = hashlib.sha1((name + '|' + tid + '|' + t).encode()).hexdigest()[:12]
                    items.append({'id': f'{name}#{tid}#{key}', 'src': name,
                                  'tree': tid, 'lv': nd['level'], 'text': t})
    items.sort(key=lambda x: x['id'])
    return items


def main():
    items = collect_c1()
    print(f'V_coarse=1 节点: {len(items)}')
    done = {}
    if os.path.exists(OUT):
        done = json.load(open(OUT))
        print(f'已判 {len(done)} (断点续传)')
    todo = [it for it in items if it['id'] not in done or done[it['id']] is None]
    print(f'待判 {len(todo)}')
    if not todo:
        print('全部已判'); return
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=N_WORKERS) as ex:
        futs = {ex.submit(judge, it['text']): it for it in todo}
        n_done = 0
        for fut in as_completed(futs):
            it = futs[fut]
            done[it['id']] = fut.result()
            n_done += 1
            if n_done % 50 == 0:
                json.dump(done, open(OUT, 'w'), ensure_ascii=False)
                el = time.time() - t0
                print(f'  {n_done}/{len(todo)} | {el:.0f}s | '
                      f'ETA {el / n_done * (len(todo) - n_done):.0f}s', flush=True)
    json.dump(done, open(OUT, 'w'), ensure_ascii=False)
    n_fail = sum(1 for v in done.values() if v is None)
    n1 = sum(1 for v in done.values() if v == 1)
    print(f'完成: {len(done)} 判, F=1: {n1}, 失败(None): {n_fail}, 耗时 {time.time() - t0:.0f}s')


if __name__ == '__main__':
    main()
