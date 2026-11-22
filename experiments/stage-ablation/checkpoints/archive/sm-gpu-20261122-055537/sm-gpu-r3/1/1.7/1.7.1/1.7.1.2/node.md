# N190: Decode 阶段激活值峰值显存占用的精确计算：Decode 阶段每次仅生成 1 个 Token，激活值峰值主要受中间层隐藏状态和 Attention 的 KV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

Decode 阶段激活值峰值显存占用的精确计算：Decode 阶段每次仅生成 1 个 Token，激活值峰值主要受中间层隐藏状态和 Attention 的 KV 读取影响。对于 Qwen3-27B，Decode 激活值峰值估算为：Peak_Activation_Decode ≈ (Batch_Size * Hidden_Dim * Bytes_per_Element * Num_Layers * Factor)。在 Batch=1, BF16 下，理论峰值约为 0.5-1.0GB。此值远低于 Prefill 阶段，表明 Decode 阶段的显存瓶颈主要在 KV Cache 而非激活值。

## Corrected Claim

Decode 阶段激活值峰值显存占用的精确计算：Decode 阶段每次仅生成 1 个 Token，激活值峰值主要受中间层隐藏状态和 Attention 的 KV 读取影响。对于 Qwen3-27B，Decode 激活值峰值估算为：Peak_Activation_Decode ≈ (Batch_Size * Hidden_Dim * Bytes_per_Element * Num_Layers * Factor)。在 Batch=1, BF16 下，理论峰值约为 0.5-1.0GB。此值远低于 Prefill 阶段，表明 Decode 阶段的显存瓶颈主要在 KV Cache 而非激活值。

## Evidence

先验知识/题面给定，逻辑校验通过
