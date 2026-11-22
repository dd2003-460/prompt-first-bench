# N111: 搜索耐心阈值 δ_patience 的量化：定义为买家在降价后愿意重新检索的最大时间窗口，通常假设 δ_patience ≈ 48 小时（基于题面中 48 小时

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N32

## Claim

搜索耐心阈值 δ_patience 的量化：定义为买家在降价后愿意重新检索的最大时间窗口，通常假设 δ_patience ≈ 48 小时（基于题面中 48 小时无新咨询的观察）。在 t > δ_patience 时，P(trigger) 趋近于 0，导致 λ_new(t, ΔP) 衰减至基准水平。

## Corrected Claim

搜索耐心阈值 δ_patience 的量化：定义为买家在降价后愿意重新检索的最大时间窗口，通常假设 δ_patience ≈ 48 小时（基于题面中 48 小时无新咨询的观察）。在 t > δ_patience 时，P(trigger) 趋近于 0，导致 λ_new(t, ΔP) 衰减至基准水平。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

buyer patience threshold time window re-search behavior
