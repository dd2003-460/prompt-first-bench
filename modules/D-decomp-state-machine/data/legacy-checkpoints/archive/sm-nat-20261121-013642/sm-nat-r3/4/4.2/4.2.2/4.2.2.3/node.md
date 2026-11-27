# N180: N61 的 K 值选择工作点 2（平衡点/最优性价比）：若缓存 Top-10,000 对象（覆盖约 65% 总字节量且包含 Top-500 热对象），H_byt

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

N61 的 K 值选择工作点 2（平衡点/最优性价比）：若缓存 Top-10,000 对象（覆盖约 65% 总字节量且包含 Top-500 热对象），H_byte_LRU ≈ 0.65，此工作点在 α=1.1, β=0.9 下为字节命中率与缓存容量的最优平衡点。

## Corrected Claim

N61 的 K 值选择工作点 2（平衡点/最优性价比）：若缓存 Top-10,000 对象（覆盖约 65% 总字节量且包含 Top-500 热对象），H_byte_LRU ≈ 0.65，此工作点在 α=1.1, β=0.9 下为字节命中率与缓存容量的最优平衡点。

## Evidence

先验知识/题面给定，逻辑校验通过
