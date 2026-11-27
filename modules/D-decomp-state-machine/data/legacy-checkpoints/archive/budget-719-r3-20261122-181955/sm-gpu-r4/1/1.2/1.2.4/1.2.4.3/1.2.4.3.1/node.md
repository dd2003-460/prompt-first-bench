# N476: NVIDIA L40S 的显存带宽为 864 GB/s (GDDR6)，在 32K 上下文、BF16 精度下，Decode 阶段单请求需读取的总数据量 = 54

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N161

## Claim

NVIDIA L40S 的显存带宽为 864 GB/s (GDDR6)，在 32K 上下文、BF16 精度下，Decode 阶段单请求需读取的总数据量 = 54GB (权重) + 8.59GB (KV Cache, 基于 N369 修正参数) = 62.59GB，理论 Decode 吞吐量上限 = 864 / 62.59 ≈ 13.8 tokens/s，对应 ITL 理论下限 ≈ 72.4 ms/token。

## Corrected Claim

NVIDIA L40S 的显存带宽为 864 GB/s (GDDR6)，在 32K 上下文、BF16 精度下，Decode 阶段单请求需读取的总数据量 = 54GB (权重) + 8.59GB (KV Cache, 基于 N369 修正参数) = 62.59GB，理论 Decode 吞吐量上限 = 864 / 62.59 ≈ 13.8 tokens/s，对应 ITL 理论下限 ≈ 72.4 ms/token。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA L40S 显存带宽 864 GB/s 符合 GDDR6 规格；数据量 62.59GB 与吞吐量 13.8 tokens/s (864/62.59) 及延迟 72.4ms (1/13.8) 计算自洽。

## Search Query

NVIDIA L40S memory bandwidth GB/s GDDR6
