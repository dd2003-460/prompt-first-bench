# N112: 在 PCIe Gen4 x16 互联下，2×RTX 4090 进行张量并行（Tensor Parallelism）时，每层 Attention 输出和 FFN 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24, N25, N26

## Claim

在 PCIe Gen4 x16 互联下，2×RTX 4090 进行张量并行（Tensor Parallelism）时，每层 Attention 输出和 FFN 中间层的全量张量同步导致的通信开销约为总计算时间的 5%-15%，具体取决于层数和隐藏层维度，此损耗需从理论吞吐量中扣除。

## Corrected Claim

在 PCIe Gen4 x16 互联下，2×RTX 4090 进行张量并行（Tensor Parallelism）时，每层 Attention 输出和 FFN 中间层的全量张量同步导致的通信开销约为总计算时间的 5%-15%，具体取决于层数和隐藏层维度，此损耗需从理论吞吐量中扣除。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

tensor parallelism PCIe communication overhead percentage LLM inference
