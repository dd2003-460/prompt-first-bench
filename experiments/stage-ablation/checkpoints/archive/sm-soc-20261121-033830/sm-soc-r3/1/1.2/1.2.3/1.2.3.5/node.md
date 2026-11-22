# N137: 代理变量预测误差 $\epsilon_{proxy}$：买家利用价格 $P$ 和信誉 $R$ 推断质量 $Q$ 的残差平方和，$\epsilon_{proxy}

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40, N41, N42

## Claim

代理变量预测误差 $\epsilon_{proxy}$：买家利用价格 $P$ 和信誉 $R$ 推断质量 $Q$ 的残差平方和，$\epsilon_{proxy} = E[(Q_{true} - \hat{Q}(P, R))^2]$；需验证在 $P_{premium}$ 区间内，该误差是否显著高于正常定价区间，从而解释为何高溢价伴随高不确定性。

## Corrected Claim

代理变量预测误差 $\epsilon_{proxy}$ 定义为 $E[(Q_{true} - \hat{Q}(P, R))^2]$。在 $P_{premium}$ 区间内，该误差是否显著高于正常定价区间需通过实证数据验证，以解释高溢价与高不确定性的潜在关联。

## Evidence

[质询]该陈述将‘高溢价伴随高不确定性’归因于代理变量预测误差（残差平方和）显著升高，但这属于经验性假设而非逻辑必然。高溢价可能源于品牌忠诚、稀缺性或信息不对称导致的逆向选择，而非单纯因为基于价格和信誉推断质量的统计误差变大。此外，‘显著高于’是一个需要实证数据支持的统计结论，无法从定义中直接推导。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该结论为经验性假设，非第一性原理可推导）

## Search Query

price as quality signal prediction error second hand marketplace proxy variables
