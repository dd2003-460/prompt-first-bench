# N486: 在标准运维工作点下，N_pop=10 时 N_ops_self = ceil(10/3) = 4 人，S_ops 取中端 25万元/年，C_ops_self =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N159, N160, N161

## Claim

在标准运维工作点下，N_pop=10 时 N_ops_self = ceil(10/3) = 4 人，S_ops 取中端 25万元/年，C_ops_self = 4 * 250000 / 12 ≈ ¥83,333/月，分摊到 Q_day=2,048,000 请求后为 ¥40.69/1000 req

## Corrected Claim

在标准运维工作点下，N_pop=10 时 N_ops_self = ceil(10/3) = 4 人，S_ops 取中端 25万元/年，C_ops_self = 4 * 250000 / 12 ≈ ¥83,333/月，分摊到 Q_day=2,048,000 请求后为 ¥40.69/1000 req

## Evidence

先验知识/题面给定，逻辑校验通过：ceil(10/3)=4，4*250000/12≈83333.33，83333.33/2048≈40.69，计算无误且量级合理。
