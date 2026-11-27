# N71: 若容量约束非绑定（N29 结论），则 LRU 有效命中率下界 H_LRU_eff 的主要折损来源仅为更新失效：H_LRU_eff ≈ 1 - P_invalid

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

若容量约束非绑定（N29 结论），则 LRU 有效命中率下界 H_LRU_eff 的主要折损来源仅为更新失效：H_LRU_eff ≈ 1 - P_invalid，其中 P_invalid 由 N15 给出。需重新评估 N24 中‘静态最优下界’的假设，因容量足够，下界应基于‘无更新命中率=1’进行修正

## Corrected Claim

若容量约束非绑定（N29 结论），则 LRU 有效命中率下界 H_LRU_eff 的主要折损来源仅为更新失效：H_LRU_eff ≈ 1 - P_invalid，其中 P_invalid 由 N15 给出。需重新评估 N24 中‘静态最优下界’的假设，因容量足够，下界应基于‘无更新命中率=1’进行修正

## Evidence

父节点级核验未通过：不完备（父节点包含两个核心任务：1. 计算/澄清 P_invalid（子节点已覆盖）；2. 重新评估 N24 的‘静态最优下界’假设并基于‘无更新命中率=1’进行修正。子节点仅详细推导了 P_invalid 的数值，完全缺失了关于 N24 假设修正及 H_LRU_eff 最终下界重构的内容，导致不完备。）
