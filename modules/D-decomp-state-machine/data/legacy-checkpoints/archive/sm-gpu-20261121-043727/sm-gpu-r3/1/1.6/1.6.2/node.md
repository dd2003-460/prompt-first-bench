# N55: 2x RTX 4090 通过 PCIe 4.0 x16 连接时，在 Tensor Parallelism 中 AllReduce 通信时间占比计算公式为：T_c

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N11

## Claim

2x RTX 4090 通过 PCIe 4.0 x16 连接时，在 Tensor Parallelism 中 AllReduce 通信时间占比计算公式为：T_comm = (M * L * 2) / (32GB/s * T_latency)，其中 M=32K, L=27B, T_latency 为 PCIe 传输延迟 (约 10-20μs)

## Corrected Claim

2x RTX 4090 通过 PCIe 4.0 x16 连接时，Tensor Parallelism 中 AllReduce 通信时间 T_comm 近似为 (2 * M * L * 2) / (32GB/s) + 2 * T_latency（Ring AllReduce 模型），通信时间占比为 T_comm / (T_comp + T_comm)。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1负责修正理论公式的错误（定性/逻辑层面），子节点2基于修正后的逻辑进行具体场景的量化计算（定量/应用层面）。两者逻辑递进，无重复或矛盾，且共同覆盖了父节点中关于公式定义和实际通信占比的核心问题。）
