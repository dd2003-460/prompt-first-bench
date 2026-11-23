#!/usr/bin/env python3
"""#48 预测 2 实证: 耦合覆盖率 (verified 占比) 与树深度的相关性。
耦合图视角: verified = 强耦合 (c=1.0), degraded = 弱耦合 (c=0.5), pending = 未耦合。
耦合覆盖率 cc = verified/(verified+degraded+pending)。
预测 2: 耦合覆盖率与 bench 分数 (此处用树深度代理) 正相关。

结果 (2026-11-23 修正版, 三域全 corpus 去重, >=20 nodes, 排除无 status 树):
  gpu: n=28, depth {3:10, 4:16, 5:2} (唯一深度变化充分的域)
       r(cc,depth)=0.100 (t=0.51, 不显著), 偏相关 r|n=-0.095
  nat: n=22, depth {3:1, 4:21} — 深度退化 (2 值, 1 树 vs 21 树), r=0.873 不可信
  soc: n=27, depth {4:27} — 深度恒定, 相关不可计算
  结论: 预测 2 在唯一可测域 (GPU) 不成立 (r≈0)。
  修正记录: 原版本 (r=0.738) 有两个 bug —
    (1) glob rep-scan/*.json 误纳入 era-matched*.json (matched-pair 文件, 非 run 树,
        depth=1 平铺, 无 status 字段);
    (2) line 39 `cc = v/(v+dg+p) if (v+dg+p) else 0` 把无 status 的树默认 cc=0 (假点),
        但 depth 真实 (depth=1) → 两个 (depth=1, cc=0) 假点把 r 从真值 0.100 拉到 0.738。
  注: depth 用 parent_ids 构树算 (level 字段全为 1, 不可用)。
  口径: 三域全 corpus; 深度退化域 (nat/soc) 的相关不可解释。
"""
import json, glob, os, math, statistics
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # 脚本在 modules/F-theory/research/, 到 pfb/ 需 4 层

DOMS = {
    'gpu': (glob.glob(os.path.join(ROOT, 'experiments/stage-ablation/checkpoints/archive/budget-*/runs-s5-sm-gpu.json'))
            + glob.glob(os.path.join(ROOT, 'modules/B-pipeline-ablation/data/rep-scan/rep-*.json'))  # 修正: rep-* 排除 era-matched*.json
            + [os.path.join(ROOT, 'experiments/stage-ablation/runs-s5-sm-gpu.json')]),
    'nat': (glob.glob(os.path.join(ROOT, 'experiments/stage-ablation/runs-s5-sm-nat*.json'))
            + glob.glob(os.path.join(ROOT, 'experiments/stage-ablation/checkpoints/archive/*nat*/runs-s5-sm-nat*.json'))
            + glob.glob(os.path.join(ROOT, 'modules/B-pipeline-ablation/data/rep-scan/*nat*.json'))),
    'soc': (glob.glob(os.path.join(ROOT, 'experiments/stage-ablation/runs-s5-sm-soc*.json'))
            + glob.glob(os.path.join(ROOT, 'experiments/stage-ablation/checkpoints/archive/*soc*/runs-s5-sm-soc*.json'))
            + glob.glob(os.path.join(ROOT, 'modules/B-pipeline-ablation/data/rep-scan/*soc*.json'))),
}

def load_nodes(f):
    if not os.path.exists(f):
        return None
    d = json.load(open(f))
    nodes = d.get('nodes', d) if isinstance(d, dict) else d
    return nodes if isinstance(nodes, list) and len(nodes) >= 20 else None

def tree_depth(nodes):
    id2 = {n.get('id'): n for n in nodes}
    sd = {}
    def d(nid):
        if nid in sd: return sd[nid]
        n = id2.get(nid)
        if not n: return 1
        pids = n.get('parent_ids') or []
        if not pids:
            sd[nid] = 1; return 1
        pd = max(d(p) for p in pids if p in id2) + 1
        sd[nid] = pd; return pd
    return max(d(n.get('id')) for n in nodes)

def cc_of(nodes):
    """无 status 字段的树返回 None (跳过, 不默认 0)。"""
    v = sum(1 for n in nodes if n.get('status') == 'verified')
    dg = sum(1 for n in nodes if n.get('status') == 'degraded')
    p = sum(1 for n in nodes if n.get('status') == 'pending')
    return v / (v + dg + p) if (v + dg + p) else None

def pearson(x, y):
    mx, my = statistics.mean(x), statistics.mean(y)
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    den = math.sqrt(sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y))
    return num / den if den else 0

def partial_r(x, y, z):
    def reg_resid(dep, ind):
        r = pearson(ind, dep)
        md, mi = statistics.mean(dep), statistics.mean(ind)
        sd_, si = (sum((a - md) ** 2 for a in dep)) ** 0.5, (sum((a - mi) ** 2 for a in ind)) ** 0.5
        beta = r * sd_ / si
        return [di - (md + beta * (ii - mi)) for di, ii in zip(dep, ind)]
    return pearson(reg_resid(x, z), reg_resid(y, z))

print(f"{'domain':>7} {'n':>4} {'n_skip':>7} {'depth_dist':>18} {'r(cc,depth)':>12} {'r|n':>7} {'t0':>7}")
for dom, cands in DOMS.items():
    seen = set()
    rows = []
    n_skip = 0
    for f in cands:
        nodes = load_nodes(f)
        if not nodes:
            continue
        key = (nodes[0].get('id'), len(nodes))
        if key in seen:
            continue
        seen.add(key)
        cc = cc_of(nodes)
        if cc is None:
            n_skip += 1
            continue
        rows.append((tree_depth(nodes), len(nodes), cc))
    depths = Counter(r[0] for r in rows)
    dd = str(dict(sorted(depths.items())))
    if len(rows) < 5 or len(depths) < 2:
        print(f"{dom:>7} {len(rows):>4} {n_skip:>7} {dd:>18} {'退化/太小':>12}")
        continue
    x = [r[0] for r in rows]
    nn = [r[1] for r in rows]
    y = [r[2] for r in rows]
    r0 = pearson(x, y)
    rp = partial_r(x, y, nn)
    n = len(rows)
    t0 = r0 * math.sqrt(n - 2) / math.sqrt(1 - r0 ** 2) if abs(r0) < 1 else float('inf')
    print(f"{dom:>7} {n:>4} {n_skip:>7} {dd:>18} {r0:>12.3f} {rp:>7.3f} {t0:>7.2f}")

print("\n结论: 预测 2 在唯一深度变化充分的域 (GPU) 不成立 (r=0.100, t=0.51)。")
print("nat/soc 深度退化 (2 值 / 恒定), 相关不可解释。")
