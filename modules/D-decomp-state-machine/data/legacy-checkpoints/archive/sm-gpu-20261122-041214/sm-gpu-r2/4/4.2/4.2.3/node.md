# N127: FP8 精度下，单卡 48GB (如 A6000) 剩余可用显存 = 48 GiB - 25.16 GiB (权重) - 1.25 GiB (加载开销) ≈ 2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

FP8 精度下，单卡 48GB (如 A6000) 剩余可用显存 = 48 GiB - 25.16 GiB (权重) - 1.25 GiB (加载开销) ≈ 21.59 GiB，可容纳约 43K tokens 的 KV Cache，满足 32K 上下文需求并留有并发余量。

## Corrected Claim

FP8 精度下，单卡 48GB (如 A6000) 剩余可用显存 = 48 GiB - 25.16 GiB (权重) - 1.25 GiB (加载开销) ≈ 21.59 GiB，可容纳约 43K tokens 的 KV Cache，满足 32K 上下文需求并留有并发余量。

## Evidence

先验知识/题面给定，逻辑校验通过：48-25.16-1.25=21.59 GiB，算术正确；21.59 GiB / 43K tokens ≈ 512 bytes/token，符合FP8下主流大模型KV Cache的典型量级，逻辑自洽。
