# N133: 2×RTX 4060 Ti 方案中，由于缺乏 NVLink，张量并行 (TP=2) 需通过 PCIe 4.0 x16 (理论 32 GB/s) 同步激活值，每层

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

2×RTX 4060 Ti 方案中，由于缺乏 NVLink，张量并行 (TP=2) 需通过 PCIe 4.0 x16 (理论 32 GB/s) 同步激活值，每层通信开销约为 2 * Hidden_Dim * Batch_Size * 2 Bytes，在 Batch_Size=1 时通信延迟占比高达 30-50%，导致实际有效吞吐进一步下降至 5-6 tokens/s。

## Corrected Claim

2×RTX 4060 Ti 方案中，由于缺乏 NVLink，张量并行 (TP=2) 需通过 PCIe 4.0 x16 同步激活值，每层通信开销约为 2 * Hidden_Dim * Batch_Size * 2 Bytes。在 Batch_Size=1 时，通信延迟占比显著（具体比例取决于模型规模），导致实际有效吞吐大幅下降（通常远低于单卡推理效率）。

## Evidence

[质询]通信延迟占比高达30-50%及最终吞吐5-6 tokens/s属于高度依赖具体模型架构（如Hidden Dim大小、层数）和硬件微架构的经验性估算，缺乏通用性；且PCIe 4.0 x16双向理论带宽通常标称64GB/s（32GB/s为单向），此处表述易产生歧义，但核心逻辑（无NVLink导致TP通信瓶颈）成立。 | 先验知识/题面给定，逻辑校验通过：无NVLink时TP=2确实依赖PCIe，通信开销公式量纲正确，高延迟占比导致吞吐下降符合直觉，但具体数值为经验估算，故降级。
