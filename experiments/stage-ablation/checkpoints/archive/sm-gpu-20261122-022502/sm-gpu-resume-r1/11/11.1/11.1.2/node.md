# N336: Qwen3-27B FP8 (E4M3) 量化后在 WikiText-2 数据集上的 Perplexity (PPL) 值为 4.53-4.54，绝对增加 0.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N121

## Claim

Qwen3-27B FP8 (E4M3) 量化后在 WikiText-2 数据集上的 Perplexity (PPL) 值为 4.53-4.54，绝对增加 0.03-0.04，相对增加 0.3%-0.8%，该数值需通过 PyTorch FP8 推理引擎实测验证，以确认其'近无损'特性。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 量化后，其 WikiText-2 Perplexity 通常接近原始精度模型，具体数值（如 4.53-4.54）需通过 PyTorch FP8 推理引擎实测验证以确认'近无损'特性。

## Evidence

[质询]该陈述包含具体的经验性数值（PPL 4.53-4.54 及增量），属于硬件/模型性能指标，无法从第一性原理推导，且检索无可用来源支持，存在数值不准确或特定配置下不成立的风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据验证具体 PPL 数值）

## Search Query

Qwen3-27B FP8 E4M3 WikiText-2 perplexity
