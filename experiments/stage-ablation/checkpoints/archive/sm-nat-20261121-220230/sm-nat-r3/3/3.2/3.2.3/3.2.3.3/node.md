# N176: LRU 有效命中率折损因子 D_LRU 的计算：D_LRU = 1 - P_invalid，若 P_invalid = 1.49%，则 D_LRU ≈ 0.98

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

LRU 有效命中率折损因子 D_LRU 的计算：D_LRU = 1 - P_invalid，若 P_invalid = 1.49%，则 D_LRU ≈ 0.9851，即命中率打 98.51 折；若 P_invalid = 0.5%，则 D_LRU ≈ 0.995，需结合 T_resident 的准确值确定最终折损系数。

## Corrected Claim

LRU 有效命中率折损因子 D_LRU 的计算：D_LRU = 1 - P_invalid，若 P_invalid = 1.49%，则 D_LRU ≈ 0.9851，即命中率打 98.51 折；若 P_invalid = 0.5%，则 D_LRU ≈ 0.995，需结合 T_resident 的准确值确定最终折损系数。

## Evidence

先验知识/题面给定，逻辑校验通过：D_LRU = 1 - P_invalid 为定义式，数值计算 1-0.0149=0.9851 和 1-0.005=0.995 准确无误，符合逻辑自洽要求。

## Search Query

cache hit rate discount factor invalidation
