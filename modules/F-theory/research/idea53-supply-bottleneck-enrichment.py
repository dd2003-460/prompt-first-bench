#!/usr/bin/env python3
"""#53 修正版 — 供给侧系统瓶颈在 run 树的 level 分布 (2026-11-24, D 修正).

D 2026-11-24 修正: 真正要测的是供给侧系统瓶颈 (SM 频率/指令吞吐/发射率/内存带宽/
occupancy/warp), 不是需求侧 (duty_demand 业务占空比), 也不是纯文本正则.

本脚本 = idea53-run-tree-bottleneck-enrichment.py 的供给侧修正版:
- 数据源: rep-scan 15 树 (3849 节点) + t53b 18 个带 level 字段 GPU 树 (5497 节点),
  合并 9346 节点. (t53b 的 bare arm 树是 markdown 字符串无 level 字段, 跳过.)
- 口径: 供给侧系统瓶颈 = 硬件供给词 ∧ 瓶颈判定词 (同节点 claim+evidence+corrected_claim).
- 对照: 全体节点 level 分布 + 需求侧 (占空比/duty/负载) 富集 + 原 #53 精确正则
  (占空比|duty, 稀缺锚点) 富集 + verified 率.
- 边界核验: 微架构词 (warp/IPC/issue rate/发射/指令吞吐) 在树节点 vs 最终报告
  (answer 字段) 的命中, 判"judge 层不产生"是节点层还是整个 run 现象.

轴陷阱 (承重): run 树 level (L1-L4, judge 层) ≠ gold 主干深度, 本脚本只测 run 树
自身坐标系. 供给词是高频背景词 (19% 节点命中), 富集倍数天然比需求侧稀缺锚点弱.
实测: 富集强度与锚点基率成反比 — 稀缺锚点 duty (基率 0.4%) 富集 1.41x,
高频类别词 供给侧硬件 (基率 19%) 富集仅 1.10x. 解读富集倍数必须带基率.
"""
import json, glob, re
from collections import Counter

REPS = '/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/rep-scan/'
T53B = '/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/t53b/'

# 供给侧系统瓶颈词 (硬件供给侧资源)
SUPPLY = re.compile(
    r'带宽|算力|TFLOPS|TOPS|FLOPS|计算密度|compute.?bound|memory.?bound'
    r'|频率|clock|降频|DVFS|throttl|功耗|TDP'
    r'|(?<![A-Za-z])SM(?![A-Za-z])|occupancy|warp|(?<![A-Za-z])IPC(?![A-Za-z])'
    r'|issue.?rate|发射|指令吞吐', re.I)
# 瓶颈判定词
JUDGE = re.compile(r'瓶颈|受限|限制|利用率|上限|天花板|不足|不够|约束')
# 需求侧 (对照, 原 #53 锚点)
DEMAND = re.compile(r'占空比|duty|业务需求|负载|需求侧', re.I)
# 原 #53 精确正则 (稀缺锚点对照, 基率 ~0.4%)
DEMAND_EXACT = re.compile(r'占空比|duty', re.I)
# 微架构细分词 (D 修正真正关心的, 单独分词看 level)
MICRO = {
    '内存带宽': re.compile(r'内存带宽|显存带宽|bandwidth', re.I),
    'SM频率/clock/降频': re.compile(r'(?<![A-Za-z])SM.{0,8}频率|频率.{0,8}(?<![A-Za-z])SM|clock|降频|DVFS|throttl', re.I),
    'SM(词)': re.compile(r'(?<![A-Za-z])SM(?![A-Za-z])'),
    'occupancy/占用率': re.compile(r'occupancy|占用率', re.I),
    'warp': re.compile(r'warp', re.I),
    'IPC': re.compile(r'(?<![A-Za-z])IPC(?![A-Za-z])'),
    'issue rate/发射': re.compile(r'issue.?rate|发射'),
    '指令吞吐': re.compile(r'指令吞吐|instruction.?throughput', re.I),
}

def find_nodes(obj):
    """递归找带 level(str)+claim 的结构化节点对象."""
    out = []
    if isinstance(obj, dict):
        if isinstance(obj.get('level'), str) and 'claim' in obj:
            out.append(obj)
        else:
            for v in obj.values():
                out += find_nodes(v)
    elif isinstance(obj, list):
        for v in obj:
            out += find_nodes(v)
    return out

def text_of(nd):
    return ' '.join(str(nd.get(k) or '') for k in ('claim', 'evidence', 'corrected_claim'))

# --- 收集节点 ---
nodes = []
n_trees = 0
for f in glob.glob(REPS + 'rep-*.json'):
    if 'era-matched' in f or 'scores' in f:
        continue
    d = json.load(open(f))
    ns = [nd for nd in d.get('nodes', []) if nd.get('level') is not None]
    if ns:
        n_trees += 1
        nodes += ns
t53b_files = sorted(glob.glob(T53B + 'runs*/gpu_*.json'))
for f in t53b_files:
    ns = find_nodes(json.load(open(f)))
    if ns:
        n_trees += 1
        nodes += ns

# --- 测量 ---
lv_all = Counter(); n = 0
lv_sup = Counter(); n_sup = 0; st_sup = Counter()
lv_dem = Counter(); n_dem = 0; st_dem = Counter()
lv_demx = Counter(); n_demx = 0
st_all = Counter()
micro_lv = {k: Counter() for k in MICRO}
for nd in nodes:
    lv = nd['level']; st = nd.get('status')
    n += 1; lv_all[lv] += 1; st_all[st] += 1
    t = text_of(nd)
    if SUPPLY.search(t) and JUDGE.search(t):
        n_sup += 1; lv_sup[lv] += 1; st_sup[st] += 1
    if DEMAND.search(t):
        n_dem += 1; lv_dem[lv] += 1; st_dem[st] += 1
    if DEMAND_EXACT.search(t):
        n_demx += 1; lv_demx[lv] += 1
    for k, rx in MICRO.items():
        if rx.search(t):
            micro_lv[k][lv] += 1

