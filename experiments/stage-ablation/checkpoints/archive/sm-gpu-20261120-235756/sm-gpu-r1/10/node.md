# N35: AMD MI300X 拥有 192GB HBM3 显存和 5300 GB/s 带宽，单卡即可容纳 Qwen3-27B BF16 权重及长上下文 KV Cache

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

AMD MI300X 拥有 192GB HBM3 显存和 5300 GB/s 带宽，单卡即可容纳 Qwen3-27B BF16 权重及长上下文 KV Cache，无需量化，适合对精度敏感且预算充足的数据中心级场景。

## Corrected Claim

AMD MI300X 拥有 192GB HBM3 显存和 5300 GB/s 带宽，单卡即可容纳 Qwen3-27B BF16 权重及长上下文 KV Cache，无需量化，适合对精度敏感且预算充足的数据中心级场景。

## Evidence

[rework-angle r1] 来源[3]和[4]直接确认了192GB HBM3显存和5.3 TB/s带宽；Qwen3-27B BF16权重约54GB，加上长上下文KV Cache在192GB容量内完全可行，逻辑自洽且有多源支持。

## Search Query

AMD MI300X HBM3 memory bandwidth specifications
