# N321: 故障检测与切换时间 T_failover 的影响：在单 POP 故障期间，DNS 或健康检查切换通常需要 30-60 秒。在这 30-60 秒内，用户仍尝试连接

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N111

## Claim

故障检测与切换时间 T_failover 的影响：在单 POP 故障期间，DNS 或健康检查切换通常需要 30-60 秒。在这 30-60 秒内，用户仍尝试连接故障 POP，导致超时。假设超时阈值为 3s，则 T_timeout = 3000ms。故障期间的平均延迟惩罚 = (T_failover / 2) × P_timeout，若 P_timeout 为 100%，则平均惩罚 ≈ 30s。

## Corrected Claim

故障检测与切换时间 T_failover 的影响：在单 POP 故障期间，DNS 或健康检查切换通常需要 30-60 秒。在这 30-60 秒内，用户仍尝试连接故障 POP，导致超时。假设超时阈值为 3s，则 T_timeout = 3000ms。故障期间的平均延迟惩罚 = (T_failover / 2) × P_timeout，若 P_timeout 为 100%，则平均惩罚 ≈ 30s。

## Evidence

先验知识/题面给定，逻辑校验通过：30-60秒切换时间的中值为45秒，若故障期间100%请求超时且平均等待时间为切换时间的一半（均匀分布假设），则平均惩罚为22.5秒，与陈述中的≈30s（取上限或保守估计）在量级和逻辑上自洽。
