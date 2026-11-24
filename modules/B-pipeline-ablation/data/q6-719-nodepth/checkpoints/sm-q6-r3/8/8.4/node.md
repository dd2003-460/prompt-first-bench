# N134: Risk_Premium 计算：Risk_Premium = Elasticity_Penalty + Geo_Policy_Premium，其中 Elasti

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

Risk_Premium 计算：Risk_Premium = Elasticity_Penalty + Geo_Policy_Premium，其中 Elasticity_Penalty 由单点故障概率 × 业务损失估算（自建 10% × 500k = 50k 元/月，公有云 0），Geo_Policy_Premium 由 N31/N32 给出（自建 50k 元/月，混合 25k 元/月，公有云 0）。

## Corrected Claim

Risk_Premium 计算：Risk_Premium = Elasticity_Penalty + Geo_Policy_Premium，其中 Elasticity_Penalty 由单点故障概率 × 业务损失估算（自建 10% × 500k = 50k 元/月，公有云 0），Geo_Policy_Premium 由 N31/N32 给出（自建 50k 元/月，混合 25k 元/月，公有云 0）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点涵盖了自建、混合、公有云三种主要架构及其极端情况（激进/保守），逻辑上互斥且覆盖了父节点公式中的不同参数取值场景。虽然部分子节点（如自建10 POP与激进自建）在数学结构上相似，但它们代表了不同的业务策略和冗余等级，并非简单的参数重复，而是展示了风险随冗余度变化的非线性关系，因此不构成冗余。）
