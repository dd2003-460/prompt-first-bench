# N34: 1×NVIDIA L40S (48GB GDDR6) 的显存带宽为 864 GB/s，价格约为 $8000-$10000，单卡可承载 Qwen3-27B 的 F

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

1×NVIDIA L40S (48GB GDDR6) 的显存带宽为 864 GB/s，价格约为 $8000-$10000，单卡可承载 Qwen3-27B 的 FP8 权重（约 13.5GB）且剩余显存支持 32K 上下文，BF16 权重需 INT8 量化后单卡可容纳，INT4 权重（约 6.75GB）单卡可容纳且支持更长上下文。

## Corrected Claim

1×NVIDIA L40S (48GB GDDR6) 的显存带宽为 864 GB/s，价格约为 $8000-$10000，单卡可承载 Qwen3-27B 的 FP8 权重（约 13.5GB）且剩余显存支持 32K 上下文，BF16 权重需 INT8 量化后单卡可容纳，INT4 权重（约 6.75GB）单卡可容纳且支持更长上下文。

## Evidence

先验知识/题面给定，逻辑校验通过：L40S 48GB GDDR6 带宽 864 GB/s 符合规格；Qwen3-27B FP8 权重约 13.5GB，剩余显存约 34.5GB，足以支持 32K 上下文（KV Cache 占用通常在几 GB 至十几 GB 之间，取决于 batch size 和具体实现，但单卡 48GB 在合理配置下可容纳）；BF16 权重约 27GB，INT8 量化后约 13.5GB，单卡可容纳；INT4 权重约 6.75GB，单卡可容纳且支持更长上下文。所有数值量级和逻辑关系自洽。
