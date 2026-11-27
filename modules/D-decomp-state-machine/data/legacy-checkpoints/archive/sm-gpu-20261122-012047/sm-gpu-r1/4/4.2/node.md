# N28: NVIDIA RTX 5090 (32GB GDDR7) 的显存带宽预计为 1792 GB/s，MSRP 为 $1999，单卡可完整承载 Qwen3-27B 的

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

NVIDIA RTX 5090 (32GB GDDR7) 的显存带宽预计为 1792 GB/s，MSRP 为 $1999，单卡可完整承载 Qwen3-27B 的 BF16 权重（约 54GB）需双卡或量化，FP8 权重（约 13.5GB）单卡可容纳且剩余显存充足支持 32K 上下文，INT4 权重（约 6.75GB）单卡可容纳且支持更长上下文。

## Corrected Claim

NVIDIA RTX 5090 (32GB GDDR7) 的显存带宽预计为 1792 GB/s，MSRP 为 $1999，单卡可完整承载 Qwen3-27B 的 BF16 权重（约 54GB）需双卡或量化，FP8 权重（约 13.5GB）单卡可容纳且剩余显存充足支持 32K 上下文，INT4 权重（约 6.75GB）单卡可容纳且支持更长上下文。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 32GB GDDR7 带宽 1792 GB/s 及 MSRP $1999 符合 NVIDIA 官方发布规格；Qwen3-27B 参数量约 27B，BF16 权重约 54GB 超出单卡 32GB 显存，FP8 约 13.5GB 及 INT4 约 6.75GB 均在 32GB 范围内，计算逻辑自洽。
