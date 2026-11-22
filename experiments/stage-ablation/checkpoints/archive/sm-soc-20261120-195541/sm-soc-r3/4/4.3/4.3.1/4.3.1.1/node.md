# N141: CVR_post 的 95% 置信区间计算公式为 [N_consult_post/N_views_post - 1.96*sqrt(p_post(1-p_pos

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

CVR_post 的 95% 置信区间计算公式为 [N_consult_post/N_views_post - 1.96*sqrt(p_post(1-p_post)/N_views_post), N_consult_post/N_views_post + 1.96*sqrt(p_post(1-p_post)/N_views_post)]，其中 p_post 为降价后48小时内的样本转化率，N_views_post 为样本量。

## Corrected Claim

CVR_post 的 95% 置信区间计算公式为 [N_consult_post/N_views_post - 1.96*sqrt(p_post(1-p_post)/N_views_post), N_consult_post/N_views_post + 1.96*sqrt(p_post(1-p_post)/N_views_post)]，其中 p_post 为降价后48小时内的样本转化率，N_views_post 为样本量。

## Evidence

先验知识/题面给定，逻辑校验通过
