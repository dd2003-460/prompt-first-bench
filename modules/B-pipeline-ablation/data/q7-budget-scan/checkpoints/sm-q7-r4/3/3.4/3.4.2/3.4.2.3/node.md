# N225: 混合恢复策略的临界点分析：设增量恢复阈值为V_inc，若故障发生时变更数据量 > V_inc，则必须全量恢复；假设日均写入10TB，则V_inc=10TB，若故

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

混合恢复策略的临界点分析：设增量恢复阈值为V_inc，若故障发生时变更数据量 > V_inc，则必须全量恢复；假设日均写入10TB，则V_inc=10TB，若故障发生在写入高峰后，C_rto期望值 E[C_rto] = P(incremental)×0 + P(full)×¥535,500，其中P(full)取决于故障时刻分布

## Corrected Claim

混合恢复策略的临界点分析：设增量恢复阈值为V_inc，若故障发生时变更数据量 > V_inc，则必须全量恢复；假设日均写入10TB，则V_inc=10TB，若故障发生在写入高峰后，C_rto期望值 E[C_rto] = P(incremental)×0 + P(full)×¥535,500，其中P(full)取决于故障时刻分布

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cloud storage incremental backup RTO calculation
