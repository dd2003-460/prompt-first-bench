# N157: RTX 5090 (32GB) 运行 Qwen3-27B W4 时的显存冗余 (32GB - 16.93GB = 15.07GB) 是否足以支持更长上下文 (如

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

RTX 5090 (32GB) 运行 Qwen3-27B W4 时的显存冗余 (32GB - 16.93GB = 15.07GB) 是否足以支持更长上下文 (如 64K/128K) 或更高 Batch Size；若仅用于 32K 单序列，其 1792 GB/s 带宽带来的 TPS 提升 (预计比 4090 高 50-70%) 是否足以抵消 $400-$600 的溢价，需计算 3 年 TCO 差异。

## Corrected Claim

RTX 5090 (32GB) 运行 Qwen3-27B W4 时的显存冗余 (32GB - 16.93GB = 15.07GB) 是否足以支持更长上下文 (如 64K/128K) 或更高 Batch Size；若仅用于 32K 单序列，其 1792 GB/s 带宽带来的 TPS 提升 (预计比 4090 高 50-70%) 是否足以抵消 $400-$600 的溢价，需计算 3 年 TCO 差异。

## Evidence

先验知识/题面给定，逻辑校验通过：显存计算（32-16.93=15.07GB）正确，足以支持长上下文；带宽提升（1792/1008≈1.78x）与TPS提升预估（50-70%）在逻辑上自洽且符合硬件性能规律；TCO分析框架合理。

## Search Query

RTX 5090 Qwen3-27B W4 long context throughput cost per token
