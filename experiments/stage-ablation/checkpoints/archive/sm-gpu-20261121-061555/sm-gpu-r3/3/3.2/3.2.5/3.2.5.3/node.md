# N247: NVFP4 量化对 Qwen3-27B 代码生成能力（HumanEval Pass@1）的具体影响数值，若 PPL 损失接近 5% 上限，需评估其在代码任务上的

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83

## Claim

NVFP4 量化对 Qwen3-27B 代码生成能力（HumanEval Pass@1）的具体影响数值，若 PPL 损失接近 5% 上限，需评估其在代码任务上的实际准确率下降是否超过 2% 阈值，以判断 NVFP4 是否适用于代码密集型工作负载。

## Corrected Claim

NVFP4 量化对 Qwen3-27B 代码生成能力（HumanEval Pass@1）的具体影响数值需通过实验评估。若 PPL 损失接近 5% 上限，应评估其在代码任务上的实际准确率下降是否超过 2% 阈值，以判断 NVFP4 是否适用于代码密集型工作负载。

## Evidence

[质询]该陈述包含具体的经验性阈值（PPL损失5%、准确率下降2%）和特定模型（Qwen3-27B）在特定量化格式（NVFP4）下的性能表现，属于经验事实。由于缺乏外部来源支持，无法验证这些具体数值阈值的合理性或该特定组合的实际表现，存在将假设性评估标准误认为既定事实的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

NVFP4 quantization code generation accuracy HumanEval pass@1 drop Qwen
