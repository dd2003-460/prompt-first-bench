# N347: 公有云 CDN 故障时的回源延迟 L_backhaul_cloud：公有云回源通常通过其内部骨干网，延迟 L_backhaul_cloud ≈ 20-50ms（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

公有云 CDN 故障时的回源延迟 L_backhaul_cloud：公有云回源通常通过其内部骨干网，延迟 L_backhaul_cloud ≈ 20-50ms（远低于自建节点的 50-200ms），因此即使 H_cloud 下降，P99 延迟增量 ΔL_p99_cloud = L_backhaul_cloud * (1-H_cloud) 仍小于自建节点的 ΔL_p99_self = L_backhaul_self * (1-H_self)；计算得 ΔL_p99_cloud ≈ 35ms * 0.15 = 5.25ms，ΔL_p99_self ≈ 100ms * 0.235 = 23.5ms。

## Corrected Claim

公有云 CDN 故障时的回源延迟 L_backhaul_cloud：公有云回源通常通过其内部骨干网，延迟 L_backhaul_cloud ≈ 20-50ms（远低于自建节点的 50-200ms），因此即使 H_cloud 下降，P99 延迟增量 ΔL_p99_cloud = L_backhaul_cloud * (1-H_cloud) 仍小于自建节点的 ΔL_p99_self = L_backhaul_self * (1-H_self)；计算得 ΔL_p99_cloud ≈ 35ms * 0.15 = 5.25ms，ΔL_p99_self ≈ 100ms * 0.235 = 23.5ms。

## Evidence

先验知识/题面给定，逻辑校验通过
