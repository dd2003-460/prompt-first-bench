# N94: 同类商品价格变异系数CV的计算公式：CV = σ_price / μ_price，其中σ_price为近30天该品类所有成交价格的样本标准差，μ_price为样

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

同类商品价格变异系数CV的计算公式：CV = σ_price / μ_price，其中σ_price为近30天该品类所有成交价格的样本标准差，μ_price为样本均值；该计算需剔除异常值（如价格>3σ或<1/3σ的成交记录）

## Corrected Claim

同类商品价格变异系数CV的计算公式：CV = σ_price / μ_price，其中σ_price为近30天该品类所有成交价格的样本标准差，μ_price为样本均值；该计算需剔除异常值（如价格>3σ或<1/3σ的成交记录）

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上是正交的（一个关注数据清洗/异常值处理，一个关注时间窗口选择），且不存在冗余。但是，分解不完备：父节点明确给出了CV的具体计算公式（CV = σ/μ）以及基础统计量的定义，而子节点仅讨论了两个特定的‘边界条件’或‘替代方案’（异常值剔除的鲁棒性替代、时间窗口的敏感性），完全缺失了对核心计算流程本身（即如何执行基础的标准差和均值计算、数据预处理的具体步骤）的分解。子节点更像是‘注意事项’而非对‘计算公式’这一主题的全面拆解。）

## Search Query

coefficient of variation price dispersion calculation method outlier exclusion
