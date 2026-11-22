# N462: Qwen3-27B 在 2 卡张量并行下，每层 Attention 计算后的 All-Reduce 通信数据量：2 * hidden_size * batch_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N147

## Claim

Qwen3-27B 在 2 卡张量并行下，每层 Attention 计算后的 All-Reduce 通信数据量：2 * hidden_size * batch_size * seq_len * dtype_size，对于 hidden_size=4096, batch_size=1, seq_len=1, dtype=BF16，每次通信量为 16 KB

## Corrected Claim

Qwen3-27B 在 2 卡张量并行下，每层 Attention 计算后的 All-Reduce 通信数据量：2 * hidden_size * batch_size * seq_len * dtype_size，对于 hidden_size=4096, batch_size=1, seq_len=1, dtype=BF16，每次通信量为 16 KB

## Evidence

先验知识/题面给定，逻辑校验通过：2 * 4096 * 1 * 1 * 2 bytes = 16384 bytes = 16 KB，计算无误且符合张量并行通信量级常识。

## Search Query

tensor parallelism all-reduce communication volume per layer
