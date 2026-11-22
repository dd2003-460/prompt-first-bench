# N33: 2×NVIDIA RTX 4090 (48GB 总显存) 的总显存带宽为 2016 GB/s，总 MSRP 为 $3198，双卡可承载 Qwen3-27B 的 

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

2×NVIDIA RTX 4090 (48GB 总显存) 的总显存带宽为 2016 GB/s，总 MSRP 为 $3198，双卡可承载 Qwen3-27B 的 BF16 权重（约 54GB）需 INT8 量化，FP8 权重（约 13.5GB）双卡可容纳且剩余显存支持 32K 上下文，INT4 权重（约 6.75GB）双卡可容纳且支持更长上下文。

## Corrected Claim

2×NVIDIA RTX 4090 (48GB 总显存) 的总显存带宽为 2016 GB/s，总 MSRP 为 $3198。双卡可承载 Qwen3-27B 的 BF16 权重（约 54GB）需 INT8 量化（约 27GB）或更低精度。FP8 权重（约 27GB）双卡可容纳，剩余显存约 21GB 支持一定长度的上下文。INT4 权重（约 13.5GB）双卡可容纳且支持更长上下文。

## Evidence

[质询]RTX 4090 的标准显存容量为 24GB，双卡总显存为 48GB，但单卡显存带宽为 1008 GB/s，双卡总带宽应为 2016 GB/s。然而，RTX 4090 的 MSRP 为 $1599，双卡总价为 $3198。陈述中关于显存容量、带宽和价格的数值本身是准确的。但是，Qwen3-27B 的 BF16 权重约为 54GB，确实超过 48GB 总显存，需要量化。FP8 权重约为 27GB（27B * 1 byte），而非 13.5GB（13.5GB 是 INT4 或类似更低精度的大小，或者是对 27B 参数量的误算，27B * 0.5 bytes = 13.5GB 是 INT4 的大小，FP8 是 1 byte，所以 27B 的 FP8 权重应为 27GB）。因此，陈述中 'FP8 权重（约 13.5GB）' 存在事实错误，FP8 权重应为 27GB 左右。 | RTX 4090 单卡 24GB，双卡 48GB，带宽 1008GB/s * 2 = 2016GB/s，价格 $1599 * 2 = $3198 均正确。但 Qwen3-27B 的 FP8 权重应为 27B * 1 byte = 27GB，而非 13.5GB（13.5GB 对应 INT4 或 0.5 byte/param）。陈述中 FP8 权重数值错误，导致后续关于剩余显存和上下文长度的推断基础错误。
