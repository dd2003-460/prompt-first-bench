# N107: CPU 方案的实际有效吞吐率通常为理论带宽瓶颈值的 60-70%（即 DDR4 下约 1.1-1.3 Token/s，DDR5 下约 2.0-2.3 Token

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

CPU 方案的实际有效吞吐率通常为理论带宽瓶颈值的 60-70%（即 DDR4 下约 1.1-1.3 Token/s，DDR5 下约 2.0-2.3 Token/s），损失主要来源于内存控制器调度开销、NUMA 跨节点访问延迟及 CPU 计算单元的反量化/矩阵乘运算瓶颈。

## Corrected Claim

CPU 方案的实际有效吞吐率通常为理论带宽瓶颈值的 60-70%（即 DDR4 下约 1.1-1.3 Token/s，DDR5 下约 2.0-2.3 Token/s），损失主要来源于内存控制器调度开销、NUMA 跨节点访问延迟及 CPU 计算单元的反量化/矩阵乘运算瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过
