# N302: 统一量化口径的选择标准：当 n*p < 10 或 n*(1-p) < 10 时，正态近似失效，必须使用精确二项分布或 Wilson 区间；H1 的 p=0.6,

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97, N98, N99

## Claim

统一量化口径的选择标准：当 n*p < 10 或 n*(1-p) < 10 时，正态近似失效，必须使用精确二项分布或 Wilson 区间；H1 的 p=0.6, n=1000 满足正态近似条件，但 N29 的宽区间暗示其可能采用了保守的 Bonferroni 校正或多重比较调整

## Corrected Claim

统一量化口径的选择标准：当 n*p < 10 或 n*(1-p) < 10 时，正态近似失效，必须使用精确二项分布或 Wilson 区间；H1 的 p=0.6, n=1000 满足正态近似条件，但 N29 的宽区间暗示其可能采用了保守的 Bonferroni 校正或多重比较调整

## Evidence

先验知识/题面给定，逻辑校验通过：n=1000, p=0.6 时 np=600, n(1-p)=400 均远大于 10，正态近似条件成立；关于 N29 的推测虽为假设，但作为对宽区间成因的合理归因（Bonferroni 校正确实会加宽区间），逻辑自洽且无内部矛盾。
