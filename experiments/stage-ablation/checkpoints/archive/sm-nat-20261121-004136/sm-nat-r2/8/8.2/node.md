# N71: 若容量约束非绑定（N29 结论），则 LRU 有效命中率下界 H_LRU_eff 的主要折损来源仅为更新失效：H_LRU_eff ≈ 1 - P_invalid

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

若容量约束非绑定（N29 结论），则 LRU 有效命中率下界 H_LRU_eff 的主要折损来源仅为更新失效：H_LRU_eff ≈ 1 - P_invalid，其中 P_invalid 由 N15 给出。需重新评估 N24 中‘静态最优下界’的假设，因容量足够，下界应基于‘无更新命中率=1’进行修正

## Corrected Claim

若容量约束非绑定（N29 结论），则 LRU 有效命中率下界 H_LRU_eff 的主要折损来源仅为更新失效：H_LRU_eff ≈ 1 - P_invalid，其中 P_invalid 由 N15 给出。需重新评估 N24 中‘静态最优下界’的假设，因容量足够，下界应基于‘无更新命中率=1’进行修正

## Evidence

先验知识/题面给定，逻辑校验通过：在容量非绑定且无更新失效的理想情况下，LRU命中率确实趋近于1，折损仅由更新失效（P_invalid）决定，推导自洽。
