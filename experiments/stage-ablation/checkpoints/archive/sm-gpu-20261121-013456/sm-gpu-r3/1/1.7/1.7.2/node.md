# N69: 若采用 MHA (32 KV heads) 配置，32K 上下文、Batch Size=1 的 KV Cache 精确占用为 17.18 GB，是 GQA 方案

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

若采用 MHA (32 KV heads) 配置，32K 上下文、Batch Size=1 的 KV Cache 精确占用为 17.18 GB，是 GQA 方案的 4 倍

## Corrected Claim

若采用 MHA (32 KV heads) 配置，32K 上下文、Batch Size=1 的 KV Cache 精确占用为 17.18 GB，是 GQA 方案的 4 倍

## Evidence

父节点级核验未通过：不完备（子节点之间存在严重的数值矛盾（子节点1修正了父节点数值，但子节点2未同步修正，仍基于修正后的67.2GB计算，导致逻辑链断裂且与父节点原始claim脱节）。此外，父节点核心claim是'17.18GB是GQA的4倍'，子节点完全未解释GQA侧的数值来源及为何MHA是GQA的4倍（通常MHA heads=32, GQA heads=8, 比例应为4:1，但17.18GB的数值来源不明，子节点直接否定父节点数值而未验证其合理性，导致分解未能忠实覆盖父节点的'对比'维度）。）
