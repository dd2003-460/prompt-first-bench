# N55: LRU有效命中率折扣因子 D_eff 的量化计算：D_eff = 1 - M_invalidation。若 M_invalidation ≈ 0.005（来自 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

LRU有效命中率折扣因子 D_eff 的量化计算：D_eff = 1 - M_invalidation。若 M_invalidation ≈ 0.005（来自 N30），则 D_eff ≈ 0.995，即命中率打 99.5 折。

## Corrected Claim

LRU有效命中率折扣因子 D_eff 的量化计算：D_eff = 1 - M_invalidation。若 M_invalidation ≈ 0.005（来自 N30），则 D_eff ≈ 0.995，即命中率打 99.5 折。

## Evidence

先验知识/题面给定，逻辑校验通过：D_eff = 1 - M_invalidation 是定义式，代入 M_invalidation ≈ 0.005 得 0.995，数学推导自洽且量级合理。
