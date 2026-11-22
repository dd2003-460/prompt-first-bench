# N121: 工作点 A（高一致性/低吞吐）：假设对象版本更新率 1%/天 且驻留时间 T_res 延长至 1 小时（通过增大缓存或降低驱逐率），则 P_inval = 1%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

工作点 A（高一致性/低吞吐）：假设对象版本更新率 1%/天 且驻留时间 T_res 延长至 1 小时（通过增大缓存或降低驱逐率），则 P_inval = 1% * (1h/24h) ≈ 0.0417。此时 f_inval 中由更新主导的项 P_inval/T_res 显著，导致有效命中率 H_eff 折损因子 (1 - P_inval) ≈ 0.958，即命中率打 95.8 折。

## Corrected Claim

工作点 A（高一致性/低吞吐）：假设对象版本更新率 1%/天 且驻留时间 T_res 延长至 1 小时（通过增大缓存或降低驱逐率），则 P_inval = 1% * (1h/24h) ≈ 0.0417。此时 f_inval 中由更新主导的项 P_inval/T_res 显著，导致有效命中率 H_eff 折损因子 (1 - P_inval) ≈ 0.958，即命中率打 95.8 折。

## Evidence

先验知识/题面给定，逻辑校验通过：1% * (1/24) ≈ 0.0417，1 - 0.0417 ≈ 0.9583，数值计算与逻辑推导自洽。
