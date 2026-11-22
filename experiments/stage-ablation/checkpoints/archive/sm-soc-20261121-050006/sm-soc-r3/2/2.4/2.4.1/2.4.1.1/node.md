# N210: 成交周期偏差（T_close_bias）的量化：T_close_bias = k_match * σ_match * log(λ_search / P_ask)

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N64

## Claim

成交周期偏差（T_close_bias）的量化：T_close_bias = k_match * σ_match * log(λ_search / P_ask)，其中 k_match 为匹配摩擦系数（k_match ∈ [0.5, 1.5]），λ_search 为买家搜索强度（单位：次/天），P_ask 为挂价，该公式将 σ_match 转化为成交周期的观测偏差。

## Corrected Claim

T_close_bias = k_match * σ_match * log(λ_search / λ_ref)，其中 λ_ref 为基准搜索强度（单位：次/天），确保对数项无量纲；或修正为 T_close_bias = k_match * σ_match * (1 - P_ask / P_ref)，需明确各变量量纲一致性。

## Evidence

[质询]公式量纲不自洽：σ_match（标准差，通常无量纲或为时间单位）与 log(λ_search / P_ask)（对数项，要求参数无量纲，但 λ_search 单位为次/天，P_ask 为货币单位，两者相除量纲不匹配）相乘，导致 T_close_bias 的量纲无法明确对应为时间单位（天），存在明显的物理/经济量纲错误。 | 逻辑校验发现量纲矛盾：λ_search (1/day) 与 P_ask (currency) 之比无意义，无法取对数；且 source 为 knowledge，虽无需外部来源，但内部逻辑硬伤导致无法 verified。
