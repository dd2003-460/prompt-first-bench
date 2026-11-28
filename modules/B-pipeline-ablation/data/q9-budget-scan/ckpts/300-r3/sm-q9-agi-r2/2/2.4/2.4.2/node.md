# N64: code_executor 执行超时阈值与重试策略：单次执行超时设为 300s，若超时触发自动 kill 并重试 1 次（超时概率 P_timeout=2%），

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

code_executor 执行超时阈值与重试策略：单次执行超时设为 300s，若超时触发自动 kill 并重试 1 次（超时概率 P_timeout=2%），重试失败则返回 error_msg='timeout'，平均单次调用耗时 E[T]=0.98*250s + 0.02*(300s+retry_cost)

## Corrected Claim

code_executor 执行超时阈值与重试策略：单次执行超时设为 300s，若超时触发自动 kill 并重试 1 次（超时概率 P_timeout=2%），重试失败则返回 error_msg='timeout'，平均单次调用耗时 E[T]=0.98*250s + 0.02*(300s+retry_cost)

## Evidence

先验知识/题面给定，逻辑校验通过：期望耗时公式 E[T] = (1-P)*T_success + P*(T_timeout + T_retry) 符合全期望公式定义，数值量级合理（250s < 300s），无内部矛盾。
