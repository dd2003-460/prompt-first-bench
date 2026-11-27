# N62: 工作点 B（工业标准）：取 S_max = 100MB（典型 CDN 对象上限），此时 S_threshold 的计算包含更大对象，预计 S_threshold

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

工作点 B（工业标准）：取 S_max = 100MB（典型 CDN 对象上限），此时 S_threshold 的计算包含更大对象，预计 S_threshold ≈ 200KB，该值用于计算 LRU 命中率基准 H_LRU_base。

## Corrected Claim

工作点 B（工业标准）：取 S_max = 100MB（典型 CDN 对象上限），此时 S_threshold 的计算包含更大对象，预计 S_threshold ≈ 200KB，该值用于计算 LRU 命中率基准 H_LRU_base。

## Evidence

先验知识/题面给定，逻辑校验通过
