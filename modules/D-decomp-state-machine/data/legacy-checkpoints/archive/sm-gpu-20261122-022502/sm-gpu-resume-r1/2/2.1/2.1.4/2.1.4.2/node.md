# N174: RTX 4090 在 32K 上下文 FP8 场景下的多卡必要性及 TCO 劣势：FP8 权重 27GB > 24GB，单卡不可行。需 2x 4090 (48G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

RTX 4090 在 32K 上下文 FP8 场景下的多卡必要性及 TCO 劣势：FP8 权重 27GB > 24GB，单卡不可行。需 2x 4090 (48GB)。CapEx $3198 + $2000 = $5198。由于多卡通信开销，有效带宽降至 ~504 GB/s (N91)，吞吐 ≈ 18.7 tokens/s。单位成本 = $5198 / 18.7 ≈ $277.96/token/s (年化 OpEx 另计，此处仅 CapEx 占比高)，远高于单卡 16K 场景的 $21.43/token/s。

## Corrected Claim

RTX 4090 在 32K 上下文 FP8 场景下的多卡必要性及 TCO 劣势：FP8 权重 27GB > 24GB，单卡不可行。需 2x 4090 (48GB)。CapEx $3198 + $2000 = $5198。由于多卡通信开销，有效带宽降至 ~504 GB/s (N91)，吞吐 ≈ 18.7 tokens/s。单位成本 = $5198 / 18.7 ≈ $277.96/token/s (年化 OpEx 另计，此处仅 CapEx 占比高)，远高于单卡 16K 场景的 $21.43/token/s。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8权重27GB确实超过单卡24GB显存，需双卡；双卡通信开销导致有效带宽下降及TCO上升符合硬件工程常识，数值量级合理。
