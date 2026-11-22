# N169: 在降价幅度 |ΔP|/P_ask > 15% 的深度折扣区间，P(Lemon | ΔP < 0) 可能回落至 0.3-0.4（因‘清仓’信号覆盖‘缺陷’信号），

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

在降价幅度 |ΔP|/P_ask > 15% 的深度折扣区间，P(Lemon | ΔP < 0) 可能回落至 0.3-0.4（因‘清仓’信号覆盖‘缺陷’信号），但此时买家支付意愿 W 需满足 W > P_ask * (1 - 0.15)，仅高支付意愿买家（W > μ_W + 2σ_W）会响应，导致成交量 Q 骤降但成交周期 T_cycle 可能缩短。

## Corrected Claim

在降价幅度 |ΔP|/P_ask > 15% 的深度折扣区间，P(Lemon | ΔP < 0) 可能回落至 0.3-0.4（因‘清仓’信号覆盖‘缺陷’信号），但此时买家支付意愿 W 需满足 W > P_ask * (1 - 0.15)，仅高支付意愿买家（W > μ_W + 2σ_W）会响应，导致成交量 Q 骤降但成交周期 T_cycle 可能缩短。

## Evidence

先验知识/题面给定，逻辑校验通过
