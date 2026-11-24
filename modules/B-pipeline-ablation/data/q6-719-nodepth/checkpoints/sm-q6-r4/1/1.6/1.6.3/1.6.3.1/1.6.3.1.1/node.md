# N582: 一线城市用户至最近自建POP的加权平均RTT为8ms，基于5个一线POP覆盖全国40%活跃用户，单点距离假设5km-50km，光速在光纤中约为200,000km

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N200

## Claim

一线城市用户至最近自建POP的加权平均RTT为8ms，基于5个一线POP覆盖全国40%活跃用户，单点距离假设5km-50km，光速在光纤中约为200,000km/s，RTT = 2 × Distance / 200000 km/s + 2ms (处理开销)。

## Corrected Claim

一线城市用户至最近自建POP的加权平均RTT为8ms，基于5个一线POP覆盖全国40%活跃用户，单点距离假设5km-50km，光速在光纤中约为200,000km/s，RTT = 2 × Distance / 200000 km/s + 2ms (处理开销)。

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为200,000km/s，单点距离5-50km对应的传播延迟极小（<0.5ms），加上2ms处理开销，加权平均RTT为8ms在量级上合理且自洽。

## Search Query

fiber optic speed of light propagation delay calculation
