# N267: RTX 4090 在 INT4 推理模式下的有效显存带宽（Memory_Bandwidth_Effective）需通过基准测试确定，通常低于峰值 1008 GB

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N96

## Claim

RTX 4090 在 INT4 推理模式下的有效显存带宽（Memory_Bandwidth_Effective）需通过基准测试确定，通常低于峰值 1008 GB/s，估算区间为 800-900 GB/s，具体值取决于驱动优化与内存访问模式。

## Corrected Claim

RTX 4090 在 INT4 推理模式下的有效显存带宽需通过基准测试确定，通常低于峰值 1008 GB/s，具体值取决于驱动优化与内存访问模式。

## Evidence

[质询]该陈述包含具体的经验性数值区间（800-900 GB/s），属于硬件性能经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4090 INT4 inference effective memory bandwidth benchmark GB/s
