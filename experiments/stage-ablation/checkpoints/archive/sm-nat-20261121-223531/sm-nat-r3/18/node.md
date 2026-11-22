# N249: 更新率对LRU有效性的衰减机制：在Write-Through模式下，1%/天的更新率对LRU命中率的影响取决于‘数据一致性检查’的成本。若CDN节点在每次命中时

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

更新率对LRU有效性的衰减机制：在Write-Through模式下，1%/天的更新率对LRU命中率的影响取决于‘数据一致性检查’的成本。若CDN节点在每次命中时验证版本（Version Check），则更新不导致Miss，但增加CPU开销；若仅在下发时验证，则更新导致Stale Data，需回源刷新。推导折损系数D_stale = P(Update | Residency Time)。对于热门对象（驻留时间短），D_stale ≈ λ_upd * T_res；对于冷门对象（驻留时间长），D_stale ≈ 1。在C >> S_total场景下，所有对象驻留，但热门对象T_res极短，故整体折损极小（<0.1%）。

## Corrected Claim

在Write-Through模式下，更新率对LRU命中率的影响取决于数据一致性检查策略。若每次命中时验证版本，更新不导致Miss但增加CPU开销；若仅在下发时验证，更新可能导致Stale Data需回源。折损系数D_stale与更新率λ_upd及驻留时间T_res正相关（D_stale ≈ λ_upd * T_res），具体数值需根据实际系统参数计算，而非固定为<0.1%。

## Evidence

[质询]该陈述包含具体的工程经验参数（如1%/天更新率、<0.1%折损阈值）及特定场景下的推导结论，属于经验事实而非纯逻辑/数学公理推论；且参考来源仅定性描述Write-Through的一致性优势，未提供具体的命中率衰减公式或数值支持，无法排除其他实现细节（如异步验证、TTL策略）对折损系数的影响。 | 逻辑推导自洽（D_stale公式符合概率直觉），但来源[1]仅间接支持Write-Through的一致性机制，未直接支持具体的折损系数数值或公式，且该事实属于经验工程参数，缺乏多源一致或第一性原理严格推导依据。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/713357984&rut=c6b29e3e969545e20023c8ae9d41da7ef05b9f8723b1d78ba08a0e8272a62c5d', 'type': 'ddg', 'title': '高并发下的分布式缓存 | Write-Through缓存模式 - 知乎'}
