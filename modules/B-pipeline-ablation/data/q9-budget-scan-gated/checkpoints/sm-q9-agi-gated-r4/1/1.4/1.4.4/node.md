# N28: TP=4 下 AllReduce 通信延迟（T_comm）与序列长度 n 成正比：T_comm ≈ 2 * n * 4096 * 2 bytes / 300 G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

TP=4 下 AllReduce 通信延迟（T_comm）与序列长度 n 成正比：T_comm ≈ 2 * n * 4096 * 2 bytes / 300 GB/s，当 n=200k 时 T_comm≈10.7 ms，占单步 decode 时间（~20 ms）的 53.5%，严重制约投机解码加速比

## Corrected Claim

TP=4 下 AllReduce 通信延迟（T_comm）与序列长度 n 成正比：T_comm ≈ 2 * n * 4096 * 2 bytes / 300 GB/s，当 n=200k 时 T_comm≈10.7 ms，占单步 decode 时间（~20 ms）的 53.5%，严重制约投机解码加速比

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2*200000*4096*2/300e9 ≈ 10.9ms，与10.7ms量级一致；占比 10.7/20 = 53.5% 正确；AllReduce 通信量与序列长度成正比的逻辑符合分布式推理常识。
