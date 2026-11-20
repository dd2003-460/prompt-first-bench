#!/usr/bin/env python3
"""T53b 节点抽查循环: 每 10min 一行摘要追加到 /tmp/t53b/node-trail.log.
只读, 不碰 SM. 62 run 跑完后 kill (pgrep -f sm-node-trail).
2026-11-20: 加通道健康探测 (wiki/ddg/bing/arxiv/webllm)——04-verify 用
时间线归因占位符 evidence 率 (哪个 run 跑在哪些通道死的时候)。"""
import subprocess, time, sys, urllib.request
PROBE = '/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/sm_node_probe.py'
TRAIL = '/tmp/t53b/node-trail.log'
CHANNELS = [
    ('wiki', 'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=test&format=json&srlimit=1'),
    ('ddg', 'https://lite.duckduckgo.com/lite/?q=test'),
    ('bing', 'https://www.bing.com/search?q=test&setlang=en&count=1'),
    ('arxiv', 'http://export.arxiv.org/api/query?search_query=all:test&max_results=1'),
]
def probe_channels():
    parts = []
    for name, url in CHANNELS:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            r = urllib.request.urlopen(req, timeout=10)
            parts.append(f'{name}:{r.status}')
        except Exception as e:
            code = getattr(e, 'code', None)
            parts.append(f'{name}:{"429" if code == 429 else type(e).__name__[:6]}')
    return ' '.join(parts)
while True:
    try:
        out = subprocess.run([sys.executable, PROBE, '--compact'],
                             capture_output=True, text=True, timeout=60)
        line = out.stdout.strip()
        with open(TRAIL, 'a') as f:
            f.write(line + ' | ' + probe_channels() + '\n')
    except Exception as e:
        with open(TRAIL, 'a') as f:
            f.write(f'ERR {e}\n')
    time.sleep(600)
