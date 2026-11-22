# N203: W4量化对Qwen3-27B质量损失的具体量化：基于MMLU基准，W4-A16（权重4bit，激活16bit）量化通常导致准确率下降1.5%-3.5%（从BF1

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N59

## Claim

W4量化对Qwen3-27B质量损失的具体量化：基于MMLU基准，W4-A16（权重4bit，激活16bit）量化通常导致准确率下降1.5%-3.5%（从BF16基线85%降至81.5%-83.5%）。若业务容忍度阈值为2%，则需选用AWQ（Activation-aware Weight Quantization）等高级量化算法，其额外计算开销会使Prefill阶段延迟增加约5%-8%，但Decode阶段吞吐保持不变。

## Corrected Claim

W4量化对Qwen3-27B质量损失的具体量化：基于MMLU基准，W4-A16量化通常导致准确率出现一定程度的下降（具体幅度取决于量化算法与实现，通常在1%-5%区间）。若业务容忍度阈值较低，需选用AWQ等高级量化算法，其可能引入额外的计算开销，导致Prefill阶段延迟增加，而Decode阶段吞吐受影响较小。

## Evidence

[质询]具体数值（1.5%-3.5%准确率下降、5%-8% Prefill延迟增加）属于特定模型（Qwen3-27B）在特定基准（MMLU）下的经验测量结果，无法从第一性原理推导，且不同量化实现（如GPTQ vs AWQ）及硬件环境会导致显著差异，缺乏通用性。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但具体数值为经验参数，非稳定理论常数，且无外部来源验证具体量级）
