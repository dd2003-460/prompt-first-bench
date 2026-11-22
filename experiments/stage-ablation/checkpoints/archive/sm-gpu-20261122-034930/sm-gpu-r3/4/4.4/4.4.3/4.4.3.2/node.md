# N334: W4 量化导致的质量损失：根据 AWQ 论文及社区实测，Qwen3-27B 在 W4A16 精度下，MMLU 准确率损失约为 2-4%（相对于 BF16），Pe

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N119

## Claim

W4 量化导致的质量损失：根据 AWQ 论文及社区实测，Qwen3-27B 在 W4A16 精度下，MMLU 准确率损失约为 2-4%（相对于 BF16），Perplexity 增加约 0.5-1.0%。此损失在通用对话任务中通常可接受，但在数学推理或代码生成任务中可能导致准确率下降 5-10%。

## Corrected Claim

W4 量化通常会导致模型质量轻微下降，在通用任务中损失较小，但在数学推理或代码生成等复杂任务中损失可能更为显著。

## Evidence

[质询]具体数值（MMLU损失2-4%、Perplexity增加0.5-1.0%、特定任务下降5-10%）缺乏直接来源支持，且不同量化实现（如AWQ vs GPTQ）及数据集版本可能导致数值波动，存在将特定实验结果泛化为普遍规律的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值量级）

## Search Query

Qwen3 27B AWQ W4A16 MMLU accuracy loss perplexity
