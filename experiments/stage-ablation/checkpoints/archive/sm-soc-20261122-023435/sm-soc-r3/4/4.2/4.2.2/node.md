# N53: N16机制下卖家最优降价触发时间 t* 的计算：t* = argmin_t [C_delay(t) + C_w(t) - E[Margin|t]]，其中 C_d

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

N16机制下卖家最优降价触发时间 t* 的计算：t* = argmin_t [C_delay(t) + C_w(t) - E[Margin|t]]，其中 C_delay(t) = α * t * GMV_base，C_w(t) 继承自 N10 (r*P_ref*t + D(t))，E[Margin|t] 随 t 增加因买家价格敏感度 ε_b 而下降。

## Corrected Claim

N16机制下卖家最优降价触发时间 t* 的计算：t* = argmin_t [C_delay(t) + C_w(t) - E[Margin|t]]，其中 C_delay(t) = α * t * GMV_base，C_w(t) 继承自 N10 (r*P_ref*t + D(t))，E[Margin|t] 随 t 增加因买家价格敏感度 ε_b 而下降。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seller optimal price adjustment timing cost of delay opportunity cost margin decay
