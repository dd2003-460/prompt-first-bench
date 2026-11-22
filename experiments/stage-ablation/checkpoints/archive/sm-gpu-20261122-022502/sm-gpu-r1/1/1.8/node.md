# N13: W4量化质量损失：相对于BF16，W4量化导致MMLU准确率下降~2-4% [待核验]，PPL上升~0.3-0.5 [待核验]，可能超出可接受范围（>2%准确率

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

W4量化质量损失：相对于BF16，W4量化导致MMLU准确率下降~2-4% [待核验]，PPL上升~0.3-0.5 [待核验]，可能超出可接受范围（>2%准确率下降）

## Corrected Claim

W4量化通常会导致MMLU准确率下降和PPL上升，具体幅度取决于量化方法和校准策略，一般认为可能超出2%准确率下降的可接受阈值。

## Evidence

[质询]数值范围（2-4% MMLU下降，0.3-0.5 PPL上升）属于经验事实，具体数值高度依赖于量化算法（如GPTQ, AWQ, SmoothQuant）、校准数据集大小及模型架构，缺乏具体上下文时，该范围可能偏乐观或偏悲观，且不同文献报道差异较大。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值范围）

## Search Query

W4 quantization LLM 27B MMLU accuracy drop perplexity increase
