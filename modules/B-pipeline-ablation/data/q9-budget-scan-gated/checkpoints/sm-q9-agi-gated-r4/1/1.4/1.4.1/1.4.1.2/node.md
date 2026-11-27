# N48: N25 中剩余 KV Cache 空间 11.8 GB 的计算逻辑正确（15.2 GB - 3.4 GB），但需考虑 NCCL 缓冲区（~0.5-1.0 GB）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

N25 中剩余 KV Cache 空间 11.8 GB 的计算逻辑正确（15.2 GB - 3.4 GB），但需考虑 NCCL 缓冲区（~0.5-1.0 GB）和 CUDA 上下文开销（~0.5 GB），实际可用 KV Cache 空间约为 10.3-10.8 GB，而非 11.8 GB。

## Corrected Claim

N25 中剩余 KV Cache 空间 11.8 GB 的计算逻辑正确（15.2 GB - 3.4 GB），但需考虑 NCCL 缓冲区（~0.5-1.0 GB）和 CUDA 上下文开销（~0.5 GB），实际可用 KV Cache 空间约为 10.3-10.8 GB，而非 11.8 GB。

## Evidence

[质询]NCCL 缓冲区和 CUDA 上下文开销的具体数值（0.5-1.0 GB 和 0.5 GB）属于经验估计，不同硬件配置和软件版本下可能有波动，但作为工程估算的量级是合理的。 | 先验知识/题面给定，逻辑校验通过：15.2 - 3.4 = 11.8 GB 计算正确；扣除典型的系统开销（NCCL+CUDA ~1.0-1.5 GB）后得到 10.3-10.8 GB 符合工程常识。
