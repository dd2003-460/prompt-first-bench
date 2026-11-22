# N413: W4 量化在 Qwen3-27B 上的 FID 分数变化 ΔFID 实测值，用于验证 W4 是否导致生成文本多样性显著下降（ΔFID > 5），特别是长尾词汇的

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N134, N135, N136

## Claim

W4 量化在 Qwen3-27B 上的 FID 分数变化 ΔFID 实测值，用于验证 W4 是否导致生成文本多样性显著下降（ΔFID > 5），特别是长尾词汇的覆盖度损失

## Corrected Claim

W4 量化在 Qwen3-27B 上可能导致生成文本多样性下降，但具体 FID 分数变化 ΔFID 的实测值及是否显著超过 5 的阈值需依赖特定实验数据验证，当前缺乏直接证据支持该具体数值结论。

## Evidence

[质询]该陈述声称存在具体的“实测值”并设定了特定的阈值（ΔFID > 5）来验证多样性下降，但FID通常用于图像生成评估，用于文本多样性评估属于非标准用法，且缺乏具体实验数据支持该特定数值阈值和结论的普适性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且FID用于文本多样性评估非标准，具体数值阈值缺乏依据）

## Search Query

Qwen3-27B W4 quantization FID score text diversity loss
