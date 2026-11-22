# N468: AWQ 算法中保留 1% 显著权重为 FP16 的机制对 MMLU 退化率的抑制效果量化：在 27B 规模下，相比全 INT4 量化，混合精度（1% FP16 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N193, N194, N195

## Claim

AWQ 算法中保留 1% 显著权重为 FP16 的机制对 MMLU 退化率的抑制效果量化：在 27B 规模下，相比全 INT4 量化，混合精度（1% FP16 + 99% INT4）带来的 MMLU 提升幅度约为 0.3-0.5 个百分点，该数值需通过对比 Qwen3-27B-AWQ-Int4 与 Qwen3-27B-Int4-GPTQ 的 MMLU 分数差值来验证

## Corrected Claim

AWQ 算法中保留少量显著权重为 FP16 的机制通常能抑制 MMLU 退化率，具体提升幅度（如 0.3-0.5 个百分点）需通过对比特定模型（如 Qwen3-27B）的 AWQ 与 GPTQ 量化版本的 MMLU 分数差值来验证，不同模型和实验设置下数值可能有所差异。

## Evidence

[质询]该陈述包含具体的经验数值（0.3-0.5个百分点）和特定的模型对比（Qwen3-27B），属于经验事实而非第一性原理可推导内容。且Qwen3-27B-AWQ-Int4与Qwen3-27B-Int4-GPTQ的MMLU分数差值受具体量化实现、校准数据集及评测协议影响极大，不同来源或实验设置下结果可能显著不同，无法仅凭逻辑自洽确定具体数值区间。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该数值为特定模型的具体实验结果，非通用理论推导）

## Search Query

AWQ mixed precision FP16 weights MMLU improvement 27B model
