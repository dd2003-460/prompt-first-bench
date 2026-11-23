# N26: 数据来源标注机制：建立数据标签系统，标记为 [Realtime: Source=WebSearch, Date=2025-XX] 表示通过实时搜索获取的最新价格

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

数据来源标注机制：建立数据标签系统，标记为 [Realtime: Source=WebSearch, Date=2025-XX] 表示通过实时搜索获取的最新价格/规格；标记为 [Memory: Source=InternalKnowledge, Confidence=High/Medium] 表示基于训练数据截止时间的记忆，且需附带 [Stale_Risk] 警告。对于价格数据，若来源为 Memory 且超过 6 个月，必须触发实时搜索验证或标记为 [待核验] 并采用保守估计值。

## Corrected Claim

数据来源标注机制：建立数据标签系统，标记为 [Realtime: Source=WebSearch, Date=2025-XX] 表示通过实时搜索获取的最新价格/规格；标记为 [Memory: Source=InternalKnowledge, Confidence=High/Medium] 表示基于训练数据截止时间的记忆，且需附带 [Stale_Risk] 警告。对于价格数据，若来源为 Memory 且超过 6 个月，必须触发实时搜索验证或标记为 [待核验] 并采用保守估计值。

## Evidence

检索失败: no sources from any channel (all 5 failed)
