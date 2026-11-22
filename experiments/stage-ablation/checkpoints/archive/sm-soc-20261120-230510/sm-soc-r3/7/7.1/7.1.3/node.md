# N284: 权重比对高挂价商品优先级的非线性影响：高挂价商品通常具有 CTR_high > CTR_median 但 CVR_high < CVR_median，其排序分数

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N97

## Claim

权重比对高挂价商品优先级的非线性影响：高挂价商品通常具有 CTR_high > CTR_median 但 CVR_high < CVR_median，其排序分数 S = w_ctr * CTR + w_cvr * CVR；当 w_ctr/w_cvr > 2.0 时，S_high > S_median 的概率 > 60%；当 w_ctr/w_cvr < 1.5 时，S_high < S_median 的概率 > 70%，需通过模拟数据验证该阈值

## Corrected Claim

权重比对高挂价商品优先级的非线性影响：高挂价商品通常具有 CTR_high > CTR_median 但 CVR_high < CVR_median，其排序分数 S = w_ctr * CTR + w_cvr * CVR；权重比 w_ctr/w_cvr 的变化会显著改变高挂价商品相对于中位商品的排序优势，具体阈值（如 w_ctr/w_cvr 在 1.5-2.0 区间）对排序概率的影响需通过特定数据集的模拟验证来确定。

## Evidence

[质询]该陈述包含具体的经验性阈值（w_ctr/w_cvr > 2.0 对应 >60% 概率，< 1.5 对应 >70% 概率），这些数值并非数学公理或第一性原理可严格推导的必然结果，而是依赖于具体的数据分布（CTR/CVR 的方差、相关性等）。在缺乏具体数据集或模拟实验数据支持的情况下，断言这些特定阈值下的概率分布属于未经证实的经验假设，存在将特定场景下的模拟结果泛化为普遍规律的风险。 | 先验知识/题面给定，逻辑校验通过（量纲一致，排序分数公式合理），但具体概率阈值属于经验事实，缺乏外部来源直接支持或第一性原理严格推导，故降级。
