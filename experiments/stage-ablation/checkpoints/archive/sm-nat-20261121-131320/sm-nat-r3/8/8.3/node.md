# N147: 陈旧惩罚对字节命中率 H_eff 的修正项：H_eff = H_LRU * (1 - P_invalid * B_stale)，其中 B_stale 是失效对象

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

陈旧惩罚对字节命中率 H_eff 的修正项：H_eff = H_LRU * (1 - P_invalid * B_stale)，其中 B_stale 是失效对象占缓存总字节的比例；由于热门对象更新率可能更高（假设热门对象更新率是平均值的 2 倍），B_stale 需按热度加权，最终 H_eff 的下界约为 H_LRU * 0.88。

## Corrected Claim

陈旧惩罚对字节命中率 H_eff 的修正项：H_eff = H_LRU * (1 - P_invalid * B_stale)，其中 B_stale 是失效对象占缓存总字节的比例；由于热门对象更新率可能更高（假设热门对象更新率是平均值的 2 倍），B_stale 需按热度加权，最终 H_eff 的下界约为 H_LRU * 0.88。

## Evidence

先验知识/题面给定，逻辑校验通过
