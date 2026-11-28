# N14: 错误恢复机制需定义 3 级降级策略：Level 1 (重试) - 单次 API 失败后指数退避重试 3 次；Level 2 (跳过) - 连续 3 次失败后标记

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

错误恢复机制需定义 3 级降级策略：Level 1 (重试) - 单次 API 失败后指数退避重试 3 次；Level 2 (跳过) - 连续 3 次失败后标记该实验分支为 blocked 并跳过；Level 3 (回滚) - 整体任务超时 (>2h) 后回滚至最近检查点。

## Corrected Claim

错误恢复机制需定义 3 级降级策略：Level 1 (重试) - 单次 API 失败后指数退避重试 3 次；Level 2 (跳过) - 连续 3 次失败后标记该实验分支为 blocked 并跳过；Level 3 (回滚) - 整体任务超时 (>2h) 后回滚至最近检查点。

## Evidence

先验知识/题面给定，逻辑校验通过
