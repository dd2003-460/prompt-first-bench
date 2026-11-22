# N82: 若使用 Spearman 相关 ρ_S=-0.3 而非 Pearson ρ_P=-0.3，LRU 的字节命中率估算误差约为 ±3%，因为尾部相关性被低估，导致对

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

若使用 Spearman 相关 ρ_S=-0.3 而非 Pearson ρ_P=-0.3，LRU 的字节命中率估算误差约为 ±3%，因为尾部相关性被低估，导致对高热度小对象的保留率预测偏低。

## Corrected Claim

若使用 Spearman 相关 ρ_S=-0.3 而非 Pearson ρ_P=-0.3，由于两者对尾部相关性的捕捉能力不同，LRU 的字节命中率估算会产生一定误差，具体幅度取决于数据分布特征。

## Evidence

[质询]该陈述包含具体的经验性数值（±3%误差）和特定的因果机制（尾部相关性低估导致保留率预测偏低），这属于经验事实而非第一性原理可推导的数学性质。虽然Spearman和Pearson在尾部相关性上确实存在差异，但具体的误差幅度（±3%）高度依赖于数据分布、对象大小分布及LRU缓存的具体参数，无法仅凭逻辑自洽确定，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持
