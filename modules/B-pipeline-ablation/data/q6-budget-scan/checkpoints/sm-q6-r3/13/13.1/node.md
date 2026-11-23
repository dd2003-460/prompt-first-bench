# N352: 延迟惩罚权重 λ_penalty 的校准方法：λ_penalty = (C_total_baseline / (P99_baseline - T)^2) * k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N111

## Claim

延迟惩罚权重 λ_penalty 的校准方法：λ_penalty = (C_total_baseline / (P99_baseline - T)^2) * k_risk，其中 k_risk 为风险厌恶系数（通常 1.0-2.0），确保当 P99 超标 10ms 时，惩罚项 C_penalty 占总成本 C_total 的 5%-10%

## Corrected Claim

延迟惩罚权重 λ_penalty 的校准方法：λ_penalty = (C_total_baseline / (P99_baseline - T)^2) * k_risk，其中 k_risk 为风险厌恶系数（通常 1.0-2.0），确保当 P99 超标 10ms 时，惩罚项 C_penalty 占总成本 C_total 的 5%-10%

## Evidence

先验知识/题面给定，逻辑校验通过
