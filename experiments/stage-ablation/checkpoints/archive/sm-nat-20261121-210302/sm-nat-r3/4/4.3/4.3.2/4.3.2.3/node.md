# N134: 工作集字节大小 W_LRU_bytes 的积分表达式：W_LRU_bytes = ∫_{P_th}^{1} N * f_P(p) * E[S|P=p] dp，需

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

工作集字节大小 W_LRU_bytes 的积分表达式：W_LRU_bytes = ∫_{P_th}^{1} N * f_P(p) * E[S|P=p] dp，需结合 Pareto(β=0.9) 与 Pareto(α=1.1) 联合分布计算

## Corrected Claim

工作集字节大小 W_LRU_bytes 的积分表达式：W_LRU_bytes = ∫_{P_th}^{1} N * f_P(p) * E[S|P=p] dp，需结合 Pareto(β=0.9) 与 Pareto(α=1.1) 联合分布计算

## Evidence

先验知识/题面给定，逻辑校验通过