print(f'树 {n_trees} 棵 | 节点 {n} (rep-scan + t53b 带 level 字段)')
print(f'全体 verified: {st_all.get("verified", 0) / n:.0%}')
print(f'供给侧 n={n_sup} verified={st_sup.get("verified", 0) / n_sup:.0%} status={dict(st_sup.most_common())}')
print(f'需求侧 n={n_dem} verified={st_dem.get("verified", 0) / n_dem:.0%} status={dict(st_dem.most_common())}')
print(f'原#53精确(占空比|duty) n={n_demx} ' +
      ' '.join(f'{lv}:{lv_demx.get(lv, 0)}({lv_demx.get(lv, 0) / n_demx:.0%}) 富集{lv_demx.get(lv, 0) / n_demx / (lv_all[lv] / n):.2f}x'
               for lv in sorted(lv_all)))

print('\n=== level 分布 (供给侧 vs 需求侧 vs 全体) ===')
print('level   全体        供给侧      供富集   需求侧     需富集')
for lv in sorted(lv_all):
    a = lv_all[lv] / n
    s = lv_sup.get(lv, 0) / n_sup
    d = lv_dem.get(lv, 0) / n_dem if n_dem else 0
    print(f'{lv}  {lv_all[lv]:4d}({a:5.1%})  {lv_sup.get(lv, 0):4d}({s:5.1%})  {s / a:5.2f}x  '
          f'{lv_dem.get(lv, 0):3d}({d:5.1%})  {d / a:5.2f}x')

print('\n=== 微架构分词 level 分布 (D 修正真正关心的) ===')
for k in MICRO:
    c = micro_lv[k]; tot = sum(c.values())
    if tot:
        print(f'{k:18s} n={tot:4d} ' + ' '.join(f'{lv}:{c.get(lv, 0)}' for lv in sorted(lv_all)))
    else:
        print(f'{k:18s} n=0  (树节点无命中)')

# --- 边界核验: 微架构词在最终报告 (answer) 是否出现 ---
print('\n=== 边界核验: 微架构词 树节点 vs 最终报告(answer) ===')
ans_count = Counter(); ans_files = 0
for f in t53b_files:
    d = json.load(open(f))
    ans = d.get('answer', '') or ''
    if ans:
        ans_files += 1
        for k, rx in MICRO.items():
            if rx.search(ans):
                ans_count[k] += 1
print(f'answer 字段文件数: {ans_files}')
for k in MICRO:
    node_tot = sum(micro_lv[k].values())
    print(f'{k:18s} answer={ans_count.get(k, 0):3d}  节点={node_tot:4d}')
print('若 answer 也 n=0 → 缺失是整个 run 现象 (数据源无 profile 输出), 非 judge 层现象.')

# --- 方法论对照: 富集倍数 vs 锚点基率 (伪影检验) ---
# 承重发现: 富集倍数与锚点基率强负相关 (r≈-0.93), 稀缺锚点显"高富集"部分是基率伪影.
# 解读 #53 的 1.51x / 本脚本供给侧 1.10x 必须带基率, 不能跨锚点直接比大小.
ANCHORS = {
    'duty(稀缺)': re.compile(r'占空比|duty', re.I),
    '功耗/TDP': re.compile(r'功耗|TDP', re.I),
    '显存容量GB': re.compile(r'\d+\s*GB|显存容量'),
    '量化INT8/FP8': re.compile(r'INT8|FP8|BF16|FP16|量化', re.I),
    '延迟/latency': re.compile(r'延迟|latency|ms|毫秒', re.I),
    'GPU型号': re.compile(r'H100|A100|H200|A6000|4090|5090', re.I),
    '带宽(高频)': re.compile(r'带宽|bandwidth', re.I),
    '吞吐(高频)': re.compile(r'吞吐|throughput|tok/s|token/s', re.I),
    'TCO/成本': re.compile(r'TCO|成本|价格|元|\\$', re.I),
    'KV Cache': re.compile(r'KV.?Cache', re.I),
}
print('\n=== 方法论对照: 锚点基率 vs L4 富集倍数 (伪影检验) ===')
print(f'{"锚点":20s} {"基率":>7s} {"L4":>5s} {"L4富集":>8s}')
import math
pts = []
for k, rx in ANCHORS.items():
    c = Counter(); nh = 0
    for nd in nodes:
        if rx.search(text_of(nd)):
            nh += 1; c[nd['level']] += 1
    if nh == 0:
        print(f'{k:20s} n=0'); continue
    base = nh / n
    l4enr = (c.get('L4', 0) / nh) / (lv_all['L4'] / n)
    pts.append((base, l4enr))
    print(f'{k:20s} {base:6.1%} {c.get("L4", 0):5d} {l4enr:7.2f}x  (n={nh})')
xs = [math.log(b) for b, _ in pts]; ys = [e for _, e in pts]
mx = sum(xs) / len(xs); my = sum(ys) / len(ys)
cov = sum((xs[i] - mx) * (ys[i] - my) for i in range(len(xs)))
vx = sum((xs[i] - mx) ** 2 for i in range(len(xs)))
vy = sum((ys[i] - my) ** 2 for i in range(len(ys)))
r = cov / math.sqrt(vx * vy) if vx * vy > 0 else 0
print(f'基率(log) vs L4富集倍数 相关系数 r = {r:.3f} (n={len(pts)} 锚点)')
print('r 强负 → 富集倍数是基率伪影, 跨锚点比大小无效, 必须带基率解读.')
