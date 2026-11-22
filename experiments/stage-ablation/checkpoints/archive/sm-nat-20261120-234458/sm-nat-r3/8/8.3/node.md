# N67: T_residence 的修正项：LRU 驻留时间并非均匀分布，热门对象驻留时间极短（接近访问间隔），冷对象驻留时间极长（接近缓存寿命），需用加权平均 T_re

- **status**: pending
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

父节点级核验未通过：不完备（子节点分别量化了热对象（r=1）和冷对象（r=N）的驻留时间，二者在频率分布上是互补且正交的，没有重复或矛盾。然而，父节点明确提出了'加权平均 T_residence_weighted'的计算公式，这是核心结论。现有的两个子节点仅提供了分布两端的边界条件（极值），完全缺失了中间大量对象的驻留时间分布情况，也未展示如何基于这些分布数据最终计算出加权平均值。因此，子节点未能覆盖父节点关于'计算加权平均'这一关键方面，导致逻辑链条断裂（从两端极值无法直接推导出全局加权平均，缺少中间过程或分布模型）。）
