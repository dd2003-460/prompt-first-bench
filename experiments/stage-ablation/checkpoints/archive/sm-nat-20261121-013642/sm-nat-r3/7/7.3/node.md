# N82: 在 ρ=-0.3 的负相关下，热门对象（freq 前 10%）的平均大小期望值 E[size | freq_top10] 相比整体平均 E[size] 降低约 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

在 ρ=-0.3 的负相关下，热门对象（freq 前 10%）的平均大小期望值 E[size | freq_top10] 相比整体平均 E[size] 降低约 15%-25%，具体数值需通过积分 ∫ s * c_θ(F_s(s), F_f(f)) ds df 计算

## Corrected Claim

在 ρ=-0.3 的负相关下，热门对象（freq 前 10%）的平均大小期望值 E[size | freq_top10] 相比整体平均 E[size] 会有所降低，具体降低幅度取决于Copula函数的具体形式及参数，需通过积分 ∫ s * c_θ(F_s(s), F_f(f)) ds df 计算得出。

## Evidence

[质询]具体数值范围（15%-25%）缺乏通用理论支持，高度依赖于具体的Copula函数类型（如Gaussian, Clayton等）及参数θ，仅凭ρ=-0.3无法唯一确定该区间，属于经验性估算而非严格推导。 | 逻辑上负相关确实导致高频对象平均大小低于整体平均，但具体百分比区间缺乏来源支持且依赖未指定的分布假设，属经验事实缺来源支持。

## Search Query

joint distribution conditional expectation negative correlation Pareto copula numerical integration
