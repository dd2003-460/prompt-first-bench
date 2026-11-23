# N204: 公有云 CDN 边缘节点 CPU 计算成本的核心变量是 CPU 利用率 U_cpu，计算公式为 Cost_cpu = (Requests_per_sec × C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

公有云 CDN 边缘节点 CPU 计算成本的核心变量是 CPU 利用率 U_cpu，计算公式为 Cost_cpu = (Requests_per_sec × CPU_time_per_req) / (U_cpu × Cores_per_node) × Price_per_core_hour；典型 CDN 边缘节点 U_cpu 在低负载时仅为 5%-15%，导致单位成本远高于理论峰值估算。

## Corrected Claim

公有云 CDN 边缘节点 CPU 计算成本的核心变量是 CPU 利用率 U_cpu，计算公式为 Cost_cpu = (Requests_per_sec × CPU_time_per_req) / (U_cpu × Cores_per_node) × Price_per_core_hour；典型 CDN 边缘节点 U_cpu 在低负载时仅为 5%-15%，导致单位成本远高于理论峰值估算。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（请求率×单请求耗时=总CPU时间，除以利用率×核心数=所需核心数，乘以单价=成本），且CDN边缘节点低负载时CPU利用率低（5%-15%）导致单位成本高的结论符合工程直觉。

## Search Query

CDN edge node CPU utilization typical value low traffic cost efficiency
