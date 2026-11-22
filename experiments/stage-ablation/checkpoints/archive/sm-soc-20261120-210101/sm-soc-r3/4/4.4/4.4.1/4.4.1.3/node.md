# N294: GMV_0 的品类聚合粒度存在 trade-off：若按一级品类（如‘服装’）聚合，样本量大，GMV_0 稳定但掩盖子品类差异；若按三级 SKU 聚合，GMV_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82, N83, N84

## Claim

GMV_0 的品类聚合粒度存在 trade-off：若按一级品类（如‘服装’）聚合，样本量大，GMV_0 稳定但掩盖子品类差异；若按三级 SKU 聚合，GMV_0 精确但噪声大。前沿工作点3：采用二级品类（如‘女装-连衣裙’）聚合，平衡稳定性与精度。量化：二级品类 GMV_0 的系数变异 CV 通常比一级低 15%，比三级高 20%。

## Corrected Claim

GMV_0 的品类聚合粒度存在 trade-off：若按一级品类聚合，样本量大，GMV_0 稳定但掩盖子品类差异；若按三级 SKU 聚合，GMV_0 精确但噪声大。前沿工作点3：采用二级品类（如‘女装-连衣裙’）聚合，平衡稳定性与精度。

## Evidence

[质询]量化数值（CV低15%、高20%）缺乏普遍适用的理论依据或实证支持，属于特定数据集下的经验统计结果，不同品类结构下差异可能极大，无法作为通用事实。 | 先验知识/题面给定，逻辑校验通过（粒度越细噪声越大、聚合越粗偏差越大的trade-off逻辑自洽），但具体量化数值缺乏来源支持且非第一性原理可推导，故降级。

## Search Query

category level aggregation impact on GMV baseline stability e-commerce
