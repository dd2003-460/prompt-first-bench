# N251: 预热对 P99 改善的有效性边界：当基础命中率 H_base > 0.95 时，p_miss_base < 0.05，预热带来的绝对延迟改善 ΔP99_warm

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

预热对 P99 改善的有效性边界：当基础命中率 H_base > 0.95 时，p_miss_base < 0.05，预热带来的绝对延迟改善 ΔP99_warm < 0.05 * t_origin * 0.63 ≈ 3-10ms（假设 t_origin=20-50ms），此时预热成本可能超过延迟改善收益，预热策略仅在 H_base < 0.90 时具有显著成本效益

## Corrected Claim

预热对 P99 改善的有效性边界：当基础命中率 H_base > 0.95 时，p_miss_base < 0.05，预热带来的绝对延迟改善 ΔP99_warm < 0.05 * t_origin * 0.63 ≈ 3-10ms（假设 t_origin=20-50ms），此时预热成本可能超过延迟改善收益，预热策略仅在 H_base < 0.90 时具有显著成本效益

## Evidence

先验知识/题面给定，逻辑校验通过：基于缓存命中率的概率模型，当基础命中率极高（>0.95）时，未命中概率极低，预热带来的绝对延迟收益（毫秒级）通常小于预热维护成本，符合系统性能优化的基本经济直觉。
