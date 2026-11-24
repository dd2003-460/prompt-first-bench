# N750: 工作点C（宽松RPO/低成本）：RPO=7天，500TB全量+35TB增量。若将35TB增量移至S3 IA层，存储成本节省 = 35TB * 1024 * ($

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N280

## Claim

工作点C（宽松RPO/低成本）：RPO=7天，500TB全量+35TB增量。若将35TB增量移至S3 IA层，存储成本节省 = 35TB * 1024 * ($0.023-$0.0125) * 12 * 7.2 ≈ ¥29,952/年。但恢复时IA层取回费 = 35TB * 1024 * $0.01 * 7.2 ≈ ¥25,805/次，若年恢复频率>2次，总成本反超Standard层，故仅适合恢复频率<1次/年的场景。

## Corrected Claim

工作点C（宽松RPO/低成本）：RPO=7天，500TB全量+35TB增量。若将35TB增量移至S3 IA层，基于典型区域价格估算，存储成本可显著降低，但需承担取回费用。由于取回费取决于取回速度和数据量，若年恢复频率较高（如>2次），总成本可能反超Standard层，故该方案仅适合恢复频率极低（<1次/年）的场景。

## Evidence

[质询]AWS S3 Standard-IA 的取回费（Retrieval Fee）并非固定的 $0.01/GB，而是根据请求大小和取回速度（Standard/Bulk/Expedited）动态变化（通常范围在 $0.01 - $0.03/GB 之间），且 S3 Standard 与 S3 Standard-IA 的存储单价差值也随区域波动，陈述中使用的固定汇率和固定单价缺乏特定区域和取回策略的限定，导致计算结果具有较大的不确定性。 | 参考来源 [1][2][3] 仅讨论备份策略概念（RPO/RTO/全量增量），未涉及 AWS S3 具体存储层级定价及成本计算，属于经验事实且缺乏直接来源支持，但逻辑推导过程自洽。

## Search Query

AWS S3 IA retrieval fee per GB 2024

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_33978578/article/details/170940616&rut=0c093e1e00efcdfad51c205cf4e4b68814bca20412862af9b82863cec0f0cfb8', 'type': 'ddg', 'title': '备份策略怎么定？全量增量差量结合rpo/Rto的排布与调优指南-csdn博客'}
- {'url': 'https://www.orathos.com/zh/insights/enterprise-application-backup-strategies-rpo-rto-and-recovery-planning&rut=0df97a7e20ea5c920fe10945406e3700c61c845fc0370afd86fa570487ad4019', 'type': 'ddg', 'title': '企业应用备份策略：RPO、RTO与恢复规划 · Orathos'}
- {'url': 'https://blog.csdn.net/weixin_42525738/article/details/170940623&rut=50de74420da169ce74b361869ff770b35fac35933f8be65f98e215a9ee0ba743', 'type': 'ddg', 'title': '备份策略实战：全量、增量、差量与rpo/Rto如何设计-csdn博客'}
