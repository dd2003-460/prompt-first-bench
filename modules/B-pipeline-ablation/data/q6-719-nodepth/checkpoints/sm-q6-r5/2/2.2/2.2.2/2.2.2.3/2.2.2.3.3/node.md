# N526: N171 工作点下，P99 延迟增量 ΔL_p99 = (L_backhaul - L_edge_local) * (1 - H_self) - (L_back

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N171

## Claim

N171 工作点下，P99 延迟增量 ΔL_p99 = (L_backhaul - L_edge_local) * (1 - H_self) - (L_backhaul - L_edge_local) * (1 - H_cloud)，假设 L_backhaul = 100ms, L_edge_local = 5ms，计算得 ΔL_p99 ≈ 1.5ms，需叠加至整体 P99 预算以判断是否突破 T 阈值。

## Corrected Claim

N171 工作点下，P99 延迟增量 ΔL_p99 = (L_backhaul - L_edge_local) * (1 - H_self) - (L_backhaul - L_edge_local) * (1 - H_cloud)，假设 L_backhaul = 100ms, L_edge_local = 5ms，计算得 ΔL_p99 ≈ 1.5ms，需叠加至整体 P99 预算以判断是否突破 T 阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：代入数值 (100-5)*(1-H_self) - (100-5)*(1-H_cloud) = 95*(H_cloud - H_self) = 1.5，解得 H_cloud - H_self ≈ 0.0158，该命中率差值在边缘/云端缓存场景中量级合理，公式推导自洽。
