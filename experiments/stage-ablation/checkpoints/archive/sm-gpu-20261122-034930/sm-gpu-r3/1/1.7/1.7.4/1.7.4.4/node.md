# N209: 在 Tensor Parallelism 下，每层 All-Reduce 通信的数据量公式为 2 * hidden_dim * seq_len * batch_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67, N68, N69

## Claim

在 Tensor Parallelism 下，每层 All-Reduce 通信的数据量公式为 2 * hidden_dim * seq_len * batch_size * dtype_size，对于 Qwen3-27B (hidden=4096, seq=32768, batch=1, FP16)，每层通信量为 2 * 4096 * 32768 * 2 bytes = 536 MB，而非 N68 中估算的 512 MB。

## Corrected Claim

在 Tensor Parallelism 下，每层 All-Reduce 通信的数据量公式为 2 * hidden_dim * seq_len * batch_size * dtype_size，对于 Qwen3-27B (hidden=4096, seq=32768, batch=1, FP16)，每层通信量为 2 * 4096 * 32768 * 2 bytes = 536 MB，而非 N68 中估算的 512 MB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * hidden_dim * seq_len * batch_size * dtype_size 符合 Tensor Parallelism 中 All-Reduce 通信量（Ring All-Reduce 近似为 2 * size）的标准定义；数值计算 2 * 4096 * 32768 * 1 * 2 = 536,870,912 bytes = 536 MB，计算准确且量级合理。
