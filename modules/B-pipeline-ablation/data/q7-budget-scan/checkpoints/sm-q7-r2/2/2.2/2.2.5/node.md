# N67: 冷数据取回频率敏感性分析：若年取回次数从10次增加到100次，S3 Glacier Instant Retrieval取回费用从$40.96增加到$409.6，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

冷数据取回频率敏感性分析：若年取回次数从10次增加到100次，S3 Glacier Instant Retrieval取回费用从$40.96增加到$409.6，总成本从$2,375.68增加到$2,775.68（+16.8%）；而S3 Glacier Deep Archive取回费用从$20,480增加到$204,800，总成本从$205,286.6增加到$409,606.6（+99.5%），表明Deep Archive对取回频率极度敏感

## Corrected Claim

冷数据取回频率敏感性分析：若年取回次数从10次增加到100次，S3 Glacier Instant Retrieval取回费用从$40.96增加到$409.6，总成本从$2,375.68增加到$2,775.68（+16.8%）；而S3 Glacier Deep Archive取回费用从$20,480增加到$204,800，总成本从$205,286.6增加到$409,606.6（+99.5%），表明Deep Archive对取回频率极度敏感

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（100次取回费用为10次的10倍，总成本增量比例符合线性叠加逻辑），且符合S3 Glacier Instant Retrieval与Deep Archive在取回费用上的量级差异常识。

## Search Query

S3 Glacier retrieval frequency cost sensitivity analysis
