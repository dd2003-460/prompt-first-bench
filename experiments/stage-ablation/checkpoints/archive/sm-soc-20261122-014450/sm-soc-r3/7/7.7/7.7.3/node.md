# N379: 时间维度修正：ΔR_seller 是瞬时流量指标，需转换为年化或月均收入变化 ΔR_annual。需引入高信号卖家的平均挂售周期 T_cycle (天) 和年活

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N121

## Claim

时间维度修正：ΔR_seller 是瞬时流量指标，需转换为年化或月均收入变化 ΔR_annual。需引入高信号卖家的平均挂售周期 T_cycle (天) 和年活跃天数 D_year，计算 ΔR_annual = ΔR_seller * (D_year / T_cycle)，以反映干预对卖家长期现金流的具体冲击。

## Corrected Claim

时间维度修正：ΔR_seller 是瞬时流量指标，需转换为年化或月均收入变化 ΔR_annual。需引入高信号卖家的平均挂售周期 T_cycle (天) 和年活跃天数 D_year，计算 ΔR_annual = ΔR_seller * (D_year / T_cycle)，以反映干预对卖家长期现金流的具体冲击。

## Evidence

先验知识/题面给定，逻辑校验通过：将瞬时流量指标转换为年化收入需乘以时间覆盖系数（年活跃天数/平均挂售周期），量纲与逻辑自洽。
