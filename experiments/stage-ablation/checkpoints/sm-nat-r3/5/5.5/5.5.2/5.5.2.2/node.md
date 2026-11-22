# N254: 集中更新工作点下的头部对象失效概率 P_invalid_head = 1 - exp(-λ_update_head * T_res_head)，其中 λ_upd

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

集中更新工作点下的头部对象失效概率 P_invalid_head = 1 - exp(-λ_update_head * T_res_head)，其中 λ_update_head = 0.1/天（假设1%总更新率集中在10%对象上），需代入 N104 计算的 T_res_head 得到具体概率值。

## Corrected Claim

集中更新工作点下的头部对象失效概率 P_invalid_head = 1 - exp(-λ_update_head * T_res_head)，其中 λ_update_head = 0.1/天（假设1%总更新率集中在10%对象上），需代入 N104 计算的 T_res_head 得到具体概率值。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松过程失效概率公式正确，参数推导（1%总更新率/10%对象=10%对象更新率，即0.1/天）符合逻辑。
