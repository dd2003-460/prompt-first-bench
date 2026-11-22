# N199: 共享随机源定义：GMV 的随机源为成交笔数 Q_i 与成交价 P_i 的联合波动；在均衡状态下，Q_i 与 P_i 存在负相关（ρ_QP < 0），导致 GMV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N61

## Claim

共享随机源定义：GMV 的随机源为成交笔数 Q_i 与成交价 P_i 的联合波动；在均衡状态下，Q_i 与 P_i 存在负相关（ρ_QP < 0），导致 GMV = Σ(P_i * Q_i) 的波动性低于单一价格或数量波动，共享随机源表现为成交量对价格冲击的滞后响应 T_lag。

## Corrected Claim

共享随机源定义：GMV 的随机源为成交笔数 Q_i 与成交价 P_i 的联合波动；在均衡状态下，Q_i 与 P_i 存在负相关（ρ_QP < 0），导致 GMV = Σ(P_i * Q_i) 的波动性低于单一价格或数量波动，共享随机源表现为成交量对价格冲击的滞后响应 T_lag。

## Evidence

先验知识/题面给定，逻辑校验通过：GMV作为乘积项，在Q与P负相关时波动性确实低于单一因子，且滞后响应符合市场微观结构常识。
