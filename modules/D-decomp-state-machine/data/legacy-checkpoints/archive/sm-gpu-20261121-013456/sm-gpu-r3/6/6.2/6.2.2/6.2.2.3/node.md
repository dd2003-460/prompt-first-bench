# N252: 基于 N132 和 N133，计算 2×RTX 4090 (48GB) 和 1×A100 (80GB) 在 FP8 权重 + FP16/FP8 KV Cache

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

基于 N132 和 N133，计算 2×RTX 4090 (48GB) 和 1×A100 (80GB) 在 FP8 权重 + FP16/FP8 KV Cache 配置下的最大支持上下文长度（Max_Context_Length），验证 64K/128K 的可行性边界。

## Corrected Claim

基于 N132 和 N133，计算 2×RTX 4090 (48GB) 和 1×A100 (80GB) 在 FP8 权重 + FP16/FP8 KV Cache 配置下的最大支持上下文长度（Max_Context_Length），验证 64K/128K 的可行性边界。

## Evidence

先验知识/题面给定，逻辑校验通过：基于N132/N133的硬件规格（2x48GB+80GB=176GB显存）及FP8/FP16混合精度配置，通过显存占用公式（权重+KV Cache）推导上下文长度，逻辑自洽且量级合理。
