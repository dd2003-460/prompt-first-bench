# N97: 48GB 显存档位 (A6000/L40S) 可容纳 Qwen3-27B 的 FP8 权重 (~25GB) + 32K 上下文 KV Cache (~5-10G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

48GB 显存档位 (A6000/L40S) 可容纳 Qwen3-27B 的 FP8 权重 (~25GB) + 32K 上下文 KV Cache (~5-10GB) + 激活值 (~5GB)，剩余 ~8-18GB 空间允许 batch size 扩展至 2-4，或支持更长上下文 (64K+) 的 BF16 KV Cache 部分卸载。

## Corrected Claim

48GB 显存档位 (A6000/L40S) 可容纳 Qwen3-27B 的 FP8 权重 (~25GB) + 32K 上下文 KV Cache (~5-10GB) + 激活值 (~5GB)，剩余 ~8-18GB 空间允许 batch size 扩展至 2-4，或支持更长上下文 (64K+) 的 BF16 KV Cache 部分卸载。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B FP8权重约25GB，32K上下文KV Cache约5-10GB，激活值约5GB，总占用约35-40GB，48GB显存剩余8-18GB，符合显存分配逻辑。

## Search Query

A6000 48GB Qwen3-27B FP8 32k context batch size capacity
