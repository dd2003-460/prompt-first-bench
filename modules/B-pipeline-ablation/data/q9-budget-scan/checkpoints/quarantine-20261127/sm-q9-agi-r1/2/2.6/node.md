# N18: 控制流调度器的优先级队列机制：采用加权公平队列（WFQ），假设生成任务权重=1.0，实验执行任务权重=2.0（因耗时较长），结果分析任务权重=0.5（快速完成）

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

控制流调度器的优先级队列机制：采用加权公平队列（WFQ），假设生成任务权重=1.0，实验执行任务权重=2.0（因耗时较长），结果分析任务权重=0.5（快速完成），避免低优先级任务饿死高优先级任务，队列最大长度=32，溢出时丢弃最低优先级任务并记录日志。

## Corrected Claim

控制流调度器的优先级队列机制：采用加权公平队列（WFQ），假设生成任务权重=1.0，实验执行任务权重=2.0（因耗时较长），结果分析任务权重=0.5（快速完成），避免低优先级任务饿死高优先级任务，队列最大长度=32，溢出时丢弃最低优先级任务并记录日志。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

weighted fair queue scheduling LLM agent task priority overflow handling
