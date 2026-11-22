# N227: 修正 N83 中通信数据量计算错误：在 Tensor Parallelism (TP=4) 下，每层 AllReduce 的数据量仅为 2 * hidden_s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

修正 N83 中通信数据量计算错误：在 Tensor Parallelism (TP=4) 下，每层 AllReduce 的数据量仅为 2 * hidden_size * batch_size * dtype_size (BF16)，即 4096 * 1 * 2 bytes = 8 KB/layer (batch=1)，而非 N83 声称的 65.5 MB/layer (错误地乘入了 seq_len)。

## Corrected Claim

修正 N83 中通信数据量计算错误：在 Tensor Parallelism (TP=4) 下，每层 AllReduce 的数据量仅为 2 * hidden_size * batch_size * dtype_size (BF16)，即 4096 * 1 * 2 bytes = 8 KB/layer (batch=1)，而非 N83 声称的 65.5 MB/layer (错误地乘入了 seq_len)。

## Evidence

先验知识/题面给定，逻辑校验通过：TP AllReduce 通信量确实与 seq_len 无关，仅取决于 hidden_size 和 batch_size，计算 2 * 4096 * 1 * 2 = 8KB 正确。
