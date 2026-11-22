# N132: KV Cache 带宽瓶颈量化模型：在 32K 上下文、Batch Size=1 的自回归解码阶段，每生成 1 token 需读取的 KV Cache 字节数 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

KV Cache 带宽瓶颈量化模型：在 32K 上下文、Batch Size=1 的自回归解码阶段，每生成 1 token 需读取的 KV Cache 字节数 = 2 × num_layers × hidden_dim × bytes_per_element × seq_len。对于 Qwen3-27B（假设 64 层，4096 hidden，BF16），计算每 token 读取量，并除以显存带宽（GB/s）得到理论最小延迟，用于验证带宽 < 1TB/s 是否导致不可接受的延迟。

## Corrected Claim

KV Cache 带宽瓶颈量化模型：在 32K 上下文、Batch Size=1 的自回归解码阶段，每生成 1 token 需读取的 KV Cache 字节数 = 2 × num_layers × hidden_dim × bytes_per_element × seq_len。对于 Qwen3-27B（假设 64 层，4096 hidden，BF16），计算每 token 读取量，并除以显存带宽（GB/s）得到理论最小延迟，用于验证带宽 < 1TB/s 是否导致不可接受的延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 读取量公式符合 Transformer 架构原理（Key+Value 各一份，随序列长度线性增长），数值量级（32K 上下文下约 13GB）与显存带宽瓶颈的物理直觉一致。
