# N170: Write-Back 模式下若假设缓存满载（U=100%）的敏感性分析：P_evict_dirty = (Cache Misses_read / Total R

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N60

## Claim

Write-Back 模式下若假设缓存满载（U=100%）的敏感性分析：P_evict_dirty = (Cache Misses_read / Total Requests) * P_dirty|miss。若 Hit_Rate=20.6%（保守下界），Miss Rate=79.4%，P_evict_dirty ≈ 0.794 * 2.3e-8 ≈ 1.8e-8，对命中率折损可忽略（< 0.000002%）。

## Corrected Claim

Write-Back 模式下若假设缓存满载（U=100%）的敏感性分析：P_evict_dirty = (Cache Misses_read / Total Requests) * P_dirty|miss。若 Hit_Rate=20.6%（保守下界），Miss Rate=79.4%，P_evict_dirty ≈ 0.794 * 2.3e-8 ≈ 1.8e-8，对命中率折损可忽略（< 0.000002%）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合概率论基本规则，数值量级（1.8e-8）与输入参数（0.794 * 2.3e-8）一致，且对命中率影响极小的结论符合直觉。
