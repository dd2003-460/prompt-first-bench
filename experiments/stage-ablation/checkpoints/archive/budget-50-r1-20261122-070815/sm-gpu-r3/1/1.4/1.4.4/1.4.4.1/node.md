# N186: 2x RTX 4090 双卡 BF16 方案的显存瓶颈修正：Qwen3-27B BF16 权重为 54 GB，加上 32K 上下文 KV Cache 2.0 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

2x RTX 4090 双卡 BF16 方案的显存瓶颈修正：Qwen3-27B BF16 权重为 54 GB，加上 32K 上下文 KV Cache 2.0 GB（混合架构）及 15% 开销 8.1 GB，总需求 64.1 GB，超过双卡总显存 48 GB，确认 BF16 双卡不可行；若采用 FP8，总需求 32.05 GB < 48 GB，可行，但需评估 PCIe 4.0 x16 互联带宽（单向 32 GB/s [修正自矛盾检测：N114 数值更可信，N84 的 50-55 GB/s 可能包含双向或误读]）对 KV Cache 分片传输的延迟影响

## Corrected Claim

2x RTX 4090 双卡 BF16 方案的显存瓶颈修正：Qwen3-27B BF16 权重为 54 GB，加上 32K 上下文 KV Cache 2.0 GB（混合架构）及 15% 开销 8.1 GB，总需求 64.1 GB，超过双卡总显存 48 GB，确认 BF16 双卡不可行；若采用 FP8，总需求 32.05 GB < 48 GB，可行，但需评估 PCIe 4.0 x16 互联带宽（单向 32 GB/s [修正自矛盾检测：N114 数值更可信，N84 的 50-55 GB/s 可能包含双向或误读]）对 KV Cache 分片传输的延迟影响

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16权重约54GB，加上KV Cache及开销后总需求64.1GB，确实超过2x48GB=96GB? 不，2x RTX 4090是24GB*2=48GB。64.1GB > 48GB，逻辑成立。FP8权重27GB，总需求32.05GB < 48GB，逻辑成立。PCIe 4.0 x16单向带宽32GB/s符合标准规格。

## Search Query

PCIe 4.0 x16 bandwidth unidirectional GB/s NVIDIA spec
