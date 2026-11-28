# N254: Decode 阶段 TP=4 AllReduce 的单次通信量 Data_Size_decode = 1 * 1 * 4096 * 2 (BF16) = 8 K

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

Decode 阶段 TP=4 AllReduce 的单次通信量 Data_Size_decode = 1 * 1 * 4096 * 2 (BF16) = 8 KB/layer；64 层总计 512 KB/step；在 150 GB/s 带宽下，理论通信时间 T_comm_decode ≈ 512 KB / 150 GB/s ≈ 3.4 μs，远低于 V100 单 token 生成时间 (~20-30 ms)，因此 Decode 阶段通信开销占比 < 0.02%，可忽略不计。

## Corrected Claim

Decode 阶段 TP=4 AllReduce 的单次通信量 Data_Size_decode = 1 * 1 * 4096 * 2 (BF16) = 8 KB/layer；64 层总计 512 KB/step；在 150 GB/s 带宽下，理论通信时间 T_comm_decode ≈ 512 KB / 150 GB/s ≈ 3.4 μs，远低于 V100 单 token 生成时间 (~20-30 ms)，因此 Decode 阶段通信开销占比 < 0.02%，可忽略不计。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程（4096*2*64=512KB，512KB/150GB/s≈3.4μs）及量级对比（3.4μs vs 20ms）均符合物理直觉与数学逻辑。
