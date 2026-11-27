# N394: Qwen3-27B INT8 (GPTQ) 量化在 MMLU 基准测试上的准确率下降幅度：相比 BF16 基线 (准确率约 80-85%)，GPTQ INT4/

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N125

## Claim

Qwen3-27B INT8 (GPTQ) 量化在 MMLU 基准测试上的准确率下降幅度：相比 BF16 基线 (准确率约 80-85%)，GPTQ INT4/INT8 量化通常导致准确率下降 1-3 个百分点，具体数值依赖于量化组大小 (group_size=128 vs 64)。

## Corrected Claim

Qwen3-27B INT8 (GPTQ) 量化在 MMLU 基准测试上的准确率通常会有轻微下降，具体幅度取决于量化组大小等超参数，但缺乏确切数值证据。

## Evidence

[质询]该陈述包含具体的经验性数值（MMLU基线80-85%，下降1-3个百分点），属于硬件/模型性能经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B GPTQ INT8 MMLU accuracy drop
