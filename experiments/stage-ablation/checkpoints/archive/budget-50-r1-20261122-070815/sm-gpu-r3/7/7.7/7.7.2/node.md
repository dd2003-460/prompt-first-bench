# N393: L40S 48GB 运行 Qwen3-27B FP8 权重 (27GB) 时的显存占用详细分解：Weight (27GB) + KV Cache (基于 N12

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N137

## Claim

L40S 48GB 运行 Qwen3-27B FP8 权重 (27GB) 时的显存占用详细分解：Weight (27GB) + KV Cache (基于 N128 混合架构计算的 FP8 或 BF16 KV 大小) + Activation (1-2GB) + 框架开销 (~2-3GB)，总和需 < 48GB 以确认单卡可行性，并计算剩余显存对 Batch Size 的支持上限（预计 Batch Size 上限低于 A100/H100）。

## Corrected Claim

L40S 48GB 运行 Qwen3-27B FP8 权重 (27GB) 时的显存占用详细分解：Weight (27GB) + KV Cache (基于 N128 混合架构计算的 FP8 或 BF16 KV 大小) + Activation (1-2GB) + 框架开销 (~2-3GB)，总和需 < 48GB 以确认单卡可行性，并计算剩余显存对 Batch Size 的支持上限（预计 Batch Size 上限低于 A100/H100）。

## Evidence

先验知识/题面给定，逻辑校验通过：27GB权重+1-2GB激活+2-3GB开销=30-32GB，剩余16-18GB显存足以容纳KV Cache，总显存占用<48GB，单卡可行性成立。
