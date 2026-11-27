# N93: 搜索时间分布的尾部风险：由于 λ_liq 的非负约束，T_search 服从逆 Gamma 分布或类似重尾分布，其 95% 分位数 Q95(T_search) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N28

## Claim

搜索时间分布的尾部风险：由于 λ_liq 的非负约束，T_search 服从逆 Gamma 分布或类似重尾分布，其 95% 分位数 Q95(T_search) 可能显著高于均值，需计算 Q95(T_search) / E[T_search] 比值，若 > 1.5，则长尾搜索行为对平台整体周转率有显著拖累。

## Corrected Claim

搜索时间分布的尾部风险：由于 λ_liq 的非负约束，T_search 服从逆 Gamma 分布或类似重尾分布，其 95% 分位数 Q95(T_search) 可能显著高于均值，需计算 Q95(T_search) / E[T_search] 比值，若 > 1.5，则长尾搜索行为对平台整体周转率有显著拖累。

## Evidence

先验知识/题面给定，逻辑校验通过：逆Gamma分布具有重尾特性，其分位数与均值之比（Q95/E）通常大于1，且对于典型参数（如形状参数较小）该比值确实可能超过1.5，符合统计学直觉。
