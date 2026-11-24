# N84: 单次NVMe SSD加速恢复的硬件折旧摊销成本 = (额外SSD采购成本 * 加速频率) / 5年，若额外100TB SSD成本约¥300,000，年折旧¥60

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

单次NVMe SSD加速恢复的硬件折旧摊销成本 = (额外SSD采购成本 * 加速频率) / 5年，若额外100TB SSD成本约¥300,000，年折旧¥60,000，单次故障摊销取决于年均故障次数（MTBF倒数）

## Corrected Claim

单次NVMe SSD加速恢复的硬件折旧摊销成本 = (额外SSD采购成本 * 加速频率) / 5年，若额外100TB SSD成本约¥300,000，年折旧¥60,000，单次故障摊销取决于年均故障次数（MTBF倒数）

## Evidence

先验知识/题面给定，逻辑校验通过：100TB SSD成本30万符合当前企业级SSD市场量级（约3元/TB），5年直线折旧计算正确（30万/5=6万/年），单次摊销逻辑（年折旧/年均故障次数）符合会计摊销基本原理。
