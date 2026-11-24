# N485: 在最小化人力成本工作点下，N_pop=10 时 N_ops_self = ceil(10/4) = 3 人，S_ops 取低端 20万元/年，C_ops_sel

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N159, N160, N161

## Claim

在最小化人力成本工作点下，N_pop=10 时 N_ops_self = ceil(10/4) = 3 人，S_ops 取低端 20万元/年，C_ops_self = 3 * 200000 / 12 = ¥50,000/月，分摊到 Q_day=2,048,000 请求后为 ¥24.41/1000 req

## Corrected Claim

在最小化人力成本工作点下，N_pop=10 时 N_ops_self = ceil(10/4) = 3 人，S_ops 取低端 20万元/年，C_ops_self = 3 * 200000 / 12 = ¥50,000/月，分摊到 Q_day=2,048,000 请求后为 ¥24.41/1000 req

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 3 * 200000 / 12 = 50000，50000 / 2048000 * 1000 ≈ 24.41，数值与逻辑均自洽。
