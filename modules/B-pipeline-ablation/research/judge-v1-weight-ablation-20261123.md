# Judge v1.0 权重敏感性消融（2026-11-23）

> ⚠️ **cov 分量已失效（2026-11-23 同日）**：本消融的 cov 来自旧 MAGNET 清零口径。
> cov 层修复（去重计数, commit f8482557f）后，含 cov 的权重行（0.5/0.5, 0.7/0.3,
> 0.3/0.7, 0/1）需重算。纯 depth 行（1.0/0.0）不受影响，"峰在 150"的 depth-only
> 结论仍成立。重算脚本: `research/k7-dedup-cov-recompute.py`（后台跑中）。

## 问题

judge v1.0 的 total = 0.5*depth + 0.5*cov，权重是 ad-hoc 的（无校准过程）。
若"峰在 150"依赖这组权重，则 finding 3 是 judge 的人造产物，不是实验发现。
这是 D 2026-11-23 问"judge 足够科学吗"时列出的缺口 #2，最便宜的验证路径。

## 数据源

`modules/B-pipeline-ablation/data/t53b/results-budget-scan.json`（15 runs,
5 budget × 3 rep, 连续 depth/cov 分量）——稿子 §4.3 的源。
⚠️ 注意：`judge-v1-budget-scan.json` 里的 depth 是**量化值**（0.667/0.8/0.9333），
与稿子口径不同，消融若用它会把峰误判到 719。两个文件并存，引用必须指明。

## 结果：峰在 150 对权重稳健（5/5 权重设置）

| 权重 | 50 | 100 | 150 | 300 | 719 | 峰 |
|---|---|---|---|---|---|---|
| 0.5d+0.5c | 0.1921 | 0.2843 | **0.3481** | 0.2692 | 0.2631 | 150 |
| 0.7d+0.3c | 0.2689 | 0.3447 | **0.3986** | 0.3325 | 0.3329 | 150 |
| 0.3d+0.7c | 0.1153 | 0.2239 | **0.2977** | 0.2059 | 0.1934 | 150 |
| 1.0d+0.0c | 0.3842 | 0.4352 | **0.4743** | 0.4275 | 0.4376 | 150 |
| 0.0d+1.0c | 0.0000 | 0.1333 | **0.2220** | 0.1110 | 0.0887 | 150 |

150 vs {100,300,719} 高原 gap：1.37–1.49 run-sd（三种混合权重）。

## 结论

- **权重不是"峰在 150"的驱动因素**。连纯 depth 和纯 cov 单独都给出 150 峰，
  说明 depth 和 cov 两个独立分量在 150 处同向抬升——这是数据里的结构，
  不是 0.5/0.5 组合出来的假象。
- 缺口 #2（ad-hoc 权重）从"可能致命"降级为"已验证稳健"。
- 仍不显著：n=3，gap 1.4 sd。rep scan（n=8）跑完后重跑本消融 + 显著性检验。
- 剩余缺口排序更新：①构念效度（depth≠研究质量，无证据）②单 gold ③L2 BOUND
  未实现。权重问题已关闭。

## 复现

```python
import json, numpy as np
from collections import defaultdict
d = json.load(open('modules/B-pipeline-ablation/data/t53b/results-budget-scan.json'))
by_b = defaultdict(list)
for r in d: by_b[r['budget']].append((r['depth'], r['coverage']))
for wd, wc in [(0.5,0.5),(0.7,0.3),(0.3,0.7),(1.0,0.0),(0.0,1.0)]:
    means = {b: (wd*np.array(v)[:,0]+wc*np.array(v)[:,1]).mean() for b,v in by_b.items()}
    print(wd, wc, {b: round(m,4) for b,m in means.items()}, max(means, key=means.get))
```
