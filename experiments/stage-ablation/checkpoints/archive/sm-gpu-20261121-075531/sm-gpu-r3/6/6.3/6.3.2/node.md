# N329: 2x RTX 4090 (TP=2) 在 PCIe 4.0 x8/x8 配置下，每层 Transformer 的 AllReduce 通信数据量为 2 * hi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

2x RTX 4090 (TP=2) 在 PCIe 4.0 x8/x8 配置下，每层 Transformer 的 AllReduce 通信数据量为 2 * hidden_size * batch_size * dtype_size = 2 * 4096 * 1 * 2 bytes = 16KB/层，32 层总通信量 512KB/Token；PCIe x8 单向有效带宽约 15 GB/s，通信耗时约 0.034ms/Token，占 4090 单卡 Decode 耗时 (~25ms/Token) 的 0.14%，表明 PCIe 带宽瓶颈对 Decode 阶段 TPS 影响极小 (<1%)，主要影响在 Prefill 阶段的大 Batch 场景。

## Corrected Claim

2x RTX 4090 (TP=2) 在 PCIe 4.0 x8/x8 配置下，每层 Transformer 的 AllReduce 通信数据量为 2 * hidden_size * batch_size * dtype_size = 2 * 4096 * 1 * 2 bytes = 16KB/层，32 层总通信量 512KB/Token；PCIe x8 单向有效带宽约 15 GB/s，通信耗时约 0.034ms/Token，占 4090 单卡 Decode 耗时 (~25ms/Token) 的 0.14%，表明 PCIe 带宽瓶颈对 Decode 阶段 TPS 影响极小 (<1%)，主要影响在 Prefill 阶段的大 Batch 场景。

## Evidence

先验知识/题面给定，逻辑校验通过：AllReduce 通信量计算（2 * 4096 * 1 * 2 = 16KB/层，32层共512KB）及耗时估算（512KB / 15GB/s ≈ 0.034ms）符合物理直觉与数学逻辑，占比计算正确。

## Search Query

Tensor Parallelism PCIe bottleneck LLM inference latency
