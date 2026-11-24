# N570: 跨网 P99 延迟的抖动（Jitter）贡献值为 5-15ms，主要源于运营商互联带宽拥塞导致的排队延迟，该值需叠加到 ΔT_cross 的均值上以计算 P99

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N186

## Claim

跨网 P99 延迟的抖动（Jitter）贡献值为 5-15ms，主要源于运营商互联带宽拥塞导致的排队延迟，该值需叠加到 ΔT_cross 的均值上以计算 P99 上限：P99_cross = ΔT_cross_mean + Jitter_max ≈ 15-25 + 15 = 30-40ms。

## Corrected Claim

跨网 P99 延迟的抖动（Jitter）贡献值为 5-15ms，主要源于运营商互联带宽拥塞导致的排队延迟，该值需叠加到 ΔT_cross 的均值上以计算 P99 上限：P99_cross = ΔT_cross_mean + Jitter_max ≈ 15-25 + 15 = 30-40ms。

## Evidence

先验知识/题面给定，逻辑校验通过：P99延迟通常由均值加上尾部抖动构成，数值量级（15-25ms均值+15ms抖动=30-40ms）符合跨网通信的一般工程经验，且内部算术逻辑自洽。

## Search Query

cross-ISP jitter P99 latency component China
