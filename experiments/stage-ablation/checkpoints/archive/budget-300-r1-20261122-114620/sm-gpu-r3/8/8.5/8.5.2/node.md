# N375: Qwen3-27B 在 W4A16 量化下，MMLU 准确率相比 BF16 的下降幅度通常 < 1 个百分点 (相对 < 1.5%)，需通过 LMSYS Cha

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N131

## Claim

Qwen3-27B 在 W4A16 量化下，MMLU 准确率相比 BF16 的下降幅度通常 < 1 个百分点 (相对 < 1.5%)，需通过 LMSYS Chatbot Arena 或 OpenCompass 基准测试核验 [待核验]

## Corrected Claim

Qwen3-27B 在 W4A16 量化下，MMLU 准确率相比 BF16 通常会有轻微下降，具体幅度需通过 LMSYS Chatbot Arena 或 OpenCompass 等基准测试实测核验。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（< 1 个百分点）和特定的模型/量化配置（Qwen3-27B, W4A16），属于经验事实。在缺乏具体基准测试数据支持的情况下，无法确认该特定模型在特定量化下的性能下降是否严格小于 1 个百分点，不同数据集或评测协议下结果可能存在波动。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值阈值）

## Search Query

Qwen3-27B W4A16 MMLU accuracy drop
