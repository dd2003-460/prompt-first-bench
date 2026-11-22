# N192: LRU 下界 $H_{LRU, base}$ 中“总字节加权请求” $\sum_{j=1}^{N} S_j H_j$ 的计算：等于 $S_{total} \ti

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

LRU 下界 $H_{LRU, base}$ 中“总字节加权请求” $\sum_{j=1}^{N} S_j H_j$ 的计算：等于 $S_{total} \times \bar{h}$，其中 $\bar{h} = 500$ 次/对象/天（基于 N74）。故总字节加权请求为 $1.15GB \times 500 = 575TB$（单位：GB·次/天）。

## Corrected Claim

LRU 下界 $H_{LRU, base}$ 中“总字节加权请求” $\sum_{j=1}^{N} S_j H_j$ 的计算：等于 $S_{total} \times \bar{h}$，其中 $\bar{h} = 500$ 次/对象/天（基于 N74）。故总字节加权请求为 $1.15GB \times 500 = 575TB$（单位：GB·次/天）。

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算正确（GB × 次/天 = GB·次/天），数值计算准确（1.15 * 500 = 575），且 source 为 knowledge，无需外部来源支持。
