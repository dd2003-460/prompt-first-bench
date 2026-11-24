# N109: 故障期间额外延迟成本量化公式：Cost_latency_extra = (L_p99_fault - L_p99_normal) × R_daily × p_f

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

故障期间额外延迟成本量化公式：Cost_latency_extra = (L_p99_fault - L_p99_normal) × R_daily × p_fail × T_fault × Lambda，其中 L_p99_fault = 150ms，L_p99_normal = 50ms，R_daily = 1.34×10^9 req/day，p_fail = 0.0154/月，T_fault = 4 小时/次（平均修复时间 MTTR），Lambda = ¥0.001/ms/req；计算得 Cost_latency_extra ≈ 50 × 1.34×10^9 × 0.0154 × (4/24) × 0.001 = ¥43,230/月。

## Corrected Claim

故障期间额外延迟成本量化公式：Cost_latency_extra = (L_p99_fault - L_p99_normal) × R_daily × p_fail × T_fault × Lambda，其中 L_p99_fault = 150ms，L_p99_normal = 50ms，R_daily = 1.34×10^9 req/day，p_fail = 0.0154/月，T_fault = 4 小时/次（平均修复时间 MTTR），Lambda = ¥0.001/ms/req；计算得 Cost_latency_extra ≈ 50 × 1.34×10^9 × 0.0154 × (4/24) × 0.001 = ¥43,230/月。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上是正交的，分别针对MTTR、Lambda和p_fail/T_fault的时间尺度问题，没有重复或矛盾。然而，完备性存在问题：父节点公式中明确包含了R_daily（日请求量）和ΔL（延迟差值，即L_p99_fault - L_p99_normal）这两个关键参数，但子节点未对其分解或来源进行解释（例如，R_daily如何估算？ΔL是否稳定？）。此外，子节点3修正了公式的时间尺度，但未明确说明修正后的公式是否替代原公式，可能导致理解混淆。）
