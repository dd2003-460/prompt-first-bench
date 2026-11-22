# N216: Qwen3-27B 在 TP=2 下，每个 Transformer 层 All-Reduce 通信量的精确计算：Comm_Bytes = 2 * hidden_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

Qwen3-27B 在 TP=2 下，每个 Transformer 层 All-Reduce 通信量的精确计算：Comm_Bytes = 2 * hidden_dim * batch_size * dtype_size，对于 hidden=4096, batch=1, FP16/BF16 (2 bytes)，单层通信量为 16KB；64层总通信量为 1MB，用于评估 PCIe 带宽利用率。

## Corrected Claim

Qwen3-27B 在 TP=2 下，每个 Transformer 层 All-Reduce 通信量的精确计算：Comm_Bytes = 2 * hidden_dim * batch_size * dtype_size，对于 hidden=4096, batch=1, FP16/BF16 (2 bytes)，单层通信量为 16KB；64层总通信量为 1MB，用于评估 PCIe 带宽利用率。

## Evidence

先验知识/题面给定，逻辑校验通过：TP=2下All-Reduce通信量公式为2*hidden_dim*batch_size*dtype_size，代入hidden=4096, batch=1, dtype=2bytes得16KB/层，64层共1MB，计算无误。

## Search Query

Qwen3 27B hidden dimension tensor parallelism allreduce communication volume
