# N365: 工作点 3 (Erasure Coding 10+4) 在分布式存储中的替代方案：几何系数 1.4，浪费率 40%，但 EC 重建只需读取 10 块盘而非 RA

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N161

## Claim

工作点 3 (Erasure Coding 10+4) 在分布式存储中的替代方案：几何系数 1.4，浪费率 40%，但 EC 重建只需读取 10 块盘而非 RAID6 的 11 块，I/O 放大系数更低。若采用 EC，空间浪费成本高达 ¥58,000/年，仅在超大规模 (>PB) 且追求极致吞吐量时优于 RAID6，对于 500TB 规模，RAID6 仍是更优的平衡点。

## Corrected Claim

工作点 3 (Erasure Coding 10+4) 在分布式存储中的替代方案：几何系数 1.4，浪费率 40%，但 EC 重建只需读取 10 块盘而非 RAID6 的 11 块，I/O 放大系数更低。若采用 EC，空间浪费成本高达 ¥58,000/年，仅在超大规模 (>PB) 且追求极致吞吐量时优于 RAID6，对于 500TB 规模，RAID6 仍是更优的平衡点。

## Evidence

先验知识/题面给定，逻辑校验通过：EC(10+4)几何系数1.4及40%浪费率计算正确（14/10=1.4, (14-10)/10=40%）；重建读取10块盘符合EC原理；500TB规模下RAID6通常优于EC的工程判断符合行业共识。

## Search Query

erasure coding vs RAID6 efficiency tradeoff
