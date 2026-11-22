# N212: 更新聚集时间尺度 T_cluster 的量化：批量发布通常发生在固定时间窗口（如每小时整点），T_cluster ≈ 1 小时；若 T_cluster << T

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N78

## Claim

更新聚集时间尺度 T_cluster 的量化：批量发布通常发生在固定时间窗口（如每小时整点），T_cluster ≈ 1 小时；若 T_cluster << T_residence，则聚集效应显著；若 T_cluster >> T_residence，则聚集效应可忽略；[待核验：T_cluster 的具体值需根据实际发布策略确定]

## Corrected Claim

更新聚集时间尺度 T_cluster 的量化：批量发布通常发生在固定时间窗口，T_cluster 的具体值需根据实际发布策略确定；若 T_cluster << T_residence，则聚集效应显著；若 T_cluster >> T_residence，则聚集效应可忽略。

## Evidence

[质询]T_cluster 的具体数值（如1小时）是经验事实，取决于具体的发布策略，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

CDN batch publish update frequency hourly window
