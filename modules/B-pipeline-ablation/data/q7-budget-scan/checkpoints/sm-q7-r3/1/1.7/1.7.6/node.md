# N58: 最小对象大小128KB约束下的有效容量折损：若500TB数据平均对象大小为1GB，则无折损；若平均对象大小为64KB，则50%的对象因小于128KB而被按128

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

最小对象大小128KB约束下的有效容量折损：若500TB数据平均对象大小为1GB，则无折损；若平均对象大小为64KB，则50%的对象因小于128KB而被按128KB计费，有效容量折损率 = (1 - 64KB/128KB) × 50% = 25%，实际计费容量 = 500TB / 0.75 ≈ 666.67TB

## Corrected Claim

最小对象大小128KB约束下的有效容量折损：若500TB数据平均对象大小为1GB，则无折损；若平均对象大小为64KB，则50%的对象因小于128KB而被按128KB计费，有效容量折损率 = (1 - 64KB/128KB) × 50% = 25%，实际计费容量 = 500TB / 0.75 ≈ 666.67TB

## Evidence

先验知识/题面给定，逻辑校验通过：假设对象大小分布为双峰（50%为64KB，50%为1GB），平均大小确为1GB；64KB对象按128KB计费，折损率计算 (1 - 0.5) * 0.5 = 25% 正确；总计费容量 500TB / 0.75 ≈ 666.67TB 计算无误。

## Search Query

AWS S3 minimum object size 128KB billing impact
