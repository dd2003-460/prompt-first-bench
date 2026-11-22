# N27: 对于负相关系数 ρ=-0.3 的联合分布，使用 Clayton Copula 或 Gaussian Copula 进行建模时，需计算条件概率 P(size > 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对于负相关系数 ρ=-0.3 的联合分布，使用 Clayton Copula 或 Gaussian Copula 进行建模时，需计算条件概率 P(size > s | freq > f)，以量化热门小对象在缓存中的实际占比，进而修正 LRU 缓存集合的期望字节覆盖率。

## Corrected Claim

对于负相关系数 ρ=-0.3 的联合分布，使用 Gaussian Copula 或 Frank/Gumbel Copula（或旋转 Clayton）进行建模时，需计算条件概率 P(size > s | freq > f)，以量化热门小对象在缓存中的实际占比，进而修正 LRU 缓存集合的期望字节覆盖率。

## Evidence

[质询]Clayton Copula 通常用于建模正相关（ρ > 0），其参数范围限制使其无法直接表示负相关（ρ = -0.3）；对于负相关，通常使用 Gumbel 或 Frank Copula，或者使用 Gaussian Copula。陈述中建议对负相关使用 Clayton Copula 存在技术上的不准确性或需特殊处理（如旋转 Copula），直接陈述易误导。 | 来源[1]仅介绍 Copula 基础概念，未涉及具体负相关建模或缓存覆盖率计算，属间接/无关支持；逻辑上条件概率计算框架自洽，但 Clayton 对负相关的适用性存疑，故降级。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/138800469&rut=00eca177cc2c121a12d6b8a207c8791f6153fedfd64f708d9f005791ad1316cf', 'type': 'ddg', 'title': 'Copula系列（一）-什么是Copula函数 - 知乎'}
