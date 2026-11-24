# N551: 核心区域P99延迟 L_p99_core 的精确计算：L_p99_core = L_prop_core + L_processing + L_backhaul 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N179

## Claim

核心区域P99延迟 L_p99_core 的精确计算：L_p99_core = L_prop_core + L_processing + L_backhaul * (1 - H_core)，其中 L_prop_core = R_avg / v_fiber = 300km / 200,000km/s = 1.5ms，L_processing = 5ms（边缘节点处理延迟），H_core = 0.85（核心区域缓存命中率高于全国均值），L_backhaul = 50ms（回源延迟），故 L_p99_core = 1.5 + 5 + 50 * 0.15 = 14ms；此值用于判断核心区域P99延迟是否满足目标T。

## Corrected Claim

核心区域P99延迟 L_p99_core 的精确计算：L_p99_core = L_prop_core + L_processing + L_backhaul * (1 - H_core)，其中 L_prop_core = R_avg / v_fiber = 300km / 200,000km/s = 1.5ms，L_processing = 5ms（边缘节点处理延迟），H_core = 0.85（核心区域缓存命中率高于全国均值），L_backhaul = 50ms（回源延迟），故 L_p99_core = 1.5 + 5 + 50 * 0.15 = 14ms；此值用于判断核心区域P99延迟是否满足目标T。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合延迟分解原理，数值计算 1.5 + 5 + 50 * 0.15 = 14 准确无误，量纲一致。
