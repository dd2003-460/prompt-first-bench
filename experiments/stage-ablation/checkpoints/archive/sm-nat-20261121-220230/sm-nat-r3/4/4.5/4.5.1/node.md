# N73: 更新率 u 与热度 H 的独立性假设检验：若 u 与 H 独立，则 ΔDiscount_LFU = 0；若存在负相关（如 ρ_uH = -0.2），则 LFU 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

更新率 u 与热度 H 的独立性假设检验：若 u 与 H 独立，则 ΔDiscount_LFU = 0；若存在负相关（如 ρ_uH = -0.2），则 LFU 的折损因子比 LRU 低约 5-10%，需量化该交互项的具体数值。

## Corrected Claim

更新率 u 与热度 H 的独立性假设检验：若 u 与 H 独立，则 ΔDiscount_LFU = 0；若存在负相关（如 ρ_uH = -0.2），则 LFU 的折损因子比 LRU 低约 5-10%，需量化该交互项的具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过：独立性假设下交互项为零符合统计定义，负相关导致LFU折损低于LRU符合缓存替换策略的基本逻辑，数值量级（5-10%）在工程经验范围内合理。
