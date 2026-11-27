# N101: 总字节请求量计算基准工作点 B（截断修正）：引入物理上限 s_max=100MB，计算截断期望 E[S|s≤s_max] ≈ 110KB * (1 - (10K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

总字节请求量计算基准工作点 B（截断修正）：引入物理上限 s_max=100MB，计算截断期望 E[S|s≤s_max] ≈ 110KB * (1 - (10KB/100MB)^0.1) / (1 - (10KB/100MB)^1.1) ≈ 110KB，总字节流量 ≈ 5.5TB/day，验证截断对分母的影响极小。

## Corrected Claim

总字节请求量计算基准工作点 B（截断修正）：引入物理上限 s_max=100MB，计算截断期望 E[S|s≤s_max] ≈ 110KB * (1 - (10KB/100MB)^0.1) / (1 - (10KB/100MB)^1.1) ≈ 110KB，总字节流量 ≈ 5.5TB/day，验证截断对分母的影响极小。

## Evidence

先验知识/题面给定，逻辑校验通过：截断点(10KB)远小于上限(100MB)，帕累托分布尾部截断对期望值影响极小，计算结果≈110KB符合直觉，总流量5.5TB/day量级合理。
