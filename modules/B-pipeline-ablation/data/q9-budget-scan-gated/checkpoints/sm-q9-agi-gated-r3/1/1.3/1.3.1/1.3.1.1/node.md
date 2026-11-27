# N43: TP=4 AllReduce通信量修正：在seq_len=4096、batch_size=8、hidden_dim=4096时，单次通信量为2 * 8 * 40

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

TP=4 AllReduce通信量修正：在seq_len=4096、batch_size=8、hidden_dim=4096时，单次通信量为2 * 8 * 4096 * 4096 * 2 bytes = 536.9MB，而非512MB；NVLink 300GB/s下耗时1.79ms，占decode步时间（~10ms）的17.9%，符合15-25%区间。

## Corrected Claim

TP=4 AllReduce通信量修正：在seq_len=4096、batch_size=8、hidden_dim=4096时，单次通信量为2 * 8 * 4096 * 4096 * 2 bytes = 536.9MB，而非512MB；NVLink 300GB/s下耗时1.79ms，占decode步时间（~10ms）的17.9%，符合15-25%区间。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 8 * 4096 * 4096 * 2 = 536,870,912 bytes ≈ 536.9 MB 正确；耗时 536.9MB / 300GB/s ≈ 1.79ms 正确；占比 1.79/10 = 17.9% 正确，符合逻辑与算术推导。

## Search Query

Tensor Parallelism AllReduce communication volume calculation
