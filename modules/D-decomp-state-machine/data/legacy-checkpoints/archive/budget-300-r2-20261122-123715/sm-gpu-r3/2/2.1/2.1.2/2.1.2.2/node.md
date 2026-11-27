# N199: Qwen3-27B INT8 (AWQ/GPTQ) 量化模型在 HumanEval 上的 Pass@1 准确率为 65.0%，在 MBPP 上的 Pass@1 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N54

## Claim

Qwen3-27B INT8 (AWQ/GPTQ) 量化模型在 HumanEval 上的 Pass@1 准确率为 65.0%，在 MBPP 上的 Pass@1 准确率为 69.0%；相对于 BF16 基线，HumanEval 下降幅度为 3.0% (68.0% - 65.0%)，MBPP 下降幅度为 3.0% (72.0% - 69.0%)。

## Corrected Claim

Qwen3-27B INT8 (AWQ/GPTQ) 量化模型在 HumanEval 和 MBPP 上的 Pass@1 准确率相较于 BF16 基线存在约 3% 的性能下降，具体数值需参考官方技术报告或基准测试数据。

## Evidence

[质询]具体数值（65.0%, 69.0%等）属于特定模型版本在特定量化方案下的经验性能指标，不同量化实现（AWQ vs GPTQ）、校准数据集及评测协议可能导致结果波动，且缺乏来源直接证实该精确数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B INT8 AWQ quantization HumanEval Pass@1 score degradation
