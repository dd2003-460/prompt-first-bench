# N133: P_inval 的时间尺度敏感性分析：若 T_life 从 100 天降至 1 天（高频更新场景），P_inval = 3.3min / 1440min ≈ 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55

## Claim

P_inval 的时间尺度敏感性分析：若 T_life 从 100 天降至 1 天（高频更新场景），P_inval = 3.3min / 1440min ≈ 0.0023。此时折损因子 (1 - P_inval) ≈ 0.9977，命中率损失约 0.23 个百分点，仍属可忽略范围，但需监控版本一致性开销。

## Corrected Claim

P_inval 的时间尺度敏感性分析：若 T_life 从 100 天降至 1 天（高频更新场景），P_inval = 3.3min / 1440min ≈ 0.0023。此时折损因子 (1 - P_inval) ≈ 0.9977，命中率损失约 0.23 个百分点，仍属可忽略范围，但需监控版本一致性开销。

## Evidence

先验知识/题面给定，逻辑校验通过：3.3/1440 ≈ 0.00229，1-0.00229 ≈ 0.9977，损失约0.23%，计算自洽且量级合理。
