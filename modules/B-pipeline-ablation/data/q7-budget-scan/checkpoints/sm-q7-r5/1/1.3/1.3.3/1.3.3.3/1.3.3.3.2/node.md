# N341: 阿里云 OSS 深度冷归档的数据取回费用分为三种优先级：低优先级（Low）约 ¥0.02/GB，标准优先级（Standard）约 ¥0.05/GB，高优先级（H

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N151, N153, N154

## Claim

阿里云 OSS 深度冷归档的数据取回费用分为三种优先级：低优先级（Low）约 ¥0.02/GB，标准优先级（Standard）约 ¥0.05/GB，高优先级（High）约 ¥0.09/GB；对于 500TB 全量冷数据，若发生一次全量取回，成本差异巨大，例如 Low 优先级成本 = 500 * 1024 * 0.02 = ¥10,240

## Corrected Claim

阿里云 OSS 深度冷归档的数据取回费用分为低、标准、高三种优先级，不同优先级的单位取回费用不同（具体数值需查阅最新官方定价页）；对于 500TB 全量冷数据，若发生一次全量取回，不同优先级下的总成本差异显著。

## Evidence

[质询]具体价格数值（¥0.02/GB, ¥0.05/GB, ¥0.09/GB）属于经验事实，且阿里云OSS定价策略可能随时间调整，当前陈述中的具体数值缺乏实时来源验证，存在过时或偏差风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体单价数值）

## Search Query

Alibaba Cloud OSS Deep Cold Archive retrieval fees low standard high priority per GB
