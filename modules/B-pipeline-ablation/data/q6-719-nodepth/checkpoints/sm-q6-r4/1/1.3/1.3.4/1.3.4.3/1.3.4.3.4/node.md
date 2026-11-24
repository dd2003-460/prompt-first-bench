# N517: s_median 对 P99 延迟分母校准的影响：P99_Latency_Denominator = s_median / Effective_Bandwidt

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N173

## Claim

s_median 对 P99 延迟分母校准的影响：P99_Latency_Denominator = s_median / Effective_Bandwidth_to_Origin，若 s_median=3.2MB, Effective_Bandwidth=100Mbps，则 P99_Latency_Denominator ≈ 0.26s，需与 s_avg 计算结果 0.29s 对比，确认使用哪个值更保守

## Corrected Claim

s_median 对 P99 延迟分母校准的影响：P99_Latency_Denominator = s_median / Effective_Bandwidth_to_Origin，若 s_median=3.2MB, Effective_Bandwidth=100Mbps，则 P99_Latency_Denominator ≈ 0.26s，需与 s_avg 计算结果 0.29s 对比，确认使用哪个值更保守

## Evidence

先验知识/题面给定，逻辑校验通过：3.2MB * 8 / 100Mbps = 0.256s ≈ 0.26s，计算无误且量级合理
