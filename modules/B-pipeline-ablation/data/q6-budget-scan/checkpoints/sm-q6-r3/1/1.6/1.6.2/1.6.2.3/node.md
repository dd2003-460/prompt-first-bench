# N118: SaaS方案（如Datadog）的月度成本 = (基础订阅费¥500/节点 * 10节点) + (数据摄入量>5GB/天的超额费用)，其中超额费用 = (实际日

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

SaaS方案（如Datadog）的月度成本 = (基础订阅费¥500/节点 * 10节点) + (数据摄入量>5GB/天的超额费用)，其中超额费用 = (实际日志量GB - 免费额度GB) * 单价(¥/GB)

## Corrected Claim

SaaS方案（如Datadog）的月度成本 = (基础订阅费¥500/节点 * 10节点) + (数据摄入量>5GB/天的超额费用)，其中超额费用 = (实际日志量GB - 免费额度GB) * 单价(¥/GB)

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Datadog pricing log ingestion cost per GB 2024
