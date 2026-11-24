# N137: 高压缩工作点：s_img = 0.15 MB (150 KB)，基于 WebP q=60 或 JPEG q=75 压缩，P99 视觉质量评分 MOS ≥ 3.5

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

高压缩工作点：s_img = 0.15 MB (150 KB)，基于 WebP q=60 或 JPEG q=75 压缩，P99 视觉质量评分 MOS ≥ 3.5，缓存命中率 H_img 提升至 92%（因对象更小，内存缓存驻留时间增加）

## Corrected Claim

高压缩工作点：s_img = 0.15 MB (150 KB)，基于 WebP q=60 或 JPEG q=75 压缩，P99 视觉质量评分 MOS ≥ 3.5，缓存命中率 H_img 显著提升（因对象更小，内存缓存驻留时间增加）

## Evidence

[质询]缓存命中率从常规水平提升至92%且归因于对象变小导致驻留时间增加，这一具体数值（92%）及因果机制属于高度依赖具体业务场景、访问模式（Zipf分布斜率）和缓存策略的经验性参数，无法从第一性原理严格推导，且缺乏通用工程共识支持该特定数值。 | source=knowledge，逻辑上对象变小确实有助于提升缓存驻留率，但92%这一具体经验数值缺乏通用理论支撑，属于特定场景下的经验事实，故降级。
