# N194: 单次 AllReduce 操作的通信延迟 T_comm 由传输时间 T_transfer 和固定启动延迟 T_launch 组成：T_comm = (V_syn

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

单次 AllReduce 操作的通信延迟 T_comm 由传输时间 T_transfer 和固定启动延迟 T_launch 组成：T_comm = (V_sync / Effective_BW) + T_launch；其中 T_launch 在 PCIe P2P 场景下通常约为 5-10 μs，需结合 N118 的带宽和 N119 的数据量计算每层总延迟，进而推导对整体吞吐的影响系数 k_bandwidth = T_compute / (T_compute + T_comm)。

## Corrected Claim

单次 AllReduce 操作的通信延迟 T_comm 由传输时间 T_transfer 和固定启动延迟 T_launch 组成：T_comm = (V_sync / Effective_BW) + T_launch；其中 T_launch 在 PCIe P2P 场景下通常约为 5-10 μs，需结合 N118 的带宽和 N119 的数据量计算每层总延迟，进而推导对整体吞吐的影响系数 k_bandwidth = T_compute / (T_compute + T_comm)。

## Evidence

先验知识/题面给定，逻辑校验通过：通信延迟模型符合基本物理直觉，PCIe P2P启动延迟量级（5-10μs）符合工程常识，公式推导自洽。
