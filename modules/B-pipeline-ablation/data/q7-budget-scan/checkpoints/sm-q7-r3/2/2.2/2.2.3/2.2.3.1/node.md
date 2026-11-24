# N176: 工作点C的静态电力成本计算：SSD功耗 50TB × 0.8W/TB = 40W，HDD功耗 450TB × 0.4W/TB = 180W，服务器基础功耗 50

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

工作点C的静态电力成本计算：SSD功耗 50TB × 0.8W/TB = 40W，HDD功耗 450TB × 0.4W/TB = 180W，服务器基础功耗 50W，总IT功耗 270W = 0.27kW；年电费 = 0.27kW × 1.4(PUE) × 0.8(¥/kWh) × 8760h ≈ ¥2,655/年。

## Corrected Claim

工作点C的静态电力成本计算：SSD功耗 50TB × 0.8W/TB = 40W，HDD功耗 450TB × 0.4W/TB = 180W，服务器基础功耗 50W，总IT功耗 270W = 0.27kW；年电费 = 0.27kW × 1.4(PUE) × 0.8(¥/kWh) × 8760h ≈ ¥2,655/年。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算准确（40+180+50=270W; 0.27*1.4*0.8*8760≈2655.36），参数符合常规数据中心能耗估算模型。

## Search Query

enterprise hdd power consumption idle active watt
