# N151: 在 S_total ≈ 602MB (N114) 且 C=128GB 的条件下，缓存容量比 C/S_total ≈ 212，表明缓存可容纳全部对象。因此 LRU

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 S_total ≈ 602MB (N114) 且 C=128GB 的条件下，缓存容量比 C/S_total ≈ 212，表明缓存可容纳全部对象。因此 LRU 稳态字节命中率下界由‘全缓存’假设主导，即 H_LRU_base ≈ 1.0 (100%)，除非考虑冷启动或更新失效。

## Corrected Claim

在 S_total ≈ 602MB (N114) 且 C=128GB 的条件下，缓存容量比 C/S_total ≈ 212，表明缓存可容纳全部对象。因此 LRU 稳态字节命中率下界由‘全缓存’假设主导，即 H_LRU_base ≈ 1.0 (100%)，除非考虑冷启动或更新失效。

## Evidence

检索失败: no sources from any channel (all 5 failed)
