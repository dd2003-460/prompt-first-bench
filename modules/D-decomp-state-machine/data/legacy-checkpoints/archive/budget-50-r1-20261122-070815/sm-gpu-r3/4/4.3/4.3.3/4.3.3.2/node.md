# N322: 在 2x RTX 4090 多卡推理中，若使用 tensor parallelism，每层 attention 后的 AllReduce 通信数据量约为 bat

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

在 2x RTX 4090 多卡推理中，若使用 tensor parallelism，每层 attention 后的 AllReduce 通信数据量约为 batch_size * hidden_dim * 2 bytes，需评估该通信量在 32 GB/s 带宽下的延迟占比是否超过 5% 导致整体吞吐下降

## Corrected Claim

在 2x RTX 4090 多卡推理中，若使用 tensor parallelism，每层 attention 后的 AllReduce 通信数据量约为 batch_size * hidden_dim * 2 bytes，需评估该通信量在 32 GB/s 带宽下的延迟占比是否超过 5% 导致整体吞吐下降

## Evidence

先验知识/题面给定，逻辑校验通过：Tensor Parallelism 中 Attention 输出需 AllReduce，数据量公式 batch_size * hidden_dim * dtype_size (2 bytes for FP16/BF16) 符合标准实现逻辑；32 GB/s 带宽下延迟占比评估属于合理的工程估算范畴，无逻辑矛盾。

## Search Query

tensor parallelism allreduce communication overhead latency percentage
