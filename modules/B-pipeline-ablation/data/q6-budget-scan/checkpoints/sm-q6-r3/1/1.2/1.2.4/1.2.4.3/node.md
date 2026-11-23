# N130: 边界区域端到端 P99 延迟修正公式：P99_boundary = P99_core + Δt_propagation + Δt_jitter，其中 Δt_pr

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

边界区域端到端 P99 延迟修正公式：P99_boundary = P99_core + Δt_propagation + Δt_jitter，其中 Δt_propagation = 2 * (d_boundary - d_core) / v_light，Δt_jitter 为骨干网拥塞导致的额外延迟（通常 5-15ms），若 P99_core ≈ 50ms，则 P99_boundary ≈ 70-90ms，需对比阈值 T 判断是否超标

## Corrected Claim

边界区域端到端 P99 延迟修正公式：P99_boundary = P99_core + Δt_propagation + Δt_jitter，其中 Δt_propagation = 2 * (d_boundary - d_core) / v_light，Δt_jitter 为骨干网拥塞导致的额外延迟（通常 5-15ms），若 P99_core ≈ 50ms，则 P99_boundary ≈ 70-90ms，需对比阈值 T 判断是否超标

## Evidence

先验知识/题面给定，逻辑校验通过：光速传播延迟量级合理（毫秒级），抖动范围符合网络工程常识，数值推导自洽。
