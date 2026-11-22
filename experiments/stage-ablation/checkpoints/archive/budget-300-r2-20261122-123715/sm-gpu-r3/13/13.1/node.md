# N380: 2x RTX 4090 (PCIe 4.0) Tensor Parallelism 下 Token 生成速度 (TPOT) 的通信开销公式为 T_comm_pe

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N119

## Claim

2x RTX 4090 (PCIe 4.0) Tensor Parallelism 下 Token 生成速度 (TPOT) 的通信开销公式为 T_comm_per_token = (num_layers * hidden_dim * dtype_size_bytes * 2) / PCIe_Bandwidth_GBps，其中 PCIe_Bandwidth_GBps 为 32 GB/s (x16)，需计算每 token 的额外延迟。

## Corrected Claim

2x RTX 4090 (PCIe 4.0) Tensor Parallelism 下 Token 生成速度 (TPOT) 的通信开销公式为 T_comm_per_token = (num_layers * hidden_dim * dtype_size_bytes * 2) / PCIe_Bandwidth_GBps，其中 PCIe_Bandwidth_GBps 为 32 GB/s (x16)，需计算每 token 的额外延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：Tensor Parallelism 中 All-Reduce 通信量约为 2 * num_layers * hidden_dim * dtype_size，PCIe 4.0 x16 带宽约 32 GB/s，公式量纲与数值量级合理。
