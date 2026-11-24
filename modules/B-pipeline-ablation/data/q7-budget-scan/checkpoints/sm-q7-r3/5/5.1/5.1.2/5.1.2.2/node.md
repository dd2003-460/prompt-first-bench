# N233: NVMe SSD 阵列每小时业务损失 L_hourly 的估算模型：L_hourly = (Revenue_per_hour_lost * Impact_fac

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

NVMe SSD 阵列每小时业务损失 L_hourly 的估算模型：L_hourly = (Revenue_per_hour_lost * Impact_factor) + (Support_ticket_cost_per_hour)；假设内部数据湖支撑 BI 分析，每小时停机导致 50 名分析师闲置（¥200/h/person）及 SLA 违约金，L_hourly ≈ ¥10,000 - ¥50,000/小时，取决于业务关键度。

## Corrected Claim

NVMe SSD 阵列每小时业务损失 L_hourly 的估算模型：L_hourly = (Revenue_per_hour_lost * Impact_factor) + (Support_ticket_cost_per_hour)；假设内部数据湖支撑 BI 分析，每小时停机导致 50 名分析师闲置（¥200/h/person）及 SLA 违约金，L_hourly ≈ ¥10,000 - ¥50,000/小时，取决于业务关键度。

## Evidence

先验知识/题面给定，逻辑校验通过：50名分析师×¥200/h=¥10,000/h，加上SLA违约金后达到¥10,000-¥50,000/h的量级符合商业常识与内部估算模型逻辑。

## Search Query

data lake downtime cost per hour business impact analysis
