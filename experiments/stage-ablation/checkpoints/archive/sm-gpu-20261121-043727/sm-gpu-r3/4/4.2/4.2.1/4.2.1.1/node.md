# N168: Prefill 阶段计算量分解项 1：线性层 (Linear Layers) FLOPs。公式 = 2 * P * L_linear_params。Qwen3-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

Prefill 阶段计算量分解项 1：线性层 (Linear Layers) FLOPs。公式 = 2 * P * L_linear_params。Qwen3-27B 中线性层参数量约占总参数 90% (剩余为 Attention 投影和 Norm)，即 L_linear ≈ 24.5e9。在 P=32K 时，FLOPs_linear ≈ 2 * 32768 * 24.5e9 ≈ 1.60 PFLOPs

## Corrected Claim

Prefill 阶段计算量分解项 1：线性层 (Linear Layers) FLOPs。公式 = 2 * P * L_linear_params。Qwen3-27B 中线性层参数量约占总参数 90% (剩余为 Attention 投影和 Norm)，即 L_linear ≈ 24.5e9。在 P=32K 时，FLOPs_linear ≈ 2 * 32768 * 24.5e9 ≈ 1.60 PFLOPs

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 总参数量约 27B，线性层占比 90% 即 24.5B 符合常识；FLOPs 计算公式 2*P*L 正确；数值计算 2 * 32768 * 24.5e9 ≈ 1.60e15 (1.60 PFLOPs) 准确无误。
