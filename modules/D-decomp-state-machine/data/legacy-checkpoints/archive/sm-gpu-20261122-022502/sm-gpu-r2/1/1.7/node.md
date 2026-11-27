# N12: INT8量化质量损失：相对于BF16，INT8量化导致MMLU准确率下降~0.5-1.0% [待核验]，PPL上升~0.1-0.2 [待核验]，在可接受范围内（

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

INT8量化质量损失：相对于BF16，INT8量化导致MMLU准确率下降~0.5-1.0% [待核验]，PPL上升~0.1-0.2 [待核验]，在可接受范围内（<2%准确率下降）

## Corrected Claim

INT8量化通常导致MMLU准确率下降约0.5-1.0%，PPL上升约0.1-0.2，具体数值取决于量化算法、校准数据及模型架构，在多数主流LLM上处于可接受范围（<2%准确率下降）。

## Evidence

[质询]数值量级可能过于乐观或特定于特定模型/数据集：对于某些敏感模型或任务，INT8量化（尤其是非对称或无校准数据时）可能导致MMLU下降超过1%或PPL上升更多；此外，'~0.5-1.0%'和'~0.1-0.2'是经验性统计值，并非普适物理定律，不同量化方法（如GPTQ, SmoothQuant, AWQ）和模型架构（LLaMA, Mistral等）差异显著，缺乏具体上下文时该范围可能不具代表性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且属于硬件/算法经验参数，不适用第一性原理推导条款）

## Search Query

INT8 quantization LLM 27B MMLU accuracy drop perplexity increase
