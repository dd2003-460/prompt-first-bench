# N639: 2x 4090 TP=2 下，每层 Attention 和 FFN 输出需 All-Reduce，每次通信数据量为 2 * hidden_size * 2 by

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N197

## Claim

2x 4090 TP=2 下，每层 Attention 和 FFN 输出需 All-Reduce，每次通信数据量为 2 * hidden_size * 2 bytes (BF16 中间激活) = 2 * 4096 * 2 = 16 KB，共 64 层，每 token 总通信量 = 64 * 16 KB = 1 MB

## Corrected Claim

2x 4090 TP=2 下，每层 Attention 和 FFN 输出需 All-Reduce，每次通信数据量为 2 * hidden_size * 2 bytes (BF16 中间激活) = 2 * 4096 * 2 = 16 KB，共 64 层，每 token 总通信量 = 64 * 16 KB = 1 MB

## Evidence

先验知识/题面给定，逻辑校验通过：TP=2下Attention和FFN各需一次All-Reduce，每次通信量为2*4096*2=16KB，64层共128次通信，总通信量1MB，计算无误。
