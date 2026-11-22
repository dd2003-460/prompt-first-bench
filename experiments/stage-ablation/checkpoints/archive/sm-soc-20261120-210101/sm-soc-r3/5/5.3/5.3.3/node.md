# N99: 数据代表性偏差检验：计算'全量降价卖家'与'抽样降价卖家'在品类分布（χ²检验）、卖家信用分均值（t检验）、商品上架时长（Mann-Whitney U检验）上的

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

数据代表性偏差检验：计算'全量降价卖家'与'抽样降价卖家'在品类分布（χ²检验）、卖家信用分均值（t检验）、商品上架时长（Mann-Whitney U检验）上的差异；若任一检验p<0.05，则抽样数据存在显著偏差，置信度降级

## Corrected Claim

数据代表性偏差检验：计算'全量降价卖家'与'抽样降价卖家'在品类分布（χ²检验）、卖家信用分均值（t检验）、商品上架时长（Mann-Whitney U检验）上的差异；若任一检验p<0.05，则抽样数据存在显著偏差，置信度降级

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点中明确指定的三个独立维度（品类分布、卖家信用分、商品上架时长），各自采用了父节点指定的对应统计检验方法（χ²、t、Mann-Whitney U），并进一步补充了效应量指标以增强鲁棒性。各子节点关注的变量不同，逻辑上互斥且无重叠，不存在冗余或矛盾。）

## Search Query

sample representativeness chi-square test t-test seller credit score bias
