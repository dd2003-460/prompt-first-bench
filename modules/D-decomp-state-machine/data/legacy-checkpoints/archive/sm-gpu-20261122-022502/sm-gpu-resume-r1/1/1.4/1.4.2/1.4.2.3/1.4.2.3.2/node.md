# N513: RTX 5090 单卡运行 Qwen3-27B FP8 权重（27GB）+ 32K 上下文 INT4 KV Cache（3.145GB）的总显存占用为 30.1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N157

## Claim

RTX 5090 单卡运行 Qwen3-27B FP8 权重（27GB）+ 32K 上下文 INT4 KV Cache（3.145GB）的总显存占用为 30.145GB，剩余 1.855GB 用于激活值（Activations）和系统开销，处于安全阈值内（通常需保留 5-10% 显存给 CUDA Context 和临时缓冲）。

## Corrected Claim

RTX 5090 单卡运行 Qwen3-27B FP8 权重（27GB）+ 32K 上下文 INT4 KV Cache（3.145GB）的总显存占用为 30.145GB，剩余 1.855GB 用于激活值（Activations）和系统开销，处于安全阈值内（通常需保留 5-10% 显存给 CUDA Context 和临时缓冲）。

## Evidence

先验知识/题面给定，逻辑校验通过：27GB + 3.145GB = 30.145GB，总显存32GB，剩余1.855GB（约5.8%），符合CUDA上下文及激活值预留的安全阈值经验值。
