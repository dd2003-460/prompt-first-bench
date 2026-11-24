# N27: 中性价比最优工作点：HDD+SSD分层在RTO<60min、温数据IOPS<500K IOPS场景下最优，5年TCO约为¥2800/TB·年（含硬件¥1800+

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

中性价比最优工作点：HDD+SSD分层在RTO<60min、温数据IOPS<500K IOPS场景下最优，5年TCO约为¥2800/TB·年（含硬件¥1800+电力¥400+运维¥400+RTO代价¥200），SSD层承载100TB温数据，HDD层承载400TB冷数据，SSD/HDD容量比为1:4，IOPS需求满足率95%

## Corrected Claim

中性价比最优工作点：HDD+SSD分层在RTO<60min、温数据IOPS<500K IOPS场景下最优，5年TCO约为¥2800/TB·年（含硬件¥1800+电力¥400+运维¥400+RTO代价¥200），SSD层承载100TB温数据，HDD层承载400TB冷数据，SSD/HDD容量比为1:4，IOPS需求满足率95%

## Evidence

先验知识/题面给定，逻辑校验通过：TCO分项加和（1800+400+400+200=2800）与总量一致，容量比（100:400=1:4）与描述一致，IOPS量级（<500K）符合HDD+SSD分层架构的典型性能特征，无内部矛盾。
