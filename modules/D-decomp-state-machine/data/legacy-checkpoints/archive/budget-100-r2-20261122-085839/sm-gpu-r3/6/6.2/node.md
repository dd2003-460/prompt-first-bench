# N96: 多卡互联带宽筛选阈值：PCIe 4.0 x16 单向带宽 32 GB/s，双向 64 GB/s；NVLink 4.0 带宽 900 GB/s。对于 27B 模型

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

多卡互联带宽筛选阈值：PCIe 4.0 x16 单向带宽 32 GB/s，双向 64 GB/s；NVLink 4.0 带宽 900 GB/s。对于 27B 模型，每层 Activation 大小约为 27.1B/48 layers * 2 bytes ≈ 1.13 GB/layer，PCIe 方案在 TP=2 时通信开销占比 = (2 * 1.13 GB * 48 layers) / (64 GB/s * T_step) [待核验: 具体 T_step 和框架实现]，通常导致 15%-30% 吞吐损失，故单卡显存不足时需优先选择 NVLink 或高带宽 PCIe 5.0 方案。

## Corrected Claim

多卡互联带宽筛选阈值：PCIe 4.0 x16 单向带宽 32 GB/s，双向 64 GB/s；NVLink 4.0 带宽 900 GB/s。对于 27B 模型，每层 Activation 大小约为 27.1B/48 layers * 2 bytes ≈ 1.13 GB/layer，PCIe 方案在 TP=2 时通信开销占比 = (2 * 1.13 GB * 48 layers) / (64 GB/s * T_step) [待核验: 具体 T_step 和框架实现]，通常导致 15%-30% 吞吐损失，故单卡显存不足时需优先选择 NVLink 或高带宽 PCIe 5.0 方案。

## Evidence

父节点级核验未通过：有冗余（子节点在逻辑上是正交的（分别针对 Decode、Prefill、NVLink 对比三个不同场景/硬件条件），且覆盖了父节点关于带宽、模型规模、通信开销占比及结论的所有关键方面。然而，存在显著冗余：子节点1、2、3本质上都是对同一个核心公式（通信时间/计算时间）在不同参数（互联类型、阶段、Batch Size）下的实例化计算。它们共同指向同一个核心结论：在27B模型当前规模下，通信开销占比极低，父节点中声称的15%-30%损失被高估或仅适用于极端未提及的条件。因此，这三个子节点可以压缩为一个更通用的分析框架或参数化表格，而非三个独立的长篇推导。）

## Search Query

PCIe vs NVLink impact on LLM inference throughput tensor parallelism
