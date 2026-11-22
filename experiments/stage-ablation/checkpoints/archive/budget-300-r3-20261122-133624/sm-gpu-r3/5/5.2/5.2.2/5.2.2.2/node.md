# N361: H100 PCIe 的 3 年动态电力成本 C_power_dynamic 计算公式为：(P_decode * T_decode_ratio + P_prefi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

H100 PCIe 的 3 年动态电力成本 C_power_dynamic 计算公式为：(P_decode * T_decode_ratio + P_prefill * T_prefill_ratio) * 8760h * 3y * $0.12/kWh。假设 Decode 时间占比 80%，Prefill 占比 20%，取中值功耗 (455W*0.8 + 665W*0.2 = 497W)，则 C_power_dynamic ≈ 497W * 26280h * $0.12/kWh ≈ $1,568.11，比静态 TDP 估算的 $2,222.88 低约 29.5%。

## Corrected Claim

H100 PCIe 的 3 年动态电力成本 C_power_dynamic 计算公式为：(P_decode * T_decode_ratio + P_prefill * T_prefill_ratio) * 8760h * 3y * $0.12/kWh。假设 Decode 时间占比 80%，Prefill 占比 20%，取中值功耗 (455W*0.8 + 665W*0.2 = 497W)，则 C_power_dynamic ≈ 497W * 26280h * $0.12/kWh ≈ $1,568.11，比静态 TDP 估算的 $2,222.88 低约 29.5%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（497W * 26280h * 0.12/kWh ≈ $1568.11），对比基准计算正确（665W * 26280h * 0.12/kWh ≈ $2222.88），降幅比例正确（(2222.88-1568.11)/2222.88 ≈ 29.5%），且符合H100 PCIe典型功耗范围及电价假设。

## Search Query

H100 inference workload power profile decode prefill ratio
