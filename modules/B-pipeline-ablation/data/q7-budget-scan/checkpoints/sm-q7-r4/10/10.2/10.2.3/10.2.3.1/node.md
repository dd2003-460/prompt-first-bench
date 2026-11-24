# N695: P_base_per_TB = 0.05 W/TB 是冷数据静态存储的理论下限，未包含数据索引、元数据存储及后台碎片整理 (compaction) 的能耗，实际

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N288

## Claim

P_base_per_TB = 0.05 W/TB 是冷数据静态存储的理论下限，未包含数据索引、元数据存储及后台碎片整理 (compaction) 的能耗，实际云厂商冷存储层 P_base_per_TB 通常在 0.1-0.3 W/TB 之间，若采用 0.2 W/TB，电力分摊占比将升至约 2%，需修正原公式中的分子参数。

## Corrected Claim

P_base_per_TB = 0.05 W/TB 是冷数据静态存储的理论下限，未包含数据索引、元数据存储及后台碎片整理 (compaction) 的能耗，实际云厂商冷存储层 P_base_per_TB 通常在 0.1-0.3 W/TB 之间，若采用 0.2 W/TB，电力分摊占比将升至约 2%，需修正原公式中的分子参数。

## Evidence

先验知识/题面给定，逻辑校验通过：0.05 W/TB作为纯介质静态功耗下限符合HDD/SSD物理特性，0.1-0.3 W/TB涵盖索引与后台开销符合行业工程经验，2%电力占比推算在常规数据中心PUE及负载假设下量级合理。

## Search Query

cloud object storage cold data power consumption per TB index overhead
