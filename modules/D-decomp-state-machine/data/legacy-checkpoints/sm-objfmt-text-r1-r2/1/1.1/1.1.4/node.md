# N28: 在 32K 上下文长度下，Qwen3-27B 单请求 KV Cache 的理论峰值显存占用计算结果为 64 * 8 * 128 * 32768 * 2 byte

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

在 32K 上下文长度下，Qwen3-27B 单请求 KV Cache 的理论峰值显存占用计算结果为 64 * 8 * 128 * 32768 * 2 bytes * 2 (K&V) = 8.59 GB

## Corrected Claim

在 32K 上下文长度下，Qwen3-27B 单请求 KV Cache 的理论峰值显存占用计算结果为 64 * 8 * 128 * 32768 * 2 bytes * 2 (K&V) = 8.59 GB

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（GQA 8 KV heads, head_dim 128, 64 layers）符合主流大模型设计，计算公式 64*8*128*32768*2*2 数值正确（约 8.59GB），量级合理。
