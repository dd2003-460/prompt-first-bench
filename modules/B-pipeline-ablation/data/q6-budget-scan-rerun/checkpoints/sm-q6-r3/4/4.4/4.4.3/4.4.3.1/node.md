# N215: 自建POP预热带宽占用的机会成本量化：预热带宽 B_prefetch = S_hot / T_prefetch，其中 S_hot = Top 1000 对象总大

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

自建POP预热带宽占用的机会成本量化：预热带宽 B_prefetch = S_hot / T_prefetch，其中 S_hot = Top 1000 对象总大小（约 2GB），T_prefetch = 15 分钟，B_prefetch = 2.22Mbps，占 10Gbps 带宽的 0.0222%，机会成本 = B_prefetch / B_total × 月度带宽费，假设月度带宽费 ¥20000，机会成本 = 0.000222 × 20000 = ¥4.44/月，年度 ¥53.28

## Corrected Claim

自建POP预热带宽占用的机会成本量化：预热带宽 B_prefetch = S_hot / T_prefetch，其中 S_hot = Top 1000 对象总大小（约 2GB），T_prefetch = 15 分钟，B_prefetch = 2.22Mbps，占 10Gbps 带宽的 0.0222%，机会成本 = B_prefetch / B_total × 月度带宽费，假设月度带宽费 ¥20000，机会成本 = 0.000222 × 20000 = ¥4.44/月，年度 ¥53.28

## Evidence

先验知识/题面给定，逻辑校验通过：2GB/900s ≈ 2.22Mbps，占比及成本计算数值准确且量级合理

## Search Query

self-hosted cdn prefetch bandwidth opportunity cost calculation
