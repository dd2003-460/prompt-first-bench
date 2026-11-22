# N176: 阈值不等式中的成本项 (C_search + C_consult) 的联合分布：由于 C_search 和 C_consult 均受买家个体差异影响，两者之和的

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

阈值不等式中的成本项 (C_search + C_consult) 的联合分布：由于 C_search 和 C_consult 均受买家个体差异影响，两者之和的方差 Var(C_total) 不为零；在典型二手交易场景中，C_total 的 90 分位数约为商品标价的 3-5%，需利用该分布计算满足 C_total > (V_buyer - P_ask') 的买家占比，以量化'60%无咨询'现象的统计显著性。

## Corrected Claim

阈值不等式中的成本项 (C_search + C_consult) 的联合分布：由于 C_search 和 C_consult 均受买家个体差异影响，两者之和的方差 Var(C_total) 不为零；在典型二手交易场景中，C_total 通常占商品标价的一定比例（具体数值需依据特定平台数据确定），需利用该分布计算满足 C_total > (V_buyer - P_ask') 的买家占比，以量化'60%无咨询'现象的统计显著性。

## Evidence

[质询]「C_total 的 90 分位数约为商品标价的 3-5%」属于具体的经验统计参数，缺乏普遍适用的理论推导基础，且不同二手交易平台（如闲鱼、eBay、Craigslist）的咨询成本结构差异巨大，该数值范围可能因场景而异，存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过；但具体数值（3-5%）为经验事实，无来源支持，故降级。

## Search Query

consumer search cost consultation cost distribution used goods transaction
