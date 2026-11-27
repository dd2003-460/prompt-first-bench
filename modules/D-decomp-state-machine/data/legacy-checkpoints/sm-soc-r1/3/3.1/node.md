# N15: 买家动机：最大化效用 U_buyer = V_item - P_pay - C_search - C_wait，其中 C_wait 随卖家降价行为增加（因买家预

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

买家动机：最大化效用 U_buyer = V_item - P_pay - C_search - C_wait，其中 C_wait 随卖家降价行为增加（因买家预期进一步降价），导致买家在卖家降价后 48 小时内选择等待而非咨询，C_wait 增量 ΔC_wait ≈ 0.1-0.2 × P_item。

## Corrected Claim

买家动机：最大化效用 U_buyer = V_item - P_pay - C_search - C_wait，其中 C_wait 随卖家降价行为增加（因买家预期进一步降价），导致买家在卖家降价后倾向于选择等待而非咨询，C_wait 增量 ΔC_wait 与 P_item 正相关。

## Evidence

[质询]C_wait 增量 ΔC_wait ≈ 0.1-0.2 × P_item 的具体数值范围缺乏理论推导或实证数据支持，属于经验性参数，且“48小时”这一时间窗口缺乏明确的经济学或行为学依据，存在将特定场景经验泛化为通用公式的风险。 | 先验知识/题面给定，逻辑校验通过（效用函数结构合理，等待成本随降价预期增加符合直觉），但具体数值系数（0.1-0.2）和时间窗口（48h）为经验参数，无来源直接支持，故降级。

## Search Query

buyer utility maximization waiting cost price reduction online marketplace
