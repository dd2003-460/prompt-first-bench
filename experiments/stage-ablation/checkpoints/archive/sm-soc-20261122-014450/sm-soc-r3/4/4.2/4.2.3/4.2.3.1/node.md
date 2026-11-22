# N237: P_initial 的量化定义为卖家首次挂价 P_list_0，基准值 P_initial = 1.25 * P_market，基于 N9 中高挂价 15-25

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N75

## Claim

P_initial 的量化定义为卖家首次挂价 P_list_0，基准值 P_initial = 1.25 * P_market，基于 N9 中高挂价 15-25% 的上限，该值作为心理账户的参考点，需计算其与当前市场价 P_market 的绝对偏离量 ΔP_initial = 0.25 * P_market。

## Corrected Claim

P_initial 的量化定义为卖家首次挂价 P_list_0，基准值 P_initial = 1.25 * P_market，基于 N9 中高挂价 15-25% 的上限，该值作为心理账户的参考点，需计算其与当前市场价 P_market 的绝对偏离量 ΔP_initial = 0.25 * P_market。

## Evidence

先验知识/题面给定，逻辑校验通过：P_initial = 1.25 * P_market 与 ΔP_initial = 0.25 * P_market 在数学上严格自洽，且符合中高挂价15-25%上限的定义逻辑。
