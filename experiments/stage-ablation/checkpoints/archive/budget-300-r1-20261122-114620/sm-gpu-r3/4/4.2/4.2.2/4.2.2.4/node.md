# N330: 2x RTX 4090 双卡方案中，第二张卡通常运行在 PCIe Gen4 x4 (16 GB/s) 模式，导致权重加载时间 T_load 从单卡 x16 的 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N106, N107, N108

## Claim

2x RTX 4090 双卡方案中，第二张卡通常运行在 PCIe Gen4 x4 (16 GB/s) 模式，导致权重加载时间 T_load 从单卡 x16 的 1.69s 增加到 54GB / 16GB/s ≈ 3.375s，若采用 Tensor Parallelism，All-Reduce 通信延迟将显著增加，预计 P99 延迟增加 20-30%

## Corrected Claim

2x RTX 4090 双卡方案中，第二张卡通常运行在 PCIe Gen4 x4 模式，带宽约为 16GB/s（理论值），实际有效带宽更低。若加载 54GB 数据，理论最小时间约为 3.375s，但实际受协议开销影响会更长。Tensor Parallelism 下的 All-Reduce 通信延迟增加幅度取决于模型结构和网络拓扑，20-30% 为经验估计值，需具体测试验证。

## Evidence

[质询]数值量级与物理直觉存在矛盾：54GB 的权重数据量对于单张 RTX 4090 (24GB VRAM) 而言过大，无法在单卡上运行；若指双卡总容量或特定大模型，单卡 x16 加载 54GB 数据耗时 1.69s 意味着带宽高达 ~32GB/s，远超 PCIe Gen4 x16 的理论峰值 (~32GB/s) 和实际有效带宽 (~25-28GB/s)，且 54GB/16GB/s=3.375s 的计算忽略了 PCIe 协议开销和实际传输效率，导致时间估算过于理想化。 | 先验知识/题面给定，逻辑校验发现数值量级不合理（单卡容量不足、带宽估算过于理想化），且无外部来源支持，故降级。
