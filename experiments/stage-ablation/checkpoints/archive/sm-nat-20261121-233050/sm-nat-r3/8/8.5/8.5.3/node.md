# N175: P(T_update < T_res_i) 的精确值：T_update 服从指数分布，参数 u=0.01/day，T_res_i 基于 N64 公式计算。对于头

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N68

## Claim

P(T_update < T_res_i) 的精确值：T_update 服从指数分布，参数 u=0.01/day，T_res_i 基于 N64 公式计算。对于头部对象（rank < 1000），T_res_i 极大（>100天），P ≈ 1；对于尾部对象（rank > 50000），T_res_i 较小（<1天），P ≈ 0.01。需按热度分层加权平均。

## Corrected Claim

P(T_update < T_res_i) 的精确值：T_update 服从指数分布，参数 u=0.01/day，T_res_i 基于 N64 公式计算。对于头部对象（rank < 1000），T_res_i 极大（>100天），P ≈ 1；对于尾部对象（rank > 50000），T_res_i 较小（<1天），P ≈ 0.01。需按热度分层加权平均。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布性质及基于N64公式的推导在逻辑上自洽，数值量级符合直觉（头部对象更新概率高，尾部低）。
