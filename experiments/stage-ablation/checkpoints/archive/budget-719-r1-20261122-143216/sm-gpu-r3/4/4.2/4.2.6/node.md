# N103: Qwen3-27B 在 NVFP4/W4 精度下的 KL 散度误差分布，需计算 NVFP4/W4 与 BF16 输出概率分布的 KL 散度，预期 KL 散度 <

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

Qwen3-27B 在 NVFP4/W4 精度下的 KL 散度误差分布，需计算 NVFP4/W4 与 BF16 输出概率分布的 KL 散度，预期 KL 散度 < 0.1

## Corrected Claim

Qwen3-27B 在 NVFP4/W4 精度下的 KL 散度误差分布需通过实验计算 NVFP4/W4 与 BF16 输出概率分布的 KL 散度以评估量化影响，具体阈值需依据实测数据确定。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（KL < 0.1），属于特定模型在特定量化精度下的性能指标，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B NVFP4 W4 KL divergence error distribution
