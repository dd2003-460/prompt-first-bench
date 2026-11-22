# N25: 单卡方案瓶颈：27B BF16 模型权重占 54GB，RTX 4090 (24GB) 无法加载，必须使用 INT4/FP8 量化或 Offloading；量化后

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

单卡方案瓶颈：27B BF16 模型权重占 54GB，RTX 4090 (24GB) 无法加载，必须使用 INT4/FP8 量化或 Offloading；量化后权重 ~14GB (INT4)，剩余显存用于 KV Cache，最大并发 Batch Size 受限于 (24GB - 14GB - 2GB OS) / KV_per_token

## Corrected Claim

单卡方案瓶颈：27B BF16 模型权重占 54GB，RTX 4090 (24GB) 无法加载，必须使用 INT4/FP8 量化或 Offloading；量化后权重 ~14GB (INT4)，剩余显存用于 KV Cache，最大并发 Batch Size 受限于 (24GB - 14GB - 2GB OS) / KV_per_token

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16权重约54GB，INT4量化后约14GB，显存计算逻辑自洽且符合硬件常识。

## Search Query

RTX 4090 24GB Qwen3-27B INT4 inference max batch size KV cache
