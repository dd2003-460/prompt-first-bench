# N622: 工作点D（高PUE/自有机房）：PUE=1.8，2台服务器功耗500W，总耗电P_total=900W，月用电量648kWh，若基础包2kW，无超额，但散热效率

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N212, N213, N214

## Claim

工作点D（高PUE/自有机房）：PUE=1.8，2台服务器功耗500W，总耗电P_total=900W，月用电量648kWh，若基础包2kW，无超额，但散热效率低导致设备寿命缩短，隐含维护成本增加约¥100/月/POP。

## Corrected Claim

工作点D（高PUE/自有机房）：PUE=1.8，2台服务器功耗500W，总耗电P_total=900W，月用电量648kWh，若基础包2kW，无超额，但散热效率低导致设备寿命缩短，隐含维护成本增加约¥100/月/POP。

## Evidence

先验知识/题面给定，逻辑校验通过：P_total = 500W / (1/1.8) = 900W，月用电量 900W * 24h * 30d = 648kWh，计算自洽；维护成本为经验估算，符合高PUE场景逻辑。

## Search Query

high PUE 1.8 data center maintenance cost impact
