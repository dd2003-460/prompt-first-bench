# N229: 成交周期 T_deal 对价格 P_deal 的偏导数 ∂T_deal/∂P 的数值估算：基于库存积压模型，假设 T_deal = T_base * (P_de

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

成交周期 T_deal 对价格 P_deal 的偏导数 ∂T_deal/∂P 的数值估算：基于库存积压模型，假设 T_deal = T_base * (P_deal/P_market)^η，计算 ∂T_deal/∂P = η * T_base / P_market，需确定弹性系数 η（如 2.0-3.0）及基准周期 T_base。

## Corrected Claim

成交周期 T_deal 对价格 P_deal 的偏导数 ∂T_deal/∂P 的数值估算：基于库存积压模型，假设 T_deal = T_base * (P_deal/P_market)^η，计算 ∂T_deal/∂P = η * T_base / P_market，需确定弹性系数 η（如 2.0-3.0）及基准周期 T_base。

## Evidence

先验知识/题面给定，逻辑校验通过：幂函数 T = T_base * (P/P_market)^η 对 P 求导，当 P=P_market 时，∂T/∂P = η * T_base / P_market，数学推导正确，量纲一致（时间/价格）。

## Search Query

time to sell price elasticity used goods inventory model
