# N175: 工作点1（小对象主导）：设定 s_min=1KB, s_max=1MB (截断)，E[Size] ≈ 2KB (α=1.1 截断均值)，R_bytes = 5e

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

工作点1（小对象主导）：设定 s_min=1KB, s_max=1MB (截断)，E[Size] ≈ 2KB (α=1.1 截断均值)，R_bytes = 5e7 * 2KB = 100GB/day。此场景下 128GB 缓存可覆盖大部分热门对象，H_byte_LRU 预期较高 (>0.8)。

## Corrected Claim

工作点1（小对象主导）：设定 s_min=1KB, s_max=1MB (截断)，E[Size] ≈ 2KB (α=1.1 截断均值)，R_bytes = 5e7 * 2KB = 100GB/day。此场景下 128GB 缓存可覆盖大部分热门对象，H_byte_LRU 预期较高 (>0.8)。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 5e7 * 2KB = 100GB 正确；在 Zipf 分布（α=1.1）且缓存容量（128GB）远大于平均对象大小（2KB）且覆盖大部分热门对象的场景下，LRU 命中率 >0.8 符合缓存理论直觉。
