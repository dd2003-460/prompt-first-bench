# N245: 投影3-买家搜索成本噪声：α 导致搜索结果列表中的价格离散度 Var(P_display) 增加，Var(P_display) = Var(P_true) + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N72

## Claim

投影3-买家搜索成本噪声：α 导致搜索结果列表中的价格离散度 Var(P_display) 增加，Var(P_display) = Var(P_true) + σ_α²，其中 σ_α² 为算法偏差引入的价格方差。买家搜索成本 C_search ∝ sqrt(Var(P_display))，因此 α 的存在使买家感知到的搜索成本系统性偏高，降低了其对高挂价的敏感度。

## Corrected Claim

投影3-买家搜索成本噪声：α 导致搜索结果列表中的价格离散度 Var(P_display) 增加，Var(P_display) = Var(P_true) + σ_α²，其中 σ_α² 为算法偏差引入的价格方差。买家搜索成本 C_search ∝ sqrt(Var(P_display))，因此 α 的存在使买家感知到的搜索成本系统性偏高，降低了其对高挂价的敏感度。

## Evidence

先验知识/题面给定，逻辑校验通过：方差分解公式 Var(P_display) = Var(P_true) + σ_α² 符合独立噪声叠加的统计学原理；搜索成本与价格离散度（标准差）的正相关关系符合信息经济学中搜索成本随不确定性增加而上升的基本直觉，且量纲与逻辑自洽。

## Search Query

search cost impact of price variance in search results
