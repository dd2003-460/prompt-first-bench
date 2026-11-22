# N142: 判定 ΔCVR 是否显著的 Z 检验统计量公式为 Z = (CVR_post - CVR_pre) / sqrt(p_pool(1-p_pool)*(1/N_v

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

判定 ΔCVR 是否显著的 Z 检验统计量公式为 Z = (CVR_post - CVR_pre) / sqrt(p_pool(1-p_pool)*(1/N_views_post + 1/N_views_pre))，其中 p_pool 为合并样本率，若 |Z| < 1.96 则支持'买家非主动搜索'假设。

## Corrected Claim

判定 ΔCVR 是否显著的 Z 检验统计量公式为 Z = (CVR_post - CVR_pre) / sqrt(p_pool(1-p_pool)*(1/N_views_post + 1/N_views_pre))，其中 p_pool 为合并样本率，若 |Z| < 1.96 则支持'买家非主动搜索'假设。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合双样本比例Z检验标准形式，1.96对应95%置信水平，逻辑自洽。
