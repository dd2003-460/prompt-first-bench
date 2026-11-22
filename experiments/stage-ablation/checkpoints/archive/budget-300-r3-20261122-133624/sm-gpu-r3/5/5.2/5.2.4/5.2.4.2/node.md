# N367: H200 的 3 年动态电力成本 C_power_dynamic 计算公式为：(P_decode * T_decode_ratio + P_prefill * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N132

## Claim

H200 的 3 年动态电力成本 C_power_dynamic 计算公式为：(P_decode * T_decode_ratio + P_prefill * T_prefill_ratio) * 8760h * 3y * $0.12/kWh。假设 Decode 时间占比 80%，Prefill 占比 20%，取中值功耗 (420W*0.8 + 682.5W*0.2 = 472.5W)，则 C_power_dynamic ≈ 472.5W * 26280h * $0.12/kWh ≈ $1,490.22，比静态 TDP 估算的 $2,222.88 低约 33%。

## Corrected Claim

H200 的 3 年动态电力成本 C_power_dynamic 计算公式为：(P_decode * T_decode_ratio + P_prefill * T_prefill_ratio) * 8760h * 3y * $0.12/kWh。假设 Decode 时间占比 80%，Prefill 占比 20%，取中值功耗 (420W*0.8 + 682.5W*0.2 = 472.5W)，则 C_power_dynamic ≈ 472.5W * 26280h * $0.12/kWh ≈ $1,490.22，比静态 TDP 估算的 $2,222.88 低约 33%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（472.5W * 26280h * 0.12/kWh ≈ $1490.22），对比静态估算（682.5W * 26280h * 0.12/kWh ≈ $2222.88）的降幅约33%符合逻辑，且H200功耗参数在合理范围内。
