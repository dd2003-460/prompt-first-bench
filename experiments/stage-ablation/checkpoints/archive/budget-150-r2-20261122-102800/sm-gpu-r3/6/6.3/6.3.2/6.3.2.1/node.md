# N348: 2× RTX 4090 (TP=2) 在 batch_size=1, seq_len=32768 下，Decode 阶段每步 AllReduce 通信量 = 2

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N138

## Claim

2× RTX 4090 (TP=2) 在 batch_size=1, seq_len=32768 下，Decode 阶段每步 AllReduce 通信量 = 2 × seq_len × hidden_size × batch_size × bytes_per_elem = 2 × 32768 × 4096 × 1 × 2 bytes (BF16) = 536,870,912 bytes ≈ 512 MB

## Corrected Claim

2× RTX 4090 (TP=2) 在 batch_size=1, seq_len=32768 下，Decode 阶段每步 AllReduce 通信量 = 2 × seq_len × hidden_size × batch_size × bytes_per_elem = 2 × 32768 × 4096 × 1 × 2 bytes (BF16) = 536,870,912 bytes ≈ 512 MB

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 32768 * 4096 * 1 * 2 = 536,870,912 bytes，换算为 512 MB 正确，符合 BF16 精度下 AllReduce 通信量的基本定义。
