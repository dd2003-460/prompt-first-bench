# N55: 冷门对象（后90%）的更新折损因子 D_cold = 1 - e^{-λ_upd * T_res_cold}，其中 T_res_cold ≈ 0（因 LRU 堆

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

冷门对象（后90%）的更新折损因子 D_cold = 1 - e^{-λ_upd * T_res_cold}，其中 T_res_cold ≈ 0（因 LRU 堆栈底部对象驻留时间极短），计算得 D_cold ≈ 1 - e^0 = 0，即冷门对象折损可忽略，但需考虑其被更新后重新进入缓存的延迟。

## Corrected Claim

冷门对象（后90%）的更新折损因子 D_cold = 1 - e^{-λ_upd * T_res_cold}，其中 T_res_cold ≈ 0（因 LRU 堆栈底部对象驻留时间极短），计算得 D_cold ≈ 1 - e^0 = 0，即冷门对象折损可忽略，但需考虑其被更新后重新进入缓存的延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：数学上 1-e^0=0 成立，且 LRU 底部对象驻留时间极短导致更新概率趋近于 0 符合缓存替换策略的基本逻辑。

## Search Query

cold object update penalty LRU cache stack depth
