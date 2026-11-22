# N130: 条件期望 E[s_i | r_i > r_threshold] 的解析表达式：在 Gaussian Copula 参数 ρ=-0.3 下，E[s_i | r_i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

条件期望 E[s_i | r_i > r_threshold] 的解析表达式：在 Gaussian Copula 参数 ρ=-0.3 下，E[s_i | r_i > r_threshold] = ∫_{r_threshold}^{∞} ∫_{s_min}^{s_max} s * f_{s|r}(s|r) * f_r(r) ds dr，其中 f_{s|r} 由 Copula 偏导数 ∂C(u,v)/∂u 给出，r_threshold 需由缓存容量 C=128GB 和对象大小分布反推确定。

## Corrected Claim

条件期望 E[s_i | r_i > r_threshold] 的解析表达式：在 Gaussian Copula 参数 ρ=-0.3 下，E[s_i | r_i > r_threshold] = ∫_{r_threshold}^{∞} ∫_{s_min}^{s_max} s * f_{s|r}(s|r) * f_r(r) ds dr，其中 f_{s|r} 由 Copula 偏导数 ∂C(u,v)/∂u 给出，r_threshold 需由缓存容量 C=128GB 和对象大小分布反推确定。

## Evidence

先验知识/题面给定，逻辑校验通过：条件期望的积分定义正确，Gaussian Copula 下条件密度由偏导数给出符合定义，阈值由容量反推符合逻辑。

## Search Query

Gaussian copula conditional expectation formula
