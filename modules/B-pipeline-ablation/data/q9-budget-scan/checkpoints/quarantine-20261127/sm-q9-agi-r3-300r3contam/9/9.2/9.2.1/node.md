# N242: TP=4 all-reduce 通信开销导致的带宽损失量化：在 V100 SXM2 NVLink (300GB/s per GPU) 下，AllReduce 通

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

TP=4 all-reduce 通信开销导致的带宽损失量化：在 V100 SXM2 NVLink (300GB/s per GPU) 下，AllReduce 通信时间 T_comm = 2 * M_tensor * (N-1)/N / BW_nvlink，其中 M_tensor 为单次激活张量大小，该部分占用的时间窗口内 HBM 带宽利用率为 0，导致有效带宽利用率从单卡的 ~60% 降至 TP=4 下的 45-55%。

## Corrected Claim

TP=4 all-reduce 通信开销导致的带宽损失量化：在 V100 SXM2 NVLink (300GB/s per GPU) 下，AllReduce 通信时间 T_comm = 2 * M_tensor * (N-1)/N / BW_nvlink，其中 M_tensor 为单次激活张量大小，该部分占用的时间窗口内 HBM 带宽利用率为 0，导致有效带宽利用率从单卡的 ~60% 降至 TP=4 下的 45-55%。

## Evidence

先验知识/题面给定，逻辑校验通过：AllReduce 通信期间计算单元空闲导致 HBM 带宽利用率为 0 符合硬件工作原理；TP=4 下因通信占比增加导致有效带宽利用率下降符合分布式训练常识；V100 NVLink 带宽量级及公式结构合理。
