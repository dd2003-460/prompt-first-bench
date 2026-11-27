# N127: 在代码生成任务（HumanEval/MBPP）上，Qwen3-27B 模型从 BF16 量化至 INT8 (AWQ/GPTQ) 的 pass@1 准确率下降幅度

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

在代码生成任务（HumanEval/MBPP）上，Qwen3-27B 模型从 BF16 量化至 INT8 (AWQ/GPTQ) 的 pass@1 准确率下降幅度为 1.5% - 3.0%，需根据具体模型版本核实基准测试数据。

## Corrected Claim

在代码生成任务（HumanEval/MBPP）上，Qwen3-27B 模型从 BF16 量化至 INT8 (AWQ/GPTQ) 通常会导致 pass@1 准确率出现一定程度的下降，具体幅度需根据实际基准测试数据核实。

## Evidence

[质询]具体数值范围（1.5%-3.0%）属于经验事实，缺乏直接来源支持，且不同量化算法（AWQ vs GPTQ）及具体模型版本（Qwen3-27B 是否为官方发布的确切型号）可能导致差异，无法仅凭逻辑推导确定精确区间。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B INT8 AWQ GPTQ HumanEval pass@1 accuracy drop
