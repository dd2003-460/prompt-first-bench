# N392: Qwen3-27B INT8量化版本的MMLU准确率Acc_INT8，需区分量化方法（如GPTQ vs SmoothQuant），并引用具体量化库（如AutoG

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N131

## Claim

Qwen3-27B INT8量化版本的MMLU准确率Acc_INT8，需区分量化方法（如GPTQ vs SmoothQuant），并引用具体量化库（如AutoGPTQ, GPTQModel）的release notes或社区评测数据，通常INT8在27B规模下MMLU下降幅度较小（<1%）。

## Corrected Claim

Qwen3-27B INT8量化版本的MMLU准确率通常较FP16/FP32基线有轻微下降，具体幅度取决于量化方法（如GPTQ vs SmoothQuant）及实现库，需参考具体评测数据。

## Evidence

[质询]该陈述包含具体的经验性数值断言（MMLU下降幅度<1%）和特定模型/量化方法的性能表现，属于硬件/模型规格类的经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B INT8 GPTQ MMLU accuracy drop
