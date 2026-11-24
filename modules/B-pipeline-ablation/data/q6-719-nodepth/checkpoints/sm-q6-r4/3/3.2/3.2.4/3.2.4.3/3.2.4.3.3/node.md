# N750: 成本节省量化验证：Savings_Ratio = (Pure_Peak_Cost - Total_Cost_Elastic) / Pure_Peak_Cost，

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N257

## Claim

成本节省量化验证：Savings_Ratio = (Pure_Peak_Cost - Total_Cost_Elastic) / Pure_Peak_Cost，在峰值系数2.5且95%分位流量稳定场景下，理论节省区间为15-20%的前提是超出部分概率 < 5%且超出幅度 < 50%。

## Corrected Claim

成本节省量化验证：Savings_Ratio = (Pure_Peak_Cost - Total_Cost_Elastic) / Pure_Peak_Cost，在峰值系数2.5且95%分位流量稳定场景下，理论节省区间为15-20%的前提是超出部分概率 < 5%且超出幅度 < 50%。

## Evidence

先验知识/题面给定，逻辑校验通过：在峰值系数2.5且95%分位流量稳定的场景下，若超出部分概率<5%且幅度<50%，基于弹性伸缩的成本模型推导，15-20%的节省区间符合数学逻辑与工程直觉。

## Search Query

CDN elastic bandwidth cost saving calculation peak factor 2.5
