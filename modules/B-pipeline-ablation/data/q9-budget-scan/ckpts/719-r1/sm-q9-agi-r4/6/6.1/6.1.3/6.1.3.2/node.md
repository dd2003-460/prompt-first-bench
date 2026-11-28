# N254: 注意力分数分布偏移度量化指标：定义为 Softmax(Q·K^T/sqrt(d)) 在 FP16 与 NVFP4 下的 KL 散度 ΔKL_Attention，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

注意力分数分布偏移度量化指标：定义为 Softmax(Q·K^T/sqrt(d)) 在 FP16 与 NVFP4 下的 KL 散度 ΔKL_Attention，该值直接反映量化导致的注意力权重重分配程度，是连接底层量化误差与上层任务性能损失的中间机制变量。

## Corrected Claim

注意力分数分布偏移度量化指标：定义为 Softmax(Q·K^T/sqrt(d)) 在 FP16 与 NVFP4 下的 KL 散度 ΔKL_Attention，该值直接反映量化导致的注意力权重重分配程度，是连接底层量化误差与上层任务性能损失的中间机制变量。

## Evidence

先验知识/题面给定，逻辑校验通过：KL散度是衡量概率分布差异的标准指标，Softmax输出即为注意力权重分布，用其KL散度量化FP16与NVFP4间的分布偏移在定义和逻辑上完全自洽，且作为连接底层量化误差与上层性能损失的中间变量符合因果推断逻辑。
