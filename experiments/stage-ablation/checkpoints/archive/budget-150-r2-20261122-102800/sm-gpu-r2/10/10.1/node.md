# N155: Normalized Throughput 的分母 max(tokens/s) 的基准值：基于 N18/N19/N20 的实测/估算峰值，max(tokens/

- **status**: degraded
- **level**: L3
- **source**: derived
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N51

## Claim

Normalized Throughput 的分母 max(tokens/s) 的基准值：基于 N18/N19/N20 的实测/估算峰值，max(tokens/s) = 57.4 (H100-80GB @ BF16, 3350/58.29)；若考虑 W4 量化下的峰值，max 可能升至 69.2 (RTX 4090 @ W4, 1008/14.57)。需明确 Normalization 是在同一精度下比较，还是跨精度归一化（跨精度归一化会扭曲质量权重，建议限定在同一精度工作点内归一化，或引入精度惩罚项）。

## Corrected Claim

Normalized Throughput 的分母 max(tokens/s) 应基于特定精度下的实测峰值确定。例如，在 BF16 精度下，H100-80GB 的峰值约为 57.4 tokens/s；在 W4 量化下，RTX 4090 的峰值可能升至 69.2 tokens/s。建议明确 Normalization 是在同一精度下比较，或引入精度惩罚项以避免跨精度归一化扭曲质量权重。

## Evidence

[质询]该陈述包含具体的硬件性能基准数值（如 H100 57.4 tokens/s, RTX 4090 69.2 tokens/s），属于经验事实。由于检索失败无外部来源支持，且这些具体数值高度依赖于特定的模型大小、序列长度、Batch Size 及推理框架版本，无法仅凭逻辑推导验证其准确性，存在数值偏差或口径不一致的风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证具体基准数值）
