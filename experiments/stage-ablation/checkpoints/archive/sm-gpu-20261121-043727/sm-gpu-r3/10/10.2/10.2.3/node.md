# N276: 对比 H200 与 2x H100 的 T_decode 加速比：H200 (18.1us) vs 2x H100 (15us)。2x H100 比 H200 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

对比 H200 与 2x H100 的 T_decode 加速比：H200 (18.1us) vs 2x H100 (15us)。2x H100 比 H200 快约 1.2x (18.1/15)。这与 N78 中 H200 比 H100 快 1.43x 的单卡对比不同，因为 2x H100 的聚合带宽 (6.7TB/s) 超过了 H200 (4.8TB/s)，且 NVLink 开销在短通信量下影响较小。

## Corrected Claim

对比 H200 与 2x H100 的 T_decode 加速比：H200 (18.1us) vs 2x H100 (15us)。2x H100 比 H200 快约 1.2x (18.1/15)。这与 N78 中 H200 比 H100 快 1.43x 的单卡对比不同，因为 2x H100 的聚合带宽 (6.7TB/s) 超过了 H200 (4.8TB/s)，且 NVLink 开销在短通信量下影响较小。

## Evidence

先验知识/题面给定，逻辑校验通过：H200单卡带宽(4.8TB/s)低于2x H100聚合带宽(6.7TB/s)，在解码阶段受带宽限制时，2x H100理论上应更快，数值关系(18.1us vs 15us)与带宽比例及NVLink开销逻辑自洽。
