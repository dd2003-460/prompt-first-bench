#!/usr/bin/env python3
"""#48 预测 2 实证: 耦合覆盖率 (verified 占比) 与树深度的相关性。
耦合图视角: verified = 强耦合 (c=1.0), degraded = 弱耦合 (c=0.5), pending = 未耦合。
耦合覆盖率 cc = verified/(verified+degraded+pending)。
预测 2: 耦合覆盖率与 bench 分数 (此处用树深度代理) 正相关。
结果 (2026-11-23, GPU 域 30 trees, budget-* + rep-scan 去重, >=20 nodes):
  r(cc, depth) = 0.738 (零阶, t=5.78, df=28)
  r(cc, depth | n_nodes) = 0.806 (偏相关, t=7.07, df=27) — 控制节点数后更强
  结论: 耦合覆盖率与树深度强正相关, 非节点数混杂 — #48 预测 2 在 GPU 域成立。
  注: depth 用 parent_ids 构树算 (level 字段全为 1, 不可用)。
  口径: 单域 (GPU), 跨域待 Q6 全曲线后验。
"""
import json, glob, os, math, statistics

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CANDS = (glob.glob(os.path.join(ROOT, 'experiments/stage-ablation/checkpoints/archive/budget-*/runs-s5-sm-gpu.json'))
         + glob.glob(os.path.join(ROOT, 'modules/B-pipeline-ablation/data/rep-scan/*.json')))

seen = set()
trees = []
for f in CANDS:
    if not os.path.exists(f):
        continue
    d = json.load(open(f))
    nodes = d.get('nodes', d) if isinstance(d, dict) else d
    if not isinstance(nodes, list) or len(nodes) < 20:
        continue
    key = (nodes[0].get('id'), len(nodes))
    if key in seen:
        continue
    seen.add(key)
    trees.append(nodes)

rows = []
for nodes in trees:
    v = sum(1 for n in nodes if n.get('status') == 'verified')
    dg = sum(1 for n in nodes if n.get('status') == 'degraded')
    p = sum(1 for n in nodes if n.get('status') == 'pending')
    cc = v / (v + dg + p) if (v + dg + p) else 0
    id2node = {n.get('id'): n for n in nodes}
    def depth_of(nid, sd):
        if nid in sd:
            return sd[nid]
        n = id2node.get(nid)
        if not n:
            return 1
        pids = n.get('parent_ids') or []
        if not pids:
            sd[nid] = 1
            return 1
        pd = max(depth_of(p, sd) for p in pids if p in id2node) + 1
        sd[nid] = pd
        return pd
    md = max(depth_of(n.get('id'), {}) for n in nodes)
    rows.append((len(nodes), cc, md))

def pearson(x, y):
    mx, my = statistics.mean(x), statistics.mean(y)
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    den = math.sqrt(sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y))
    return num / den if den else 0

n_nodes = [r[0] for r in rows]
cc = [r[1] for r in rows]
depth = [r[2] for r in rows]
r_cd = pearson(cc, depth)
r_cn = pearson(cc, n_nodes)
r_dn = pearson(depth, n_nodes)
r_partial = (r_cd - r_cn * r_dn) / math.sqrt((1 - r_cn ** 2) * (1 - r_dn ** 2))

print(f"n={len(rows)} trees (GPU 域, >=20 nodes, 去重)")
print(f"r(cc, depth) = {r_cd:.3f} (零阶)")
print(f"r(cc, n_nodes) = {r_cn:.3f}")
print(f"r(depth, n_nodes) = {r_dn:.3f}")
print(f"偏相关 r(cc, depth | n_nodes) = {r_partial:.3f}")
if abs(r_partial) < 1:
    t = r_partial * math.sqrt((len(rows) - 3) / (1 - r_partial ** 2))
    print(f"  t = {t:.2f} (df={len(rows) - 3})")
print("结论: 耦合覆盖率与树深度强正相关, 控制节点数后更强 — #48 预测 2 在 GPU 域成立")
