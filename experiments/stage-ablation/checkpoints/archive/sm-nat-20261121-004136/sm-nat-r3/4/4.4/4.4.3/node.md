# N59: 有效命中率折损因子 Discount_Factor 的量化推导：Discount_Factor = 1 - λ_update * (E[Size | Updat

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N18

## Claim

有效命中率折损因子 Discount_Factor 的量化推导：Discount_Factor = 1 - λ_update * (E[Size | Updated] / E[Size]) * (1 - H_LRU_original)，其中 H_LRU_original 为无更新时的命中率，λ_update=0.01/day，直接给出‘打几折’的数值。

## Corrected Claim

Discount_Factor 可近似表示为 1 - λ_update * (E[Size | Updated] / E[Size]) * (1 - H_LRU_original)，用于估算有效命中率的折损程度，但具体数值需结合系统实际参数校准，不宜视为精确理论值。

## Evidence

父节点级核验失败（LLM 错误）：curl rc=28 b''
