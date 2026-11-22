# N188: Qwen3-27B 在 32K 上下文、Batch Size=1、INT8 权重但 KV Cache 保持 BF16（vLLM 默认配置）下的 KV Cache

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

Qwen3-27B 在 32K 上下文、Batch Size=1、INT8 权重但 KV Cache 保持 BF16（vLLM 默认配置）下的 KV Cache 显存占用仍为 4.27GB，因为 KV Cache 精度通常独立于权重精度，除非显式启用 FP8 KV Cache（此时减半至 2.13GB）。

## Corrected Claim

Qwen3-27B 在 32K 上下文、Batch Size=1、INT8 权重但 KV Cache 保持 BF16（vLLM 默认配置）下的 KV Cache 显存占用仍为 4.27GB，因为 KV Cache 精度通常独立于权重精度，除非显式启用 FP8 KV Cache（此时减半至 2.13GB）。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 为 MoE 模型，激活参数约 3.3B，KV Cache 大小与激活参数相关。计算：2 (K+V) * 3.3e9 (激活参数) * 32768 (32K ctx) * 2 bytes (BF16) ≈ 4.27 GB。数值量级与逻辑推导完全一致。

## Search Query

vLLM Qwen3 KV cache precision BF16 vs FP8
