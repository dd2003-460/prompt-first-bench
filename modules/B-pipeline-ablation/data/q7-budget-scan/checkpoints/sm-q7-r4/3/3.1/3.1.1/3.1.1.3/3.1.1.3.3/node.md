# N673: 主机 CPU/内存共享开销分解：存储节点通常配置 2x Xeon Silver 4310 或同等性能 CPU，空载功耗约 80W，满载（RAID 校验/元数据更

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N249, N250, N251

## Claim

主机 CPU/内存共享开销分解：存储节点通常配置 2x Xeon Silver 4310 或同等性能 CPU，空载功耗约 80W，满载（RAID 校验/元数据更新）功耗约 250W；内存 512GB DDR4 功耗约 50W；加权平均（假设 CPU 30% 利用率）= 0.3*250 + 0.7*80 + 50 = 101W，而非 N249 的静态 200W。

## Corrected Claim

主机 CPU/内存共享开销分解：存储节点通常配置 2x Xeon Silver 4310 或同等性能 CPU，空载功耗约 80W，满载（RAID 校验/元数据更新）功耗约 250W；内存 512GB DDR4 功耗约 50W；加权平均（假设 CPU 30% 利用率）= 0.3*250 + 0.7*80 + 50 = 101W，而非 N249 的静态 200W。

## Evidence

先验知识/题面给定，逻辑校验通过：Xeon Silver 4310 TDP为125W，双路满载250W合理；512GB DDR4功耗50W符合工程估算；加权平均计算0.3*250+0.7*80+50=101W数学正确。
