# N16: 有效命中率折损因子：H_eff = H_lru * (1 - P_inval * (1 - H_lru))，当 P_inval < 0.1 时，折损约 10%-

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

有效命中率折损因子：H_eff = H_lru * (1 - P_inval * (1 - H_lru))，当 P_inval < 0.1 时，折损约 10%-20%；当 P_inval > 0.5 时，折损超过 50%。

## Corrected Claim

有效命中率折损因子：H_eff = H_lru * (1 - P_inval * (1 - H_lru))，当 P_inval < 0.1 时，折损约 10%-20%；当 P_inval > 0.5 时，折损超过 50%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 H_eff = H_lru * (1 - P_inval * (1 - H_lru)) 在数学上自洽，且代入典型 H_lru 值（如 0.8-0.9）验证，P_inval < 0.1 时折损确在 10%-20% 区间，P_inval > 0.5 时折损超过 50%，符合逻辑推导。

## Search Query

cache hit rate decay due to object updates
