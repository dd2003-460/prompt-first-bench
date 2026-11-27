#!/usr/bin/env python3
"""sm_node_probe.py — T53b 节点抽查: 每个活跃 run 采样节点, 看内容+更新时间戳。

用法: python3 sm_node_probe.py [--n 5] [--run gpu]
只读, 不碰 SM 代码, 不影响 run 同质性。

判断逻辑:
- 最新节点 mtime 距现在 < 5min → 在干活
- 5-30min → 可能在长 LLM 调用 (30K prompt 可达 1-2min, 但 30min 无新节点=可疑)
- > 30min → 疑似卡死, 配合 sm.log tail 判断
- 节点 status 分布: verified/degraded/pending 比例异常 (如全 pending) → 验证环节有问题
"""
import json, os, sys, glob, time, argparse

CKPT = os.path.join(os.path.dirname(__file__), 'checkpoints')


def latest_nodes(run, n):
    """取该 run 所有 checkpoint 目录里 mtime 最新的 n 个 node.json。"""
    dirs = glob.glob(os.path.join(CKPT, f'sm-{run}-r*'))
    nodes = []
    for d in dirs:
        for f in glob.glob(os.path.join(d, '**', 'node.json'), recursive=True):
            nodes.append((os.path.getmtime(f), f))
    nodes.sort(reverse=True)
    return nodes[:n]


def probe(run, n, compact=False):
    nodes = latest_nodes(run, n)
    now = time.time()
    # 实时健康信号: 当前 run 的 sm.log mtime (秒级更新, 比 checkpoint 可靠)
    # checkpoint 只在轮次边界落盘, 轮次中间不更新 → 不能用它判"卡没卡"
    logs = glob.glob(f'/tmp/t53b/{run}_*.sm.log')
    log_age = None
    log_name = None
    if logs:
        newest = max(logs, key=os.path.getmtime)
        log_age = now - os.path.getmtime(newest)
        log_name = os.path.basename(newest)
        log_s = f'{int(log_age)//60}m{int(log_age)%60:02d}s'
        health = 'LIVE' if log_age < 120 else ('SLOW' if log_age < 1800 else 'DEAD?')
        if compact:
            print(f'{run}|{log_name}|{int(log_age)}s|{health}', end='')
        else:
            print(f'\n[{run}] sm.log {log_name} {log_s} ago → {health}')
    if not nodes:
        if compact:
            print('|-|0|NO_CKPT')
        else:
            print(f'  (无 checkpoint 节点 — 可能轮次中间未落盘, 看 sm.log 判健康)')
        return
    # 状态分布 (全量)
    dirs = glob.glob(os.path.join(CKPT, f'sm-{run}-r*'))
    dist = {}
    total = 0
    for d in dirs:
        for f in glob.glob(os.path.join(d, '**', 'node.json'), recursive=True):
            try:
                s = json.load(open(f)).get('status', '?')
                dist[s] = dist.get(s, 0) + 1
                total += 1
            except Exception:
                pass
    if compact:
        print(f'|n={total}|' + ' '.join(f'{k}:{v}' for k, v in sorted(dist.items())))
        return
    dist_str = ' '.join(f'{k}:{v}' for k, v in sorted(dist.items()))
    print(f'\n[{run}] 总节点 {total} | 状态 {dist_str}')
    for mt, f in nodes:
        age = int(now - mt)
        age_s = f'{age//60}m{age%60:02d}s' if age < 3600 else f'{age//3600}h{(age%3600)//60}m'
        # 节点 mtime = 轮次落盘时间, 不是实时信号 (健康看上面的 sm.log)
        try:
            d = json.load(open(f))
            claim = (d.get('claim') or '')[:60].replace('\n', ' ')
            print(f'  {age_s:>7s} ago(ckpt)  N{d.get("id","?"):<8s} '
                  f'L{d.get("level","?")} {d.get("status","?"):<10s} {claim}')
        except Exception as e:
            print(f'  ERR {f}: {e}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=5, help='每 run 采样节点数')
    ap.add_argument('--run', default=None, help='只看指定 run (gpu/nat/soc)')
    ap.add_argument('--compact', action='store_true',
                    help='每 run 一行 run|log|age|health (供定时抽查留痕)')
    a = ap.parse_args()
    runs = [a.run] if a.run else ['gpu', 'nat', 'soc']
    if a.compact:
        print(time.strftime('%H:%M:%S'), end=' ')
    else:
        print(f'=== 节点抽查 {time.strftime("%H:%M:%S")} ===')
    for r in runs:
        probe(r, a.n, compact=a.compact)
        if not a.compact:
            print()


if __name__ == '__main__':
    main()
