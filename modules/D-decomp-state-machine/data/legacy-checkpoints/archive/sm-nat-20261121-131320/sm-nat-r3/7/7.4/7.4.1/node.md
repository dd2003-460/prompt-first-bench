# N143: Gaussian Copula 与 Clayton Copula 在 ρ=-0.3 下对 K_ρ 的预测差异量化：ΔK_ρ = |K_ρ,Clayton - K

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

Gaussian Copula 与 Clayton Copula 在 ρ=-0.3 下对 K_ρ 的预测差异量化：ΔK_ρ = |K_ρ,Clayton - K_ρ,Gaussian| / K_ρ,Gaussian；由于 Clayton 具有下尾依赖性，当 ρ 为负时，Clayton 预测的 K_ρ 通常比 Gaussian 高 3-8%，该差异是否超过 5% 的阈值需通过蒙特卡洛模拟 10,000 次样本验证。

## Corrected Claim

Gaussian Copula 与 Clayton Copula 在负相关（如 ρ=-0.3）下对 K_ρ 的预测存在差异，由于 Clayton 具有下尾依赖性，其预测值通常高于 Gaussian；具体差异幅度（如是否超过 5%）需通过蒙特卡洛模拟验证，而非直接断定为 3-8%。

## Evidence

[质询]该陈述包含具体的经验性数值范围（3-8%）和特定的统计结论，属于经验事实而非第一性原理可推导的数学恒等式；且未提供具体的参数映射关系（如 Clayton 参数 theta 与 Spearman 相关系数 rho 的对应关系），导致无法仅凭逻辑验证该具体数值区间的准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体百分比差异无法从第一性原理严格推出）

## Search Query

Gaussian vs Clayton copula tail dependence impact on cache hit rate simulation
