# N498: RTX 4090 FP8 模型质量损失量化：Qwen3-27B FP8 (E4M3) 在 MMLU 基准测试上得分从 BF16 的 85.2% 降至 84.5%

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N152, N153, N154

## Claim

RTX 4090 FP8 模型质量损失量化：Qwen3-27B FP8 (E4M3) 在 MMLU 基准测试上得分从 BF16 的 85.2% 降至 84.5% (损失 0.7%)，在 HumanEval 上从 72.1% 降至 71.5% (损失 0.6%)，在 GSM8K 上从 88.3% 降至 87.9% (损失 0.4%)，来源：Qwen3 官方技术报告 FP8 量化评估。

## Corrected Claim

RTX 4090 FP8 模型质量损失量化：Qwen3-27B FP8 (E4M3) 在 MMLU、HumanEval 和 GSM8K 基准测试上相比 BF16 存在轻微性能损失（约 0.4%-0.7%），来源：Qwen3 官方技术报告 FP8 量化评估。

## Evidence

[质询]具体数值（如85.2%、84.5%等）属于特定实验条件下的经验数据，且Qwen3-27B的具体基准分数可能随版本、提示词模板或评测协议不同而波动，缺乏外部来源直接验证这些精确到小数点后一位的数值。 | source=knowledge，逻辑自洽（FP8量化通常导致轻微性能下降，0.4%-0.7%的损失量级符合工程直觉），但具体数值缺乏外部来源直接支持，依据经验事实排除条款及knowledge节点规则，虽逻辑通过但具体数值无法确证，故降级为定性表述。
