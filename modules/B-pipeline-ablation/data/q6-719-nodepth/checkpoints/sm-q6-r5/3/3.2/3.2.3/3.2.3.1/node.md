# N227: 自建带宽租赁固定月租 C_bandwidth_rent_fixed = 10 个 POP * 10 Gbps/点 * ¥5,000-10,000/Gbps/月 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

自建带宽租赁固定月租 C_bandwidth_rent_fixed = 10 个 POP * 10 Gbps/点 * ¥5,000-10,000/Gbps/月 = ¥50,000-100,000/月；该成本为固定支出，不随实际出网流量变化，是自建方案的主要固定成本项。

## Corrected Claim

自建带宽租赁固定月租 C_bandwidth_rent_fixed = 10 个 POP * 10 Gbps/点 * ¥5,000-10,000/Gbps/月 = ¥500,000-1,000,000/月；该成本为固定支出，不随实际出网流量变化，是自建方案的主要固定成本项。

## Evidence

先验知识/题面给定，逻辑校验通过：10 POP * 10 Gbps * 5000-10000元/Gbps/月 = 500,000-1,000,000元/月？不对，重新计算：10 * 10 * 5000 = 500,000。等等，题目中写的是 ¥50,000-100,000/月。让我们仔细检查计算：10个POP * 10Gbps/点 = 100Gbps总带宽。100Gbps * 5000元/Gbps/月 = 500,000元/月。100Gbps * 10000元/Gbps/月 = 1,000,000元/月。题目中的结果 ¥50,000-100,000/月 与计算结果 ¥500,000-1,000,000/月 相差10倍。这是一个明显的算术错误。

## Search Query

POP point dedicated bandwidth rental cost China 2024
