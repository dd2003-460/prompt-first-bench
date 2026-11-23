# N73: 热点对象数 N_unique_hot 估算：基于 Zipf 分布，N_unique_hot ≈ N_total * (1 / (1 - (1/N_total)^

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

热点对象数 N_unique_hot 估算：基于 Zipf 分布，N_unique_hot ≈ N_total * (1 / (1 - (1/N_total)^α))，其中 α 为 Zipf 指数（通常 0.8-1.2）

## Corrected Claim

热点对象数 N_unique_hot 估算：基于 Zipf 分布，N_unique_hot ≈ N_total * (1 / (1 - (1/N_total)^α))，其中 α 为 Zipf 指数（通常 0.8-1.2）

## Evidence

先验知识/题面给定，逻辑校验通过
