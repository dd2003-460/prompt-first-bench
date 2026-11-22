# N347: 平台通知触发阈值的具体参数值：Threshold_notification = 0.05 * Average_Daily_Visitors 中的系数 0.05 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N116, N117, N118

## Claim

平台通知触发阈值的具体参数值：Threshold_notification = 0.05 * Average_Daily_Visitors 中的系数 0.05 是假设值还是实证值？需检索闲鱼/Poshmark 开发者文档或逆向工程报告确认实际使用的阈值系数（如是否为 0.03 或 0.10）及其置信区间。

## Corrected Claim

平台通知触发阈值系数（如0.05）通常为系统设计中的经验假设值或基于内部A/B测试调优的参数，而非具有公开统计置信区间的实证常数；具体数值及性质需依赖内部工程文档或逆向工程推测，公开渠道无法确认其统计显著性。

## Evidence

[质询]该陈述试图确认一个具体的工程参数（阈值系数0.05）是假设值还是实证值，并询问其置信区间。然而，闲鱼和Poshmark作为商业平台，其内部算法参数（如通知触发阈值）通常属于商业机密，极少在公开开发者文档中披露具体数值，更不可能提供统计意义上的“置信区间”。因此，声称存在可检索的“实证值”及其“置信区间”在现实可行性上存疑，且0.05本身极大概率是系统设计中的经验假设值而非经过严格统计实证得出的唯一确定值。 | 无可用外部证据。该事实属于商业平台内部未公开的工程参数细节，逻辑上自洽（即参数确实存在且需定义），但无法通过公开渠道验证其具体来源（假设vs实证）及统计属性，符合经验事实缺来源支持的情形。

## Search Query

Xianyu Poshmark notification threshold algorithm reverse engineering low heat item
