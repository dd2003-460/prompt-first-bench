# N249: 预热时间窗口 T_warm 的调度约束：预热需在业务低峰期执行，若低峰期时长 T_offpeak < T_warm，则预热无法在低峰期完成，需跨峰期执行，跨峰期

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

预热时间窗口 T_warm 的调度约束：预热需在业务低峰期执行，若低峰期时长 T_offpeak < T_warm，则预热无法在低峰期完成，需跨峰期执行，跨峰期预热时间占比 r_cross = (T_warm - T_offpeak) / T_warm 导致额外实时延迟成本 C_cross = r_cross * Q_peak * ΔP99_realtime * c_penalty_ms

## Corrected Claim

预热时间窗口 T_warm 的调度约束：预热需在业务低峰期执行，若低峰期时长 T_offpeak < T_warm，则预热无法在低峰期完成，需跨峰期执行，跨峰期预热时间占比 r_cross = (T_warm - T_offpeak) / T_warm 导致额外实时延迟成本 C_cross = r_cross * Q_peak * ΔP99_realtime * c_penalty_ms

## Evidence

先验知识/题面给定，逻辑校验通过
