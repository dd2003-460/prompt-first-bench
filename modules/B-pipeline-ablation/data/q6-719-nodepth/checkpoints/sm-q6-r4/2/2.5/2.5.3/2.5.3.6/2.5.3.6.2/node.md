# N627: 增加 POP 的边际成本 N_add * C_pop_marginal 中，C_pop_marginal 的固定部分包括机柜租金、基础电力及静态带宽租赁，变动部

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N207

## Claim

增加 POP 的边际成本 N_add * C_pop_marginal 中，C_pop_marginal 的固定部分包括机柜租金、基础电力及静态带宽租赁，变动部分包括运维人力分摊；具体拆解为 C_pop_marginal = C_rent_pop + C_power_base + C_bw_static + (C_eng_total / N_pop_total)，其中 C_rent_pop ≈ ¥1500/月，C_bw_static ≈ ¥5000/月 (10Gbps 基础包)。

## Corrected Claim

增加 POP 的边际成本 N_add * C_pop_marginal 中，C_pop_marginal 的固定部分包括机柜租金、基础电力及静态带宽租赁，变动部分包括运维人力分摊；具体拆解为 C_pop_marginal = C_rent_pop + C_power_base + C_bw_static + (C_eng_total / N_pop_total)，其中 C_rent_pop ≈ ¥1500/月，C_bw_static ≈ ¥5000/月 (10Gbps 基础包)。

## Evidence

先验知识/题面给定，逻辑校验通过：成本拆解公式结构合理，机柜租金与静态带宽的量级符合行业常见经验值（knowledge 节点不适用经验事实排除条款）。

## Search Query

edge POP point marginal cost breakdown rent power bandwidth
