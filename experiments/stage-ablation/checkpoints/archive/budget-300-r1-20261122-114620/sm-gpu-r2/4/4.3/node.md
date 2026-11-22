# N26: 互连带宽开销对推理吞吐的影响量化：PCIe Gen4 x16 带宽为 32 GB/s，NVLink 带宽为 900 GB/s (A100)，在 27B 模型 B

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

互连带宽开销对推理吞吐的影响量化：PCIe Gen4 x16 带宽为 32 GB/s，NVLink 带宽为 900 GB/s (A100)，在 27B 模型 BF16 权重下，多卡推理的 all-reduce 通信时间占比约为 (2 * 54GB / 32GB/s) / T_compute，需计算通信瓶颈导致的吞吐损失百分比

## Corrected Claim

互连带宽开销对推理吞吐的影响量化：PCIe Gen4 x16 带宽为 32 GB/s，NVLink 带宽为 900 GB/s (A100)，在 27B 模型 BF16 权重下，多卡推理的 all-reduce 通信时间占比约为 (2 * 54GB / 32GB/s) / T_compute，需计算通信瓶颈导致的吞吐损失百分比

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点1和2存在严重冗余，它们本质上是在计算同一个参数（初始加载时间）在不同带宽下的取值，而非独立的正交维度。此外，父节点核心要求量化 'all-reduce 通信时间占比' 和 '吞吐损失百分比'，子节点3仅给出公式，子节点4给出经验范围但未展示基于父节点给定参数（54GB, 32/900 GB/s）的具体计算过程，导致对父节点核心问题的覆盖不完整（缺少基于具体带宽和权重大小的定量推导）。）
