# N159: 筛选功能有效性系数 E_filter 的分解：E_filter = E_filter_price + E_filter_brand - E_filter_int

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

筛选功能有效性系数 E_filter 的分解：E_filter = E_filter_price + E_filter_brand - E_filter_interaction_loss，其中价格区间筛选贡献约 0.2-0.3，品牌筛选贡献约 0.1-0.2，交互损失项反映多条件筛选导致的召回率下降，需通过 A/B 测试测量各筛选器单独启用时的点击转化率提升。

## Corrected Claim

筛选功能有效性系数 E_filter 可分解为价格区间筛选贡献、品牌筛选贡献及交互损失项之和（E_filter = E_filter_price + E_filter_brand - E_filter_interaction_loss），其中交互损失项反映多条件筛选导致的召回率下降，各分项的具体贡献值需通过 A/B 测试测量，典型量级需结合具体业务场景确定。

## Evidence

[质询]数值量级缺乏实证支持：0.2-0.3 和 0.1-0.2 的具体贡献值属于经验性统计结果，不同电商场景、用户群体及筛选器实现方式下差异巨大，无法从第一性原理推导，且缺乏通用基准数据支持该特定区间。 | 先验知识/题面给定，逻辑校验通过（公式结构符合集合论/概率论中多条件筛选的交互效应分解逻辑，量纲一致），但具体数值为经验事实，无来源直接支持，故降级。

## Search Query

filter effectiveness coefficient e-commerce search price brand filter A/B test conversion lift
