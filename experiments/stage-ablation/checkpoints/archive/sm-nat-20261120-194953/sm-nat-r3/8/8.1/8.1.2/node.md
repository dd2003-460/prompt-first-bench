# N159: 在全量驻留（中性价比/高准确性）工作点下，基于 N81 修正 E[S]=6.9KB 导致 K_cap=1.9×10^7 >> 10^5，T_avg 公式失效，实

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

在全量驻留（中性价比/高准确性）工作点下，基于 N81 修正 E[S]=6.9KB 导致 K_cap=1.9×10^7 >> 10^5，T_avg 公式失效，实际驻留时间由更新率主导：T_avg ≈ 1/u = 100 天，此时 LRU 驱逐机制不活跃，命中率下界由 P_inval 决定而非容量竞争

## Corrected Claim

在全量驻留（中性价比/高准确性）工作点下，基于 N81 修正 E[S]=6.9KB 导致 K_cap=1.9×10^7 >> 10^5，T_avg 公式失效，实际驻留时间由更新率主导：T_avg ≈ 1/u = 100 天，此时 LRU 驱逐机制不活跃，命中率下界由 P_inval 决定而非容量竞争

## Evidence

先验知识/题面给定，逻辑校验通过：当容量远大于工作集时，LRU驱逐不活跃，驻留时间由更新率决定，命中率受失效概率主导，符合缓存理论第一性原理。
