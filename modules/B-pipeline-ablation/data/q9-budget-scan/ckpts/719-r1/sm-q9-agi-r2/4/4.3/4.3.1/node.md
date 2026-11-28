# N63: MTTR < 30 分钟的分解：MTTR = Detection Time + Diagnosis Time + Recovery Time。Detection

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

MTTR < 30 分钟的分解：MTTR = Detection Time + Diagnosis Time + Recovery Time。Detection Time 依赖于监控粒度（建议 < 5 min，基于 Prometheus 抓取间隔 30s + 告警延迟），Diagnosis Time 依赖于日志聚合效率（建议 < 10 min），Recovery Time 依赖于容器重启与状态加载（建议 < 15 min）。

## Corrected Claim

MTTR < 30 分钟的分解：MTTR = Detection Time + Diagnosis Time + Recovery Time。Detection Time 依赖于监控粒度（建议 < 5 min，基于 Prometheus 抓取间隔 30s + 告警延迟），Diagnosis Time 依赖于日志聚合效率（建议 < 10 min），Recovery Time 依赖于容器重启与状态加载（建议 < 15 min）。

## Evidence

先验知识/题面给定，逻辑校验通过：MTTR分解符合SRE通用定义，各分项时间估算（5+10+15=30min）与Prometheus 30s抓取间隔及容器重启常规耗时在量级上自洽且合理。
