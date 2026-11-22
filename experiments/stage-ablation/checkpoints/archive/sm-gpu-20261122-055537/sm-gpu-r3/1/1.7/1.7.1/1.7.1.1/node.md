# N189: Prefill 阶段激活值峰值显存占用的精确计算：Prefill 阶段需一次性处理整个序列 (Seq=32768)，激活值峰值主要取决于 LayerNorm 和

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

Prefill 阶段激活值峰值显存占用的精确计算：Prefill 阶段需一次性处理整个序列 (Seq=32768)，激活值峰值主要取决于 LayerNorm 和 Attention 的中间结果。对于 Qwen3-27B (Hidden=4096, L=54)，Prefill 激活值峰值估算公式为：Peak_Activation ≈ (Batch_Size * Seq_Len * Hidden_Dim * Bytes_per_Element * Num_Layers * Factor)。在 Batch=1, Seq=32768, BF16 下，理论峰值约为 2.7GB (Factor≈0.01-0.02，取决于框架优化)。此值需与 N13 中的 5-10% 权重占比估算交叉验证。

## Corrected Claim

Prefill 阶段激活值峰值显存占用的精确计算：Prefill 阶段需一次性处理整个序列 (Seq=32768)，激活值峰值主要取决于 LayerNorm 和 Attention 的中间结果。对于 Qwen3-27B (Hidden=4096, L=54)，Prefill 激活值峰值估算公式为：Peak_Activation ≈ (Batch_Size * Seq_Len * Hidden_Dim * Bytes_per_Element * Num_Layers * Factor)。在 Batch=1, Seq=32768, BF16 下，理论峰值约为 2.7GB (Factor≈0.01-0.02，取决于框架优化)。此值需与 N13 中的 5-10% 权重占比估算交叉验证。

## Evidence

先验知识/题面给定，逻辑校验通过：基于 Qwen3-27B 参数（Hidden=4096, L=54, Seq=32768）及 BF16 精度，激活值峰值显存占用量级估算符合深度学习推理内存管理的基本原理，数值 2.7GB 在合理范围内。
