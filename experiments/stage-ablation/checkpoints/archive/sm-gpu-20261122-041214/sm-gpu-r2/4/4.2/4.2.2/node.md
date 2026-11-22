# N126: FP8 精度下，单卡 32GB (如 4090 48G mod 或 L4) 剩余可用显存 = 32 GiB - 25.16 GiB (权重) - 1.25 Gi

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

FP8 精度下，单卡 32GB (如 4090 48G mod 或 L4) 剩余可用显存 = 32 GiB - 25.16 GiB (权重) - 1.25 GiB (加载开销) ≈ 5.59 GiB，仅能容纳约 11K tokens 的 KV Cache (基于 N36 公式)，不满足 32K 上下文需求。

## Corrected Claim

FP8 精度下，单卡 32GB (如 4090 48G mod 或 L4) 剩余可用显存 = 32 GiB - 25.16 GiB (权重) - 1.25 GiB (加载开销) ≈ 5.59 GiB，仅能容纳约 11K tokens 的 KV Cache (基于 N36 公式)，不满足 32K 上下文需求。

## Evidence

先验知识/题面给定，逻辑校验通过：32 - 25.16 - 1.25 = 5.59 GiB，数值计算准确；基于FP8精度及典型KV Cache大小估算，5.59 GiB确实仅能容纳约11K tokens，远小于32K需求，结论自洽。
