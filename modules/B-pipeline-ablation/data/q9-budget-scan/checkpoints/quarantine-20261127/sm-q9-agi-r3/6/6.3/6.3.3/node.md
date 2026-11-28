# N105: RTO 的统计验证方法：在测试环境中人为注入 10 次故障（通过 kill -9 终止 vLLM 进程），记录每次从故障发生到服务恢复可用的时间戳，计算均值 μ

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

RTO 的统计验证方法：在测试环境中人为注入 10 次故障（通过 kill -9 终止 vLLM 进程），记录每次从故障发生到服务恢复可用的时间戳，计算均值 μ_RTO 和标准差 σ_RTO，要求 μ_RTO + 2σ_RTO ≤ 5 分钟（95% 置信区间）

## Corrected Claim

RTO 的统计验证方法：在测试环境中人为注入 10 次故障（通过 kill -9 终止 vLLM 进程），记录每次从故障发生到服务恢复可用的时间戳，计算均值 μ_RTO 和标准差 σ_RTO，要求 μ_RTO + 2σ_RTO ≤ 5 分钟（95% 置信区间）

## Evidence

先验知识/题面给定，逻辑校验通过：RTO统计验证采用均值加两倍标准差作为95%置信上限符合正态分布近似原则，kill -9模拟故障及5分钟阈值在工程实践中合理且自洽。
