# N67: 在张量并行 (Tensor Parallelism) 中，每次 Attention 和 FFN 层都需要 All-Reduce 通信，通信量约为 2 * hid

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

在张量并行 (Tensor Parallelism) 中，每次 Attention 和 FFN 层都需要 All-Reduce 通信，通信量约为 2 * hidden_size * batch_size * seq_len * bytes，对于 Qwen3-27B (hidden_size=4096)，每 token 每层通信量约为 16 KB (BF16)，64 层总计约 1 MB/token，在 64 GB/s 带宽下引入约 15.6 us/token 的纯通信延迟。

## Corrected Claim

在张量并行 (Tensor Parallelism) 中，每次 Attention 和 FFN 层都需要 All-Reduce 通信，通信量约为 2 * hidden_size * batch_size * seq_len * bytes，对于 Qwen3-27B (hidden_size=4096)，每 token 每层通信量约为 16 KB (BF16)，64 层总计约 1 MB/token，在 64 GB/s 带宽下引入约 15.6 us/token 的纯通信延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：通信量计算 (2 * 4096 * 2 bytes = 16KB) 及延迟推导 (1MB / 64GB/s ≈ 15.6us) 均符合张量并行标准通信模式及物理量纲。
