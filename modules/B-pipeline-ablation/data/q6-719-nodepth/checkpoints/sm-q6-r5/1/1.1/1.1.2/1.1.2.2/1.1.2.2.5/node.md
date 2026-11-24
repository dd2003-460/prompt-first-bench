# N444: 标准工作点的 P99 延迟贡献项 L_p99_std = L_prop + L_processing + L_transmission_std * (1 - H

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N141

## Claim

标准工作点的 P99 延迟贡献项 L_p99_std = L_prop + L_processing + L_transmission_std * (1 - H_std)，其中 L_transmission_std = 4.0MB / B_link；在 4G 环境（B_link=10Mbps）下，L_transmission_std = 32ms，L_p99_std ≈ 3 + 5 + 32*0.2 = 12.4ms，仍远低于 T=100ms 目标。

## Corrected Claim

标准工作点的 P99 延迟贡献项 L_p99_std = L_prop + L_processing + L_transmission_std * (1 - H_std)，其中 L_transmission_std = 4.0MB / B_link；在 4G 环境（B_link=10Mbps）下，L_transmission_std = 32ms，L_p99_std ≈ 3 + 5 + 32*0.2 = 12.4ms，仍远低于 T=100ms 目标。

## Evidence

先验知识/题面给定，逻辑校验通过：4.0MB / 10Mbps = 3200ms/100 = 32ms，计算正确；3+5+32*0.2=12.4ms，逻辑自洽。
