# N115: Lifespan_Hours 的设定需基于硬件保修期和实际使用寿命；消费级显卡保修期通常 2-3 年，数据中心卡 3-5 年；假设 3 年生命周期，每天使用 8

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

Lifespan_Hours 的设定需基于硬件保修期和实际使用寿命；消费级显卡保修期通常 2-3 年，数据中心卡 3-5 年；假设 3 年生命周期，每天使用 8 小时，则 Lifespan_Hours = 3*365*8 = 8760 小时；若每天使用 24 小时，则 Lifespan_Hours = 26280 小时，电力成本占比随利用率增加而上升。

## Corrected Claim

Lifespan_Hours 的设定需基于硬件保修期和实际使用寿命；消费级显卡保修期通常 2-3 年，数据中心卡 3-5 年；假设 3 年生命周期，每天使用 8 小时，则 Lifespan_Hours = 3*365*8 = 8760 小时；若每天使用 24 小时，则 Lifespan_Hours = 26280 小时，电力成本占比随利用率增加而上升。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（3*365*8=8760, 3*365*24=26280），硬件保修期范围符合行业常识，逻辑自洽。
