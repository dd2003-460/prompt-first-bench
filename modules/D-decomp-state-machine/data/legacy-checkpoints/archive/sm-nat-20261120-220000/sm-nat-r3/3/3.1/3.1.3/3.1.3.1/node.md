# N102: 修正N36公式中的f_refill项：f_refill不应为源站不可用率(0.21%)，而应为'重填充期间并发请求导致额外Miss'的概率。根据N39，P(mi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N36

## Claim

修正N36公式中的f_refill项：f_refill不应为源站不可用率(0.21%)，而应为'重填充期间并发请求导致额外Miss'的概率。根据N39，P(miss|refill) ≈ 0.951。因此折损公式应修正为 H_eff = H_steady * (1 - p_invalid * P(miss|refill))。

## Corrected Claim

修正N36公式中的f_refill项：f_refill不应为源站不可用率(0.21%)，而应为'重填充期间并发请求导致额外Miss'的概率。根据N39，P(miss|refill) ≈ 0.951。因此折损公式应修正为 H_eff = H_steady * (1 - p_invalid * P(miss|refill))。

## Evidence

先验知识/题面给定，逻辑校验通过：将缓存失效后的重填充期间并发请求导致的额外Miss概率（P(miss|refill)）作为折损因子，在逻辑上比单纯使用源站不可用率更准确地反映了缓存命中率的有效折损，且公式结构 H_eff = H_steady * (1 - p_invalid * P(miss|refill)) 符合概率论中条件概率的乘法原理，量纲与量级合理。
