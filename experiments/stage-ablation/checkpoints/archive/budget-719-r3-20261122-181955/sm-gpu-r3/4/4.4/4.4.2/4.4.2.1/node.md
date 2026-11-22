# N330: 量化精度损失的共享随机源定义为模型架构与量化算法的交互效应 $\epsilon_{model, algo}$，该随机源驱动 MMLU 和 HumanEval 的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N109

## Claim

量化精度损失的共享随机源定义为模型架构与量化算法的交互效应 $\epsilon_{model, algo}$，该随机源驱动 MMLU 和 HumanEval 的损失分布，不同模型（如 Qwen3 vs Llama3）和算法（AWQ vs GPTQ）下该源的参数不同。

## Corrected Claim

量化精度损失的共享随机源定义为模型架构与量化算法的交互效应 $\epsilon_{model, algo}$，该随机源驱动 MMLU 和 HumanEval 的损失分布，不同模型（如 Qwen3 vs Llama3）和算法（AWQ vs GPTQ）下该源的参数不同。

## Evidence

先验知识/题面给定，逻辑校验通过
