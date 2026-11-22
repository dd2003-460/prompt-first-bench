# N359: 筛选效应下高挂价组买家等待容忍度 ΔT_tolerance 的量化模型：T_tolerance = f(WTP, Patience, Search_Cost)。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

筛选效应下高挂价组买家等待容忍度 ΔT_tolerance 的量化模型：T_tolerance = f(WTP, Patience, Search_Cost)。在高挂价筛选后，剩余买家的平均 WTP 提高，但搜索成本 S_cost 也增加（因为匹配对象更少）。需建立方程 T_tolerance_high - T_tolerance_low = (∂T/∂WTP * ΔWTP) + (∂T/∂S * ΔS_cost)，其中 ∂T/∂WTP < 0（高估值者更急于成交），∂T/∂S > 0（高搜索成本增加等待时间）。需估计这两个偏导数的具体数值，以判断净效应是否为正（即 ΔT_tolerance > 0 是否成立）。

## Corrected Claim

筛选效应下高挂价组买家等待容忍度 ΔT_tolerance 的量化模型：T_tolerance = f(WTP, Patience, Search_Cost)。在高挂价筛选后，剩余买家的平均 WTP 提高，但搜索成本 S_cost 也增加（因为匹配对象更少）。需建立方程 T_tolerance_high - T_tolerance_low = (∂T/∂WTP * ΔWTP) + (∂T/∂S * ΔS_cost)，其中 ∂T/∂WTP < 0（高估值者更急于成交），∂T/∂S > 0（高搜索成本增加等待时间）。需估计这两个偏导数的具体数值，以判断净效应是否为正（即 ΔT_tolerance > 0 是否成立）。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述构建了一个基于微积分全微分近似（Total Differential）的量化模型框架，符号定义（∂T/∂WTP < 0, ∂T/∂S > 0）符合经济学直觉（高支付意愿者时间价值高，搜索成本高导致等待久），且明确指出了需估计偏导数以判断净效应，逻辑自洽且无内部矛盾。

## Search Query

buyer patience willingness to pay search cost trade-off in matching markets
