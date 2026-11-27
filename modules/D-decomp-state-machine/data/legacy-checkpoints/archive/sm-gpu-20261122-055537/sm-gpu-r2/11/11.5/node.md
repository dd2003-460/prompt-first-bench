# N121: BF16精度下Qwen3-27B的Q_score为1.0（无量化损失），而INT4精度下Q_score通常在0.85-0.95之间（基于MMLU/HumanEv

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

BF16精度下Qwen3-27B的Q_score为1.0（无量化损失），而INT4精度下Q_score通常在0.85-0.95之间（基于MMLU/HumanEval基准测试的相对性能），需具体量化损失幅度以判断是否可接受。

## Corrected Claim

BF16精度下Qwen3-27B的Q_score为1.0（无量化损失）；INT4精度下Q_score通常低于1.0，具体数值（如0.85-0.95）需依据特定基准测试（如MMLU/HumanEval）的实际量化实验结果确定。

## Evidence

[质询]将特定模型（Qwen3-27B）在特定基准（MMLU/HumanEval）上的量化表现泛化为‘通常’范围，且缺乏具体量化实验数据支持该数值区间（0.85-0.95）的普适性，存在以偏概全风险。 | 先验知识/题面给定，逻辑校验通过：BF16作为训练精度通常无量化损失（Q_score=1.0）符合逻辑；INT4量化导致性能下降是已知现象，但具体数值区间（0.85-0.95）属于经验事实，虽逻辑自洽但缺乏来源直接支持，故降级。

## Search Query

Qwen3 27B INT4 vs BF16 benchmark accuracy drop
