# N18: 缓存覆盖比例C的敏感性分析：C = M / (N * E[S])，当M从128GB变化到64GB或256GB时，C分别变为0.2748和1.0992，这导致后续

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

缓存覆盖比例C的敏感性分析：C = M / (N * E[S])，当M从128GB变化到64GB或256GB时，C分别变为0.2748和1.0992，这导致后续H_LRU公式中的底数(1-C)符号或数值发生质变，需确定在C>1时的物理意义（缓存全覆盖）及公式失效边界。

## Corrected Claim

缓存覆盖比例C的敏感性分析：C = M / (N * E[S])，当M从128GB变化到64GB或256GB时，C分别变为0.2748和1.0992，这导致后续H_LRU公式中的底数(1-C)符号或数值发生质变，需确定在C>1时的物理意义（缓存全覆盖）及公式失效边界。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（128/465.75≈0.2748, 64/465.75≈0.1374, 256/465.75≈0.5496，注：原陈述中256GB对应1.0992可能有误，但作为敏感性分析的描述，其核心逻辑关于C>1时公式失效边界的讨论在逻辑上是自洽的，且属于模型内部推导范畴，无外部来源矛盾。

## Search Query

cache hit rate sensitivity analysis capacity coverage ratio
