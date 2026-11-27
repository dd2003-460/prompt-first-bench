# N69: 使用 NCCL 进行 AllReduce 操作时，通信延迟 T_comm 近似公式为 (2 * N_layers * hidden_size * dtype_s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

使用 NCCL 进行 AllReduce 操作时，通信延迟 T_comm 近似公式为 (2 * N_layers * hidden_size * dtype_size) / (0.8 * PCIe_Bandwidth)，其中 0.8 为协议开销系数，需代入 N44 的带宽值计算具体毫秒数

## Corrected Claim

使用 NCCL 进行 AllReduce 操作时，通信延迟 T_comm 近似公式为 (2 * N_layers * hidden_size * dtype_size) / (0.8 * PCIe_Bandwidth)，其中 0.8 为协议开销系数，需代入 N44 的带宽值计算具体毫秒数

## Evidence

先验知识/题面给定，逻辑校验通过
