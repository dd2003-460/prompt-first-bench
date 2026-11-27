# N74: 敏感性系数 k 的边界条件与失效修正：公式 CTR' = C0 * (1 - k*偏离度) 假设线性负相关，但当偏离度 D > 25% 时，由于‘稀缺性信号’效

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

敏感性系数 k 的边界条件与失效修正：公式 CTR' = C0 * (1 - k*偏离度) 假设线性负相关，但当偏离度 D > 25% 时，由于‘稀缺性信号’效应（N9），CTR 可能不降反升或降幅收窄。修正公式为 CTR' = C0 * (1 - k*D) * exp(λ_rarity * max(0, D - 25%))，其中 λ_rarity 为稀缺性溢价系数，需通过 D > 25% 子样本回归确定。

## Corrected Claim

敏感性系数 k 的边界条件与失效修正：公式 CTR' = C0 * (1 - k*偏离度) 假设线性负相关，但当偏离度 D > 25% 时，由于‘稀缺性信号’效应（N9），CTR 可能不降反升或降幅收窄。修正公式为 CTR' = C0 * (1 - k*D) * exp(λ_rarity * max(0, D - 25%))，其中 λ_rarity 为稀缺性溢价系数，需通过 D > 25% 子样本回归确定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price deviation effect on click through rate luxury goods signaling effect
