# N290: 在 S_total < C 的全量缓存场景下，LFU 与 LRU 的稳态字节命中率差异 ΔH_static = 0，因为两者都缓存了所有对象；LFU 的潜在增益

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 S_total < C 的全量缓存场景下，LFU 与 LRU 的稳态字节命中率差异 ΔH_static = 0，因为两者都缓存了所有对象；LFU 的潜在增益仅在容量受限 (S_total > C) 时通过优化对象选择产生，本题中最大潜在提升为 0 个百分点。

## Corrected Claim

在 S_total < C 的全量缓存场景下，LFU 与 LRU 的稳态字节命中率差异 ΔH_static = 0，因为两者都缓存了所有对象；LFU 的潜在增益仅在容量受限 (S_total > C) 时通过优化对象选择产生，本题中最大潜在提升为 0 个百分点。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

LFU LRU steady state hit rate difference full cache capacity
