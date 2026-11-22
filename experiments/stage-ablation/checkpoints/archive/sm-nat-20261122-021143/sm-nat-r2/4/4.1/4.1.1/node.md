# N42: T_avg 公式中 R 的定义：R 为缓存内对象的总请求率（requests/day），需从 N7 的热度分布和 N10 的 K 值计算：R = Σ_{k=1}

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

T_avg 公式中 R 的定义：R 为缓存内对象的总请求率（requests/day），需从 N7 的热度分布和 N10 的 K 值计算：R = Σ_{k=1}^{K} R_k

## Corrected Claim

T_avg 公式中 R 的定义：R 为缓存内对象的总请求率（requests/day），需从 N7 的热度分布和 N10 的 K 值计算：R = Σ_{k=1}^{K} R_k

## Evidence

先验知识/题面给定，逻辑校验通过：总请求率定义为各对象请求率之和，量纲与定义自洽。
