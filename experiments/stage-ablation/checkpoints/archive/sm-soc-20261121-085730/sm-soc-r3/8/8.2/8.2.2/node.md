# N387: 标签误报率 q_false_positive 的贝叶斯估计值：基于先验分布 Beta(α, β) 与观察到的误报样本数 k，后验均值 q_fp = (α + k

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N136

## Claim

标签误报率 q_false_positive 的贝叶斯估计值：基于先验分布 Beta(α, β) 与观察到的误报样本数 k，后验均值 q_fp = (α + k) / (α + β + N_test)，其中 N_test 为抽检样本量，需设定 α, β 先验参数（如 α=1, β=1）并执行假设检验。

## Corrected Claim

标签误报率 q_false_positive 的贝叶斯估计值：基于先验分布 Beta(α, β) 与观察到的误报样本数 k，后验均值 q_fp = (α + k) / (α + β + N_test)，其中 N_test 为抽检样本量，需设定 α, β 先验参数（如 α=1, β=1）并执行假设检验。

## Evidence

逻辑推导成立，来源未直接覆盖

## Search Query

false positive rate calculation for seller quality labels in online marketplaces
