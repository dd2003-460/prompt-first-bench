# N254: 在流量饱和模型中，当曝光量超过买家搜索列表的可视阈值（如Top-10）时，λ_flow 趋近于0，导致曝光减半对成交概率的边际影响小于0.5，具体饱和点需通过平

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

在流量饱和模型中，当曝光量超过买家搜索列表的可视阈值（如Top-10）时，λ_flow 趋近于0，导致曝光减半对成交概率的边际影响小于0.5，具体饱和点需通过平台搜索日志中的位置-点击率（Position-CTR）曲线确定。

## Corrected Claim

在流量饱和模型中，当曝光量超过买家搜索列表的可视阈值（如Top-10）时，λ_flow 趋近于0，导致曝光减半对成交概率的边际影响小于0.5，具体饱和点需通过平台搜索日志中的位置-点击率（Position-CTR）曲线确定。

## Evidence

先验知识/题面给定，逻辑校验通过：流量饱和模型中，曝光量超过可视阈值后，边际效用递减符合经济学直觉，λ_flow趋近于0导致边际影响小于0.5在逻辑上自洽，且饱和点需通过Position-CTR曲线确定符合数据驱动建模的常规做法。

## Search Query

search engine result page position bias CTR decay curve saturation point
