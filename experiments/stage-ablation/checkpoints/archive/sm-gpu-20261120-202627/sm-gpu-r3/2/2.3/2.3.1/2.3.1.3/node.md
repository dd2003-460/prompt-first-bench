# N221: GPTQ 量化中 group_size 从 64 增加到 128 对困惑度降低的边际收益量化：需对比 group_size=64 与 group_size=12

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N55

## Claim

GPTQ 量化中 group_size 从 64 增加到 128 对困惑度降低的边际收益量化：需对比 group_size=64 与 group_size=128 两种配置下的困惑度差值（例如：group_size=64 时 PPL 增加 1.5%，group_size=128 时 PPL 增加 0.8%），以验证父节点中‘group_size=128 优于 64’的量化依据

## Corrected Claim

GPTQ 量化中，增大 group_size（如从 64 增加到 128）通常能降低量化误差，从而减少困惑度（PPL）的增加幅度，但具体降低的百分比取决于模型和数据集，需通过实验对比验证。

## Evidence

[质询]该陈述包含具体的经验数值（PPL增加1.5% vs 0.8%），属于硬件/模型性能的经验事实，无法从第一性原理推导，且检索无可用来源支持具体数值，存在数值不准确或特定模型依赖的风险。 | 经验事实，逻辑自洽（group_size增大通常降低量化误差从而降低PPL）但缺来源支持具体数值，故降级。

## Search Query

GPTQ group_size 64 vs 128 perplexity difference LLM quantization sensitivity analysis
