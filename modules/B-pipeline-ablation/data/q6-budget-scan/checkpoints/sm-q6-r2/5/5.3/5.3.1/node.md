# N78: 预热对象选择策略：基于历史热度排名，选取 Top-K 热点对象进行预热，K 由预热预算 B_warm 决定：K = B_warm / (s_avg * c_ba

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

预热对象选择策略：基于历史热度排名，选取 Top-K 热点对象进行预热，K 由预热预算 B_warm 决定：K = B_warm / (s_avg * c_bandwidth)

## Corrected Claim

预热对象选择策略：基于历史热度排名，选取 Top-K 热点对象进行预热，K 由预热预算 B_warm 决定：K = B_warm / (s_avg * c_bandwidth)

## Evidence

先验知识/题面给定，逻辑校验通过
