# N53: 声誉溢价 β_status 的边际衰减率：随着卖家历史交易次数 N_trans 增加，β_status 呈指数衰减 β_status(N) = β_0 * e^

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19, N20, N21

## Claim

声誉溢价 β_status 的边际衰减率：随着卖家历史交易次数 N_trans 增加，β_status 呈指数衰减 β_status(N) = β_0 * e^(-k*N_trans)，其中 k 为衰减系数。新卖家（N_trans < 5）的 β_status 显著高于老卖家（N_trans > 20），解释为何新卖家更倾向高挂价。

## Corrected Claim

随着卖家历史交易次数增加，声誉溢价通常呈现边际衰减趋势，新卖家可能因缺乏历史约束而更倾向高挂价，但具体的指数衰减系数及阈值需依据特定平台数据实证确定。

## Evidence

[质询]该陈述包含具体的数学函数形式（指数衰减）和特定的阈值（N_trans < 5, > 20），属于经验事实或特定模型假设，无法从第一性原理直接推导，且参考来源仅涉及声誉溢出效应，未提供该具体衰减公式及阈值的实证支持。 | 逻辑上指数衰减符合声誉积累边际效应递减的直觉，但参考来源[1]仅讨论声誉溢出，未直接支持具体的指数衰减公式及阈值设定，属于经验事实缺来源支持。

## Search Query

seller reputation accumulation pricing behavior online marketplace dynamic

## Retrieval Sources

- {'url': 'https://cnais.sem.tsinghua.edu.cn/info/1073/1772.htm&rut=a8b6ea9367e2c79e734378666d6022bb72a005a9c67f08778da541244c15eaca', 'type': 'ddg', 'title': '数字平台中代理商声誉对个人创作者声誉的溢出效应研究-中国系统工程学会信息系统工程专业委员会'}
