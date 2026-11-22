# N39: 买家容忍度阈值 θ 的基准量化：基于买家搜索成本 C_search 与咨询成本 C_consult 的权衡，θ 通常等于 (C_search + C_consu

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N8

## Claim

买家容忍度阈值 θ 的基准量化：基于买家搜索成本 C_search 与咨询成本 C_consult 的权衡，θ 通常等于 (C_search + C_consult) / σ 的倒数形式简化，经验值为 0.5-0.8，显著小于卖家溢价系数 k (≈0.32-0.5)，导致 P_ask > V + θ·σ 的商品被过滤。

## Corrected Claim

买家容忍度阈值 θ 与卖家溢价系数 k 的具体数值关系及计算公式因市场模型而异，不能简单断言 θ 显著小于 k 或固定为 0.5-0.8。

## Evidence

[质询]陈述中声称买家容忍度阈值 θ (0.5-0.8) 显著小于卖家溢价系数 k (0.32-0.5)，这在数值上存在明显矛盾（0.5-0.8 大于 0.32-0.5），且将具体的经验数值与特定的数学公式（(C_search + C_consult) / σ 的倒数）强行绑定，缺乏通用的理论或实证支持，属于高度特定且可能错误的经验参数组合。 | 逻辑校验发现内部数值矛盾：θ (0.5-0.8) 并不小于 k (0.32-0.5)，且该具体公式与数值组合缺乏通用理论依据，属于不可靠的经验断言。

## Search Query

buyer search cost consultation cost threshold used market
