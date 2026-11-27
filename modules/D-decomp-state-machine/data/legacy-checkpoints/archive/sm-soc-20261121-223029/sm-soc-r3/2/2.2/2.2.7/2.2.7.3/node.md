# N188: 搜索成本 k 的异质性分析：区分高参与度买家（如收藏家）与低参与度买家（如普通用户）的 k 值差异。若高参与度买家 k_low ≈ 0.1，低参与度买家 k_h

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

搜索成本 k 的异质性分析：区分高参与度买家（如收藏家）与低参与度买家（如普通用户）的 k 值差异。若高参与度买家 k_low ≈ 0.1，低参与度买家 k_high ≈ 0.6，则需加权计算整体 C_inquiry，以解释为何 60% 的卖家（主要面向低参与度买家）遭遇无咨询。

## Corrected Claim

搜索成本 k 的异质性分析：高参与度买家（如收藏家）通常具有较低的搜索成本 k，而低参与度买家（如普通用户）具有较高的搜索成本 k。这种异质性导致面向低参与度买家的卖家面临更高的无咨询风险，需通过加权计算整体咨询成本来解释这一现象。

## Evidence

[质询]该陈述包含具体的经验参数（k_low ≈ 0.1, k_high ≈ 0.6）和统计结论（60%卖家遭遇无咨询），这些属于经验事实而非第一性原理可推导的数学性质。在缺乏外部来源支持的情况下，无法验证这些具体数值和比例是否准确，存在参数设定随意或与实际市场数据不符的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

heterogeneity in search cost sensitivity among consumer segments second-hand goods
