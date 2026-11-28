# N129: Budget_limit 的动态计算逻辑：Budget_limit = Total_Allocated_Budget * (1 - Remaining_Task

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

Budget_limit 的动态计算逻辑：Budget_limit = Total_Allocated_Budget * (1 - Remaining_Tasks_Ratio) - Safety_Margin，其中 Safety_Margin 设为 10% 以防止意外超支，Remaining_Tasks_Ratio 为当前队列中剩余任务数与总任务数之比。

## Corrected Claim

Budget_limit 的动态计算逻辑：Budget_limit = Total_Allocated_Budget * (1 - Remaining_Tasks_Ratio) - Safety_Margin，其中 Safety_Margin 设为 10% 以防止意外超支，Remaining_Tasks_Ratio 为当前队列中剩余任务数与总任务数之比。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

dynamic budget allocation algorithm for multi-agent systems
