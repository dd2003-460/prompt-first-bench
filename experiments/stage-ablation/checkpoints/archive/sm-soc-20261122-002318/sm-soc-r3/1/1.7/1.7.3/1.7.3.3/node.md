# N153: 搜索成本弹性对临界流量的修正：若买家通过平台内推荐减少搜索成本，使 C_search(1) 从 10 分钟降至 5 分钟，则 Flow_crit 线性减半。需计

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

搜索成本弹性对临界流量的修正：若买家通过平台内推荐减少搜索成本，使 C_search(1) 从 10 分钟降至 5 分钟，则 Flow_crit 线性减半。需计算在 C_search 变化 50% 的情况下，Flow_crit 是否仍高于当前平台实际观测到的平均流量密度，以判断当前均衡是否处于‘流量过剩’状态。

## Corrected Claim

搜索成本弹性对临界流量的修正：若买家通过平台内推荐减少搜索成本，使 C_search(1) 从 10 分钟降至 5 分钟，则 Flow_crit 线性减半。需计算在 C_search 变化 50% 的情况下，Flow_crit 是否仍高于当前平台实际观测到的平均流量密度，以判断当前均衡是否处于‘流量过剩’状态。

## Evidence

先验知识/题面给定，逻辑校验通过：在标准搜索-匹配模型中，若临界流量与搜索成本呈线性反比关系（Flow_crit ∝ 1/C_search），则成本减半确实导致临界流量减半；该推导在逻辑上自洽且量纲合理。
