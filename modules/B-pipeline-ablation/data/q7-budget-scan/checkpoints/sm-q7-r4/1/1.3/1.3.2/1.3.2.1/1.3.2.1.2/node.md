# N452: 增量恢复数据量 V_incr 的精确界定：题目假设 T_incremental ≈ 5TB/1.25GB/s。需明确这5TB是‘最近24小时写入量’还是‘最近2

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N152

## Claim

增量恢复数据量 V_incr 的精确界定：题目假设 T_incremental ≈ 5TB/1.25GB/s。需明确这5TB是‘最近24小时写入量’还是‘最近24小时变更量’。若数据湖为Append-only日志，V_incr = 24h * Write_Rate。假设年写入总量为数据湖增量的主要部分，若年增长20%（100TB/年），则日均写入 ≈ 0.27TB，24h增量仅为0.27TB。5TB假设可能高估了增量，导致RTO时间被高估。需修正 V_incr = Daily_Write_Volume * RPO_Hours。

## Corrected Claim

增量恢复数据量 V_incr 取决于具体的写入模式与RPO。若为Append-only日志，V_incr = 日均写入量 × RPO小时数。具体数值需基于实际业务负载（如年增量100TB则日均约0.27TB）进行估算，原题中5TB的假设需根据实际日均写入率修正。

## Evidence

[质询]该陈述包含具体的业务假设（如年增长100TB、日均写入0.27TB），这些属于特定场景下的经验数据或题设条件，无法从通用第一性原理推导得出；且参考来源均为Power BI配置文档，与数据湖恢复量计算无关，缺乏外部证据支持其数值合理性。 | 逻辑推导自洽（日均写入=年总量/365，增量=日均*RPO），但参考来源[1][2][3]均涉及Power BI或SQL面试，与数据湖恢复量计算主题无关，属经验事实且缺来源支持。

## Search Query

data lake daily write volume estimation 500TB 20% annual growth

## Retrieval Sources

- {'url': 'https://learn.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-overview&rut=60fe43ecb51a4187156632a48dca521cdc9a45fa561d99d06c3ee7d206c82ee7', 'type': 'ddg', 'title': 'Configure incremental refresh and real-time data for Power BI semantic ...'}
- {'url': 'https://learn.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-configure&rut=ad702bedc8ee72f68ff21633d8ade8a7ed08a769b2dd4e1993044dae2491954e', 'type': 'ddg', 'title': 'Configure incremental refresh for Power BI semantic models - Power BI'}
- {'url': 'https://yennj12.js.org/yennj12_blog_V4/posts/sql-interview-for-de-part4-transform-incremental-merge-zh/&rut=c4ea08afe50850d7243d9db9af5b839a0a24b5ad27d8231b63115e74fe14c451', 'type': 'ddg', 'title': 'DE SQL 面試指南 Part 4：資料轉換——冪等、增量與 MERGE'}
