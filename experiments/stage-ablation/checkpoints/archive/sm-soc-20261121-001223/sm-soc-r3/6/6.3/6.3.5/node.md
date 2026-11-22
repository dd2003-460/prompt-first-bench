# N200: 买家忽略概率 P_ignored 的量化模型：当 P_ask > P_avg * (1+δ) 时，P_ignored = 1 - exp(-k * (P_ask

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72, N73, N74

## Claim

买家忽略概率 P_ignored 的量化模型：当 P_ask > P_avg * (1+δ) 时，P_ignored = 1 - exp(-k * (P_ask - P_avg * (1+δ)) / P_avg)，其中 k 为敏感度系数；需校准 k 值以匹配平台实际点击率（CTR）数据，k 通常与平台算法的‘惩罚因子’正相关。

## Corrected Claim

买家忽略概率 P_ignored 的量化模型：当 P_ask > P_avg * (1+δ) 时，P_ignored = 1 - exp(-k * (P_ask - P_avg * (1+δ)) / P_avg)，其中 k 为敏感度系数；需校准 k 值以匹配平台实际点击率（CTR）数据，k 通常与平台算法的‘惩罚因子’正相关。

## Evidence

先验知识/题面给定，逻辑校验通过
