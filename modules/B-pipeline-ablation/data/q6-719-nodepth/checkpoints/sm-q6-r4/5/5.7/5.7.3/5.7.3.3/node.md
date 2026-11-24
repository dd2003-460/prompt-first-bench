# N487: 在最高可靠性/低故障率工作点下，N_pop=10 时 N_ops_self = ceil(10/2) = 5 人（1人管2个POP），S_ops 取高端 30万

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N159, N160, N161

## Claim

在最高可靠性/低故障率工作点下，N_pop=10 时 N_ops_self = ceil(10/2) = 5 人（1人管2个POP），S_ops 取高端 30万元/年，C_ops_self = 5 * 300000 / 12 = ¥125,000/月，分摊到 Q_day=2,048,000 请求后为 ¥61.04/1000 req

## Corrected Claim

在最高可靠性/低故障率工作点下，N_pop=10 时 N_ops_self = ceil(10/2) = 5 人（1人管2个POP），S_ops 取高端 30万元/年，C_ops_self = 5 * 300000 / 12 = ¥125,000/月，分摊到 Q_day=2,048,000 请求后为 ¥61.04/1000 req

## Evidence

先验知识/题面给定，逻辑校验通过：ceil(10/2)=5，5*300000/12=125000，125000/2048000*1000≈61.035，四舍五入为61.04，计算无误。
