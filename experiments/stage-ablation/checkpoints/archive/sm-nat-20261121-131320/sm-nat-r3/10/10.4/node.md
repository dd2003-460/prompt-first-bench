# N155: 通过实际 CDN 日志验证相关性结构的量化指标为 Spearman 秩相关系数 ρ_s 与 Kendall τ_b 的差异；若 |ρ_s - τ_b| > 0.

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

通过实际 CDN 日志验证相关性结构的量化指标为 Spearman 秩相关系数 ρ_s 与 Kendall τ_b 的差异；若 |ρ_s - τ_b| > 0.05，表明存在非线性尾部依赖，Gaussian Copula 假设失效，需切换至 Clayton Copula 并重新估算 K_ρ。

## Corrected Claim

通过实际 CDN 日志验证相关性结构时，可计算 Spearman 秩相关系数 ρ_s 与 Kendall τ_b 的差异；若两者差异显著（如超过经验阈值），表明数据存在非线性尾部依赖，Gaussian Copula 假设可能不适用，需考虑切换至更合适的 Copula（如 Clayton 或 Gumbel）并重新估算参数。

## Evidence

[质询]阈值 0.05 为经验性启发式规则，缺乏普适的统计显著性标准或理论推导支持；且 Spearman 与 Kendall 系数的差异主要反映分布的非线性或尾部依赖特征，但直接将其作为 Gaussian Copula 失效并强制切换至 Clayton Copula 的唯一判据在逻辑上过于绝对，忽略了其他 Copula 类型（如 Gumbel）的可能性。 | 先验知识/题面给定，逻辑校验通过：Spearman 和 Kendall 均为秩相关系数，量纲一致，差异可反映非线性依赖；但具体阈值 0.05 及特定 Copula 切换策略属于经验性工程规则，非第一性原理可严格推导，故降级为定性表述。
