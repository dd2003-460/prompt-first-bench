# N268: 在 BF16 精度下，RTX 4090 双卡 (TP=2) 方案因总显存 48GB < 模型需求 55GB，该工作点显存溢出，吞吐量理论值为 0 tokens/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N120

## Claim

在 BF16 精度下，RTX 4090 双卡 (TP=2) 方案因总显存 48GB < 模型需求 55GB，该工作点显存溢出，吞吐量理论值为 0 tokens/s，属于不可行工作点，必须通过量化或 Offload 修正。

## Corrected Claim

在 BF16 精度下，RTX 4090 双卡 (TP=2) 方案因总显存 48GB < 模型需求 55GB，该工作点显存溢出，吞吐量理论值为 0 tokens/s，属于不可行工作点，必须通过量化或 Offload 修正。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 单卡显存为 24GB，双卡总显存 48GB，小于模型需求 55GB，显存溢出导致不可行，吞吐量理论值为 0 符合逻辑。
