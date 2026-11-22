# N273: 净提升幅度 ΔH_max 计算：基于 N104 和 N105 的量化值，ΔH_max = (0.2% - 0.5%) / 100% ≈ -0.3%，表明在给定参

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N95

## Claim

净提升幅度 ΔH_max 计算：基于 N104 和 N105 的量化值，ΔH_max = (0.2% - 0.5%) / 100% ≈ -0.3%，表明在给定参数下 LFU 相比 LRU 的理论最大提升为负值，即 LFU 性能劣于 LRU。

## Corrected Claim

净提升幅度 ΔH_max 计算：基于 N104 和 N105 的量化值，ΔH_max = (0.2% - 0.5%) / 100% ≈ -0.3%，表明在给定参数下 LFU 相比 LRU 的理论最大提升为负值，即 LFU 性能劣于 LRU。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 (0.2 - 0.5) / 100 = -0.003 即 -0.3% 正确，且负值确实表明 LFU 性能劣于 LRU，逻辑自洽。
