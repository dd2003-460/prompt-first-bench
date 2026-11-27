# N15: BF16精度作为基准，Qwen3-27B在MMLU、GSM8K、HumanEval基准上的得分分别为85.2%、82.1%、68.5%，作为质量损失的参考零点，

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

BF16精度作为基准，Qwen3-27B在MMLU、GSM8K、HumanEval基准上的得分分别为85.2%、82.1%、68.5%，作为质量损失的参考零点，任何量化精度的损失均以此为基准计算相对下降百分比。

## Corrected Claim

BF16精度作为基准，Qwen3-27B在MMLU、GSM8K、HumanEval基准上的得分约为85%、82%、68%左右，作为质量损失的参考零点，任何量化精度的损失均以此为基准计算相对下降百分比。

## Evidence

[质询]具体数值（85.2%, 82.1%, 68.5%）属于特定模型版本在特定基准上的经验性测试结果，不同评测集、提示词或解码策略可能导致数值波动，且Qwen3-27B的具体官方发布数据需以官方技术报告为准，此处数值可能为近似值或特定实验结果，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体基准分数属于经验数据，无法仅凭第一性原理推导，故降级）

## Search Query

Qwen3 27B BF16 MMLU GSM8K HumanEval benchmark scores
