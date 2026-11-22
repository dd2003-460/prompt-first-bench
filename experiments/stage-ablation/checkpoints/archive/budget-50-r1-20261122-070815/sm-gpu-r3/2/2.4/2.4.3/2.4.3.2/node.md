# N231: NVFP4 量化在 HumanEval 上的分数下降幅度 (Delta %) 约为 3-6 个百分点（即从 70-75% 降至 64-72%），代码生成对 to

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N67

## Claim

NVFP4 量化在 HumanEval 上的分数下降幅度 (Delta %) 约为 3-6 个百分点（即从 70-75% 降至 64-72%），代码生成对 token 概率分布的微小扰动极其敏感，4-bit 量化导致的 logit 偏移易引发语法错误或逻辑偏差

## Corrected Claim

NVFP4 量化在 HumanEval 等代码生成任务上通常会导致分数下降（幅度视具体模型和实现而定，常见在几个百分点范围内），这是因为代码生成对 token 概率分布的微小扰动极其敏感，4-bit 量化导致的 logit 偏移易引发语法错误或逻辑偏差。

## Evidence

[质询]具体数值区间（3-6个百分点）及基准分数（70-75%）属于特定实验条件下的经验数据，缺乏通用性，且不同模型/数据集版本下波动较大，易被质疑为以偏概全或数据过时。 | 先验知识/题面给定，逻辑校验通过：4-bit量化确实会引入logit偏移，对代码生成等对语法敏感的任务影响显著，量级符合一般量化误差规律，但具体数值缺乏来源直接支持。

## Search Query

NVFP4 quantization HumanEval performance drop code generation
