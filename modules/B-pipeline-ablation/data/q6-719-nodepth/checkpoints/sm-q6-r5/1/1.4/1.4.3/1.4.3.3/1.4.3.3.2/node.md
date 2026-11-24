# N481: QoS 降级对用户体验的影响量化：若触发 QoS 降级，带宽被限制至 B_degraded（如 50% 预留值），导致 P99 延迟增加 ΔL_qos = s_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N154

## Claim

QoS 降级对用户体验的影响量化：若触发 QoS 降级，带宽被限制至 B_degraded（如 50% 预留值），导致 P99 延迟增加 ΔL_qos = s_avg / (B_degraded - B_actual)；需计算 ΔL_qos 是否超过 P99 目标 T（N17），若超过则需提高 B_reserve。

## Corrected Claim

QoS 降级对用户体验的影响量化：若触发 QoS 降级，带宽被限制至 B_degraded（如 50% 预留值），导致 P99 延迟增加 ΔL_qos = s_avg / (B_degraded - B_actual)；需计算 ΔL_qos 是否超过 P99 目标 T（N17），若超过则需提高 B_reserve。

## Evidence

先验知识/题面给定，逻辑校验通过
