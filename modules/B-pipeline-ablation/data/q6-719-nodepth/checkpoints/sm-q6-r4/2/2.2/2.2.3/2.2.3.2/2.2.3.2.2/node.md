# N632: 人工成本 Labor_Cost 结构：远程诊断与指导成本为 ¥0（由 SRE 兼任），现场更换人工成本为 ¥500-¥1,000/次（含差旅）；若 POP 位于

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N217

## Claim

人工成本 Labor_Cost 结构：远程诊断与指导成本为 ¥0（由 SRE 兼任），现场更换人工成本为 ¥500-¥1,000/次（含差旅）；若 POP 位于偏远地区，差旅成本增加 50%，Labor_Cost 中值取 ¥750；若采用自动化故障隔离（BGP Anycast 切换），可避免现场人工介入，Labor_Cost 降至 ¥0，但需额外投入自动化系统开发成本。

## Corrected Claim

人工成本 Labor_Cost 结构：远程诊断与指导成本为 ¥0（由 SRE 兼任），现场更换人工成本为 ¥500-¥1,000/次（含差旅）；若 POP 位于偏远地区，差旅成本增加 50%，Labor_Cost 中值取 ¥750；若采用自动化故障隔离（BGP Anycast 切换），可避免现场人工介入，Labor_Cost 降至 ¥0，但需额外投入自动化系统开发成本。

## Evidence

先验知识/题面给定，逻辑校验通过
