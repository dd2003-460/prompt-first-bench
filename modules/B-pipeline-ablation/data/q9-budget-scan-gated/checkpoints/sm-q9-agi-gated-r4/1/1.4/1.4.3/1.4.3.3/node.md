# N53: 计算 N28 中 TP=4 AllReduce 延迟公式的隐含假设：公式 T_comm ≈ 2 * n * 4096 * 2 bytes / 300 GB/s 

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27, N28, N29

## Claim

计算 N28 中 TP=4 AllReduce 延迟公式的隐含假设：公式 T_comm ≈ 2 * n * 4096 * 2 bytes / 300 GB/s 假设了全双工零开销传输，实际 NVLink 存在协议头开销和 PCIe 桥接延迟（若 V100 间非直连 NVLink 而是经 PCIe 交换，带宽降为 16GB/s），需根据服务器实际拓扑（SXM2 模组是否配备 NVSwitch）确定有效带宽 B_eff，重新计算 n=200k 时的真实 T_comm。

## Corrected Claim

计算 N28 中 TP=4 AllReduce 延迟公式的隐含假设：公式 T_comm ≈ 2 * n * 4096 * 2 bytes / B_nominal 假设了全双工零开销传输。实际 NVLink 或 PCIe 链路存在协议头开销和桥接延迟，有效带宽 B_eff 通常低于标称值（例如 PCIe 3.0 x16 双向约 16GB/s，NVLink 视代际而定）。需根据服务器实际拓扑确定 B_eff，重新计算 n=200k 时的真实 T_comm。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于物理拓扑识别与带宽参数确定（定性/诊断），子节点2基于确定的参数进行具体的延迟计算与对比（定量/验证）。两者逻辑递进，无重叠或矛盾，且共同覆盖了父节点要求的‘确定拓扑’和‘重新计算延迟’两个核心任务。）

## Search Query

Tesla V100 SXM2 NVLink bandwidth per card effective throughput AllReduce latency
