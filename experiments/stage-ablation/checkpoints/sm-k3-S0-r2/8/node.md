# N32: 建立人工抽查验证流程（Human-in-the-Loop Verification Protocol）：采用分层抽样策略，对每篇产出论文抽取关键论证链（Key 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

建立人工抽查验证流程（Human-in-the-Loop Verification Protocol）：采用分层抽样策略，对每篇产出论文抽取关键论证链（Key Argument Chains, KACs）进行复核。KACs定义为包含因果推断或核心实验数据的段落，占比约15-20%。人工复核重点为事实性错误（Factuality Errors）和逻辑跳跃（Logical Leaps），设定单次复核时间预算 T_human < 45 min/paper，若发现事实性错误率 E_fact > 5%，则判定该批次不合格并触发系统参数重校准。

## Corrected Claim

建立人工抽查验证流程（Human-in-the-Loop Verification Protocol）：采用分层抽样策略，对每篇产出论文抽取关键论证链（Key Argument Chains, KACs）进行复核。KACs定义为包含因果推断或核心实验数据的段落，占比约15-20%。人工复核重点为事实性错误（Factuality Errors）和逻辑跳跃（Logical Leaps），设定单次复核时间预算 T_human < 45 min/paper，若发现事实性错误率 E_fact > 5%，则判定该批次不合格并触发系统参数重校准。

## Evidence

检索失败: no sources from any channel (all 5 failed)
