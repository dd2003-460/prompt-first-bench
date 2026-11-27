# N68: LRU 驱逐热度阈值 h_th 的计算公式：h_th = R_total / (N * C_norm) / (1 - (N+1)^{1-β})，其中 C_nor

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

LRU 驱逐热度阈值 h_th 的计算公式：h_th = R_total / (N * C_norm) / (1 - (N+1)^{1-β})，其中 C_norm=0.119, β=0.9, N=100,000，需计算具体数值以确定被驱逐对象的最低热度。

## Corrected Claim

LRU 驱逐热度阈值 h_th 的计算公式：h_th = R_total / (N * C_norm) / (1 - (N+1)^{1-β})，其中 C_norm=0.119, β=0.9, N=100,000，需计算具体数值以确定被驱逐对象的最低热度。

## Evidence

先验知识/题面给定，逻辑校验通过
