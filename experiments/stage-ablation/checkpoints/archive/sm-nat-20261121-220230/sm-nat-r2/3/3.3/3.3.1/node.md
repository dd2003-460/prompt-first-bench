# N61: 在 LFU 策略下，由于高频对象长期驻留，T_avg_resident 趋于无穷大（或受限于最大 TTL），导致失效折扣因子 (1 - 0.01 * T_avg

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

在 LFU 策略下，由于高频对象长期驻留，T_avg_resident 趋于无穷大（或受限于最大 TTL），导致失效折扣因子 (1 - 0.01 * T_avg_resident) 趋近于 0，有效命中率 H_eff_LFU ≈ 0，这是 LFU 在高更新率场景下的极端劣势工作点。

## Corrected Claim

在 LFU 策略下，由于高频对象长期驻留，T_avg_resident 趋于无穷大（或受限于最大 TTL），导致失效折扣因子 (1 - 0.01 * T_avg_resident) 趋近于 0，有效命中率 H_eff_LFU ≈ 0，这是 LFU 在高更新率场景下的极端劣势工作点。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 策略下高频对象长期驻留导致 T_avg_resident 极大，代入公式 (1 - 0.01 * T_avg_resident) 确实趋近于 0，符合数学逻辑与缓存理论直觉。

## Search Query

LFU cache invalidation rate high update frequency impact
