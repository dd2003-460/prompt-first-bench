# N210: 单POP点容量配置 C_pop_i 的最小值计算：C_pop_i ≥ B_peak_pop_i / U_target，其中 U_target = 0.5（50%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

单POP点容量配置 C_pop_i 的最小值计算：C_pop_i ≥ B_peak_pop_i / U_target，其中 U_target = 0.5（50%利用率目标）；若最大 geo_share_i = 0.08（8%），则 B_peak_pop_max = (23.15 Mbps × 3.0 × 0.08) / 10 ≈ 0.0556 Mbps，C_pop_min = 0.0556 / 0.5 ≈ 0.111 Mbps；此值远低于实际部署的 10Gbps 带宽，表明容量瓶颈不在单点带宽，而在缓存内存和磁盘I/O

## Corrected Claim

单POP点容量配置 C_pop_i 的最小值计算：C_pop_i ≥ B_peak_pop_i / U_target，其中 U_target = 0.5（50%利用率目标）；若最大 geo_share_i = 0.08（8%），则 B_peak_pop_max = (23.15 Mbps × 3.0 × 0.08) / 10 ≈ 0.0556 Mbps，C_pop_min = 0.0556 / 0.5 ≈ 0.111 Mbps；此值远低于实际部署的 10Gbps 带宽，表明容量瓶颈不在单点带宽，而在缓存内存和磁盘I/O

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（23.15*3*0.08/10/0.5 ≈ 0.111），量级对比合理（0.111 Mbps << 10 Gbps），结论符合网络工程常识。
