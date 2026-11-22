# N335: 流动性风险折价系数 β_liquidity 的估计方法：通过回归 P_ask = α + β_1*P_min + β_2*(P_ref - P_min) + β

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N110, N111, N112

## Claim

流动性风险折价系数 β_liquidity 的估计方法：通过回归 P_ask = α + β_1*P_min + β_2*(P_ref - P_min) + β_3*β_liquidity + ε 估计，其中 β_liquidity 与卖家历史成交周期 T_cycle 负相关，若 T_cycle > 30 天则 β_liquidity 典型值为 0.4-0.6，需验证具体平台数据。

## Corrected Claim

流动性风险折价系数 β_liquidity 的估计方法：通过回归 P_ask = α + β_1*P_min + β_2*(P_ref - P_min) + β_3*β_liquidity + ε 估计，其中 β_liquidity 与卖家历史成交周期 T_cycle 负相关。具体数值范围（如 T_cycle > 30 天时的典型值）需根据具体平台数据进行实证验证，不宜直接断定为 0.4-0.6。

## Evidence

[质询]该陈述包含具体的经验性数值范围（T_cycle > 30天时β_liquidity为0.4-0.6）和特定的回归模型设定，属于金融/市场微观结构领域的经验事实，无法从第一性原理或数学公理直接推导得出，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

liquidity risk discount coefficient seller pricing behavior used goods platform
