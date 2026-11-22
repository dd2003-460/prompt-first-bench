# N268: AFR (Annual Failure Rate) 的一手数据来源与置信度：Google/Amazon 数据中心论文报告的 1-3% AFR 基于百万级规模且包

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85, N86, N87

## Claim

AFR (Annual Failure Rate) 的一手数据来源与置信度：Google/Amazon 数据中心论文报告的 1-3% AFR 基于百万级规模且包含冗余设计；消费级 GPU (RTX 4090) 缺乏大规模公开 AFR 数据，社区估算 5-10% 主要基于二手市场退货率及故障报告，置信度低 [待核验]；对于本地单卡无冗余场景，应保守采用 10% AFR 进行风险评估。

## Corrected Claim

AFR (Annual Failure Rate) 的一手数据来源与置信度：Google/Amazon 数据中心论文报告的 1-3% AFR 基于百万级规模且包含冗余设计；消费级 GPU (RTX 4090) 缺乏大规模公开 AFR 数据，社区估算 5-10% 主要基于二手市场退货率及故障报告，置信度低；对于本地单卡无冗余场景，建议保守采用 10% AFR 进行风险评估，但需注意该数值为经验性保守估计，缺乏大规模实证数据支持。

## Evidence

[质询]消费级GPU（如RTX 4090）的5-10% AFR估算缺乏大规模公开一手数据支持，主要基于社区二手市场退货率及故障报告，存在样本偏差和幸存者偏差，置信度低；且将数据中心冗余设计下的AFR与本地单卡无冗余场景直接对比并建议保守采用10% AFR，缺乏严谨的统计推导或权威来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，全部通道失败）

## Search Query

RTX 4090 annual failure rate AFR benchmark consumer GPU vs data center
