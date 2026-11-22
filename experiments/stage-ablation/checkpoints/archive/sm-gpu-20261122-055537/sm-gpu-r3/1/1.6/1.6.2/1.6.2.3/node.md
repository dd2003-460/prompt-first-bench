# N185: KV Cache 对总显存需求的占比分析：在 RTX 4090 (24GB) 上运行 Qwen3-27B INT4 (权重~14GB) 时，KV Cache (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

KV Cache 对总显存需求的占比分析：在 RTX 4090 (24GB) 上运行 Qwen3-27B INT4 (权重~14GB) 时，KV Cache (7.25GB) 占比约为 30% (7.25/24)，剩余显存仅 2.75GB 用于激活值和框架开销。若上下文长度增加至 64K，KV Cache 翻倍至 14.5GB，总需求 28.5GB > 24GB，导致 OOM。因此 32K 是 24GB 卡运行 27B INT4 的临界上限。

## Corrected Claim

KV Cache 对总显存需求的占比分析：在 RTX 4090 (24GB) 上运行 Qwen3-27B INT4 (权重~14GB) 时，KV Cache (7.25GB) 占比约为 30% (7.25/24)，剩余显存仅 2.75GB 用于激活值和框架开销。若上下文长度增加至 64K，KV Cache 翻倍至 14.5GB，总需求 28.5GB > 24GB，导致 OOM。因此 32K 是 24GB 卡运行 27B INT4 的临界上限。

## Evidence

先验知识/题面给定，逻辑校验通过：权重14GB + KV 7.25GB + 开销2.75GB = 24GB，数学自洽；64K时KV翻倍至14.5GB，总需求28.5GB > 24GB，OOM结论符合显存管理逻辑。
