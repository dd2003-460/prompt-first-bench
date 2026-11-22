# N275: W4量化下Qwen3-27B的精度损失需量化：HumanEval Pass@1损失通常≥5-8%（基于其他W4模型经验），GSM8K损失通常≥3-5%；若损失超

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N117

## Claim

W4量化下Qwen3-27B的精度损失需量化：HumanEval Pass@1损失通常≥5-8%（基于其他W4模型经验），GSM8K损失通常≥3-5%；若损失超过业务阈值，W4方案不可行，需回退至INT8

## Corrected Claim

W4量化下Qwen3-27B的精度损失需实测量化：参考其他W4模型经验，HumanEval Pass@1损失可能在5-8%左右，GSM8K损失可能在3-5%左右；若实测损失超过业务阈值，W4方案不可行，需回退至INT8

## Evidence

[质询]将其他W4模型的通用经验值直接套用于Qwen3-27B属于过度泛化，不同模型架构和训练数据对量化的敏感度存在差异，具体损失幅度需实测验证，不能仅凭经验断定'通常≥5-8%'。 | 经验事实，逻辑自洽但缺来源支持；W4量化确实会导致精度损失，但具体数值范围因模型而异，无法从第一性原理严格推出特定百分比。

## Search Query

W4 quantization LLM accuracy loss HumanEval GSM8K benchmark
