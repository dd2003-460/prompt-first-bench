#!/usr/bin/env python3
"""#47 连续化测量: A (带2b prior) vs B (去2b) 的 crosscut 维度语义相似度。
二值 KWS 命中 (idea-list #47 原方法) 效应量 Δ=0.16 (ns); 本脚本用语义相似度
(bge-m3 dim 对参照集 max cosine) 测分布差异, 预期效应量更大。
结果 (2026-11-23): A 0.5201 vs B 0.5079, t=0.349 ns, Cohen's d=0.102 —
效应量比二值更小, 2b prior 影响弱, 扩 n 性价比低 (双重确认)。
数据: modules/F-theory/research/l1-repro-probe{,-v2}.jsonl (A 33 dims, B 18 dims)
"""
import json, os, sys, math
from statistics import mean, stdev
from sentence_transformers import SentenceTransformer

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(HERE, 'modules', 'F-theory', 'research')
REFS = ["不确定性分级", "置信度评估", "风险披露", "条件性结论", "溯源验证", "敏感性分析"]

model = SentenceTransformer("BAAI/bge-m3")
ref = model.encode(REFS, normalize_embeddings=True)

recs = []
for f in ['l1-repro-probe.jsonl', 'l1-repro-probe-v2.jsonl']:
    p = os.path.join(DATA, f)
    if not os.path.exists(p):
        continue
    for line in open(p):
        r = json.loads(line)
        g = r.get('group', 'v1-A')  # v1 无 group 字段, 全是 A-full
        for d in r.get('dims', []):
            recs.append(('A' if g in ('A-full', 'v1-A') else 'B', d))

scores = {'A': [], 'B': []}
for key, d in recs:
    emb = model.encode([d], normalize_embeddings=True)
    scores[key].append(float((emb @ ref.T).max()))

print("#47 连续化测量 (dim 对参照集 max cosine):")
for k in ['A', 'B']:
    v = scores[k]
    print(f"  {k} 组: n={len(v)} mean={mean(v):.4f} median={sorted(v)[len(v)//2]:.4f}")
a, b = scores['A'], scores['B']
n1, n2 = len(a), len(b)
sp = math.sqrt(((n1-1)*stdev(a)**2 + (n2-1)*stdev(b)**2) / (n1+n2-2))
t = (mean(a)-mean(b)) / (sp*math.sqrt(1/n1+1/n2))
d = abs(mean(a)-mean(b)) / sp
print(f"  t={t:.3f} (df={n1+n2-2}), Cohen's d={d:.3f}")
print("结论: 效应量弱 (d<0.2), 扩 n 性价比低 — 与二值命中 (Δ=0.16 ns) 双重确认")
