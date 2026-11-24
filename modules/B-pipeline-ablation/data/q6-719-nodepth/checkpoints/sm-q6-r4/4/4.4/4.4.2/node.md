# N113: L2 命中率 H_L2 的计算模型：H_L2 = 1 - (Miss_L1 * (1 - H_origin))，其中 Miss_L1 为 L1 未命中率，H_o

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

L2 命中率 H_L2 的计算模型：H_L2 = 1 - (Miss_L1 * (1 - H_origin))，其中 Miss_L1 为 L1 未命中率，H_origin 为源站缓存命中率（通常为 0，即直接回源）；H_L2 受内容工作集大小 W 与 L2 容量 C_L2 之比影响，当 W/C_L2 < 0.5 时 H_L2 > 0.8，否则 H_L2 显著下降。

## Corrected Claim

L2 命中率 H_L2 的计算模型：H_L2 = 1 - (Miss_L1 * (1 - H_origin))，其中 Miss_L1 为 L1 未命中率，H_origin 为源站缓存命中率（通常为 0，即直接回源）；H_L2 受内容工作集大小 W 与 L2 容量 C_L2 之比影响，当 W/C_L2 < 0.5 时 H_L2 > 0.8，否则 H_L2 显著下降。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN L2 cache hit rate calculation model
