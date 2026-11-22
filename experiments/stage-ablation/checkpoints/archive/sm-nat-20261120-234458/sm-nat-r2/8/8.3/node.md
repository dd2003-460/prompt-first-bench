# N67: T_residence 的修正项：LRU 驻留时间并非均匀分布，热门对象驻留时间极短（接近访问间隔），冷对象驻留时间极长（接近缓存寿命），需用加权平均 T_re

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

T_residence 的修正项：LRU 驻留时间并非均匀分布，热门对象驻留时间极短（接近访问间隔），冷对象驻留时间极长（接近缓存寿命），需用加权平均 T_residence_weighted = Σ (Frequency_i * T_residence_i) / Σ Frequency_i 计算

## Corrected Claim

T_residence 的修正项：LRU 驻留时间并非均匀分布，热门对象驻留时间极短（接近访问间隔），冷对象驻留时间极长（接近缓存寿命），需用加权平均 T_residence_weighted = Σ (Frequency_i * T_residence_i) / Σ Frequency_i 计算

## Evidence

先验知识/题面给定，逻辑校验通过
