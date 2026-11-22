# N110: EPYC 9654 (128核, 3TB DDR5) 的内存容量为 3TB，Qwen3-27B W4 权重 13.5GB + 8.4GB (KV Cache) 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

EPYC 9654 (128核, 3TB DDR5) 的内存容量为 3TB，Qwen3-27B W4 权重 13.5GB + 8.4GB (KV Cache) + 2GB (激活) = 23.9GB，剩余 2976.1GB 内存可用于增加并发或更长上下文，内存利用率约 0.79%。

## Corrected Claim

EPYC 9654 (128核, 3TB DDR5) 的内存容量为 3TB，Qwen3-27B W4 权重 13.5GB + 8.4GB (KV Cache) + 2GB (激活) = 23.9GB，剩余 2976.1GB 内存可用于增加并发或更长上下文，内存利用率约 0.79%。

## Evidence

先验知识/题面给定，逻辑校验通过：EPYC 9654 支持 3TB 内存，Qwen3-27B W4 量化后权重约 13.5GB，总占用 23.9GB 远小于 3TB，利用率计算 (23.9/3072 ≈ 0.78%) 合理。
