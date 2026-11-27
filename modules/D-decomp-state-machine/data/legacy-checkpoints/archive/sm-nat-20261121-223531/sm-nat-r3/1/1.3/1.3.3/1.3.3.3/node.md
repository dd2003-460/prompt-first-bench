# N111: 字节命中率计算中的更新惩罚项量化：在模拟中，若对象在缓存期间发生更新（概率 P_update = 1 - exp(-0.01 * T_res)），该请求视为 M

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33, N34, N36

## Claim

字节命中率计算中的更新惩罚项量化：在模拟中，若对象在缓存期间发生更新（概率 P_update = 1 - exp(-0.01 * T_res)），该请求视为 Miss 并触发缓存失效；需统计因更新导致的额外 Miss 比例 ΔH_upd，预期值在 0.5%-2% 之间，用于修正纯 LRU 命中率下界。

## Corrected Claim

字节命中率计算中的更新惩罚项量化：在模拟中，若对象在缓存期间发生更新（概率 P_update = 1 - exp(-0.01 * T_res)），该请求视为 Miss 并触发缓存失效；需统计因更新导致的额外 Miss 比例 ΔH_upd，预期值在 0.5%-2% 之间，用于修正纯 LRU 命中率下界。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache invalidation update rate impact hit rate simulation
