# N149: S_min 的合理工程假设范围确定：基于 CDN 常见对象大小分布（如视频分片 1-10MB，图片 100KB-1MB），S_min 应取 100KB-1MB 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

S_min 的合理工程假设范围确定：基于 CDN 常见对象大小分布（如视频分片 1-10MB，图片 100KB-1MB），S_min 应取 100KB-1MB 区间；若取 S_min=1MB，S_total=100TB，C/S_total=0.000128，命中率极低，需结合具体业务场景确定 S_min。

## Corrected Claim

S_min 的合理工程假设范围需结合具体业务场景确定；基于常见 CDN 对象大小分布（如视频分片 1-10MB，图片 100KB-1MB），S_min 通常建议在 100KB-1MB 区间内选取，具体数值需根据实际数据分布调整。

## Evidence

[质询]该陈述包含具体的工程经验参数（CDN对象大小分布、S_min取值范围、特定计算结果），属于经验事实而非第一性原理可推导内容，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

CDN object size distribution typical values S_min
