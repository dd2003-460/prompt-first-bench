# N172: 工作点B的静态电力成本计算：SSD功耗 100TB × 0.8W/TB = 80W，HDD功耗 400TB × 0.4W/TB = 160W，服务器基础功耗 5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

工作点B的静态电力成本计算：SSD功耗 100TB × 0.8W/TB = 80W，HDD功耗 400TB × 0.4W/TB = 160W，服务器基础功耗 50W，总IT功耗 290W = 0.29kW；年电费 = 0.29kW × 1.4(PUE) × 0.8(¥/kWh) × 8760h ≈ ¥2,844/年。

## Corrected Claim

工作点B的静态电力成本计算：SSD功耗 100TB × 0.8W/TB = 80W，HDD功耗 400TB × 0.4W/TB = 160W，服务器基础功耗 50W，总IT功耗 290W = 0.29kW；年电费 = 0.29kW × 1.4(PUE) × 0.8(¥/kWh) × 8760h ≈ ¥2,844/年。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（100*0.8+400*0.4+50=290W；290*1.4*0.8*8760/1000≈2843.9），单位换算与量级符合数据中心能耗常识。

## Search Query

enterprise nvme ssd power consumption per tb watt spec
