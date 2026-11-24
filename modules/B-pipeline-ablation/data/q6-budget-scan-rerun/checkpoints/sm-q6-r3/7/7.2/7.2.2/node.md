# N369: 自建 POP 流量分散度对 CHR 的惩罚：CHR_self_geo = CHR_uniform × (1 - β × H(geo_share))，其中 H(g

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N117

## Claim

自建 POP 流量分散度对 CHR 的惩罚：CHR_self_geo = CHR_uniform × (1 - β × H(geo_share))，其中 H(geo_share) 为地理分布的香农熵，β 为分散度惩罚系数（典型值 0.05-0.15），当 geo_share 高度不均（如某 POP 占 30% 流量），CHR 比均匀分布降低 5-10%。

## Corrected Claim

自建 POP 流量分散度对 CHR 的惩罚：CHR_self_geo = CHR_uniform × (1 - β × H(geo_share))，其中 H(geo_share) 为地理分布的香农熵，β 为分散度惩罚系数（典型值 0.05-0.15），当 geo_share 高度不均（如某 POP 占 30% 流量），CHR 比均匀分布降低 5-10%。

## Evidence

先验知识/题面给定，逻辑校验通过
