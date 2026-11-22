# N126: Stale 对象在缓存中的字节占比量化：计算 Stale_bytes = ∫_{1}^{∞} S(k) * P(age > 1 | k) dk，其中 P(age

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

Stale 对象在缓存中的字节占比量化：计算 Stale_bytes = ∫_{1}^{∞} S(k) * P(age > 1 | k) dk，其中 P(age > 1 | k) 需结合对象 k 的驻留时间 T_res(k) 和更新率 u=0.01 进行联合概率积分，而非简单乘以 10%。

## Corrected Claim

Stale 对象在缓存中的字节占比量化：计算 Stale_bytes = ∫_{1}^{∞} S(k) * P(age > 1 | k) dk，其中 P(age > 1 | k) 需结合对象 k 的驻留时间 T_res(k) 和更新率 u=0.01 进行联合概率积分，而非简单乘以 10%。

## Evidence

先验知识/题面给定，逻辑校验通过：Stale 字节占比确实需要基于年龄分布（Age Distribution）进行积分计算，而非简单乘以固定比例，公式结构符合缓存理论中基于驻留时间和更新率的概率积分逻辑。
