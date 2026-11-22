# N102: Qwen3-27B 在 FP8 精度下的 KL 散度误差分布，需计算 FP8 与 BF16 输出概率分布的 KL 散度，预期 KL 散度 < 0.05

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

Qwen3-27B 在 FP8 精度下的 KL 散度误差分布，需计算 FP8 与 BF16 输出概率分布的 KL 散度，预期 KL 散度 < 0.05

## Corrected Claim

Qwen3-27B 在 FP8 精度下的 KL 散度误差分布需通过计算 FP8 与 BF16 输出概率分布的 KL 散度来评估，具体阈值需根据实际应用场景和数据集确定，通常预期在较小范围内（如 < 0.05），但需实证验证。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（KL < 0.05），属于经验事实而非第一性原理可推导结论；且不同模型、不同数据集下FP8与BF16的KL散度分布差异较大，缺乏通用性保证，单一阈值可能不适用于所有场景。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值阈值的普适性）

## Search Query

Qwen3-27B FP8 KL divergence error distribution
