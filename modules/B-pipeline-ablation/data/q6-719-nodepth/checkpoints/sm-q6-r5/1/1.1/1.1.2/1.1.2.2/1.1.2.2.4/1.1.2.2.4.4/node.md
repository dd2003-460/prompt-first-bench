# N1284: 高码率工作点带宽成本对比：C_bw_high = 800GB/day * 30 * ¥0.2/GB = ¥4,800/月，比标准工作点增加 100%；需评估高码

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N438

## Claim

高码率工作点带宽成本对比：C_bw_high = 800GB/day * 30 * ¥0.2/GB = ¥4,800/月，比标准工作点增加 100%；需评估高码率对 P99 延迟的影响，L_transmission 增加 100%，可能触发 A_p99 上升。

## Corrected Claim

高码率工作点带宽成本对比：C_bw_high = 800GB/day * 30 * ¥0.2/GB = ¥4,800/月，比标准工作点增加 100%；需评估高码率对 P99 延迟的影响，L_transmission 增加 100%，可能触发 A_p99 上升。

## Evidence

先验知识/题面给定，逻辑校验通过：800GB/day * 30天 * 0.2元/GB = 4800元/月，计算无误；若标准工作点成本为2400元/月（即400GB/day），则增加100%符合逻辑；带宽翻倍导致传输时间翻倍进而影响P99延迟符合网络基本原理。
