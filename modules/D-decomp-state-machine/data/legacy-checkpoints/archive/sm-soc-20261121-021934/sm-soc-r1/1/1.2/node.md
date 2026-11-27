# N6: 演化定向压力投影1：损失厌恶系数 λ 使得卖家心理保留价 P_min = V_true + λ·(V_true - P_market)，其中 λ ∈ [1.5,

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

演化定向压力投影1：损失厌恶系数 λ 使得卖家心理保留价 P_min = V_true + λ·(V_true - P_market)，其中 λ ∈ [1.5, 2.5]（Kahneman & Tversky 经典值），导致挂价 P_ask = P_min + ε_i，系统性高于近期成交价 P_rec 的 15-25% 区间对应 λ=2.0 且 ε_i 取正向 1σ。

## Corrected Claim

演化定向压力投影1：损失厌恶系数 λ 使得卖家心理保留价 P_min = V_true + λ·(V_true - P_market)，其中 λ ∈ [1.5, 2.5]（Kahneman & Tversky 经典值），导致挂价 P_ask = P_min + ε_i，系统性高于近期成交价 P_rec；在典型市场条件下，这种系统性溢价常表现为 15-25% 的区间，但这取决于具体的市场波动率 ε_i 分布及 V_true 与 P_market 的相对关系，而非仅由 λ=2.0 单一决定。

## Evidence

[质询]该陈述将行为经济学中的心理参数（λ）与具体的市场统计现象（15-25%溢价）强行绑定，声称特定参数组合（λ=2.0, ε=1σ）必然导致该特定区间，缺乏严谨的数学推导或实证数据支持，属于过度简化的因果归因。 | 先验知识/题面给定，逻辑校验通过：公式结构符合前景理论基本框架，量级在合理范围内，但具体数值映射（15-25%对应λ=2.0）缺乏直接来源支持且推导链条不完整，故降级。

## Search Query

loss aversion coefficient lambda used goods pricing behavior
