# N327: 公有云策略的边际成本 $MC_{cloud}(R)$ 定义为增加 1 个请求所需的额外流量费用，即 $MC_{cloud} = P_{traffic}^{eff

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N122

## Claim

公有云策略的边际成本 $MC_{cloud}(R)$ 定义为增加 1 个请求所需的额外流量费用，即 $MC_{cloud} = P_{traffic}^{eff} \times s_{avg}$，其中 $P_{traffic}^{eff}$ 为当前流量档位下的等效单价，$s_{avg}$ 为平均对象大小，需计算在 750 万日活场景下的具体数值。

## Corrected Claim

公有云策略的边际成本 $MC_{cloud}(R)$ 定义为增加 1 个请求所需的额外流量费用，即 $MC_{cloud} = P_{traffic}^{eff} \times s_{avg}$，其中 $P_{traffic}^{eff}$ 为当前流量档位下的等效单价，$s_{avg}$ 为平均对象大小，需计算在 750 万日活场景下的具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过：边际成本定义为增量成本，在流量单价恒定区间内，增加1个请求的边际成本确实等于等效单价乘以平均对象大小，量纲与逻辑自洽。
