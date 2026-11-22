# N319: 分支2 (Budget > $5000) 的 L40S 吞吐验证：N97 计算 L40S 理论吞吐 13.2 tok/s，实际 9.2 tok/s (0.7效率

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

分支2 (Budget > $5000) 的 L40S 吞吐验证：N97 计算 L40S 理论吞吐 13.2 tok/s，实际 9.2 tok/s (0.7效率)，不满足 Latency_SLA < 50ms/token (即 >20 tok/s) 的约束。因此，推荐 '1x L40S + FP8' 是错误的，除非降低上下文长度或接受 SLA 违约。需寻找满足 >20 tok/s 的替代方案。

## Corrected Claim

分支2 (Budget > $5000) 的 L40S 吞吐验证：N97 计算 L40S 理论吞吐 13.2 tok/s，实际 9.2 tok/s (0.7效率)，不满足 Latency_SLA < 50ms/token (即 >20 tok/s) 的约束。因此，推荐 '1x L40S + FP8' 是错误的，除非降低上下文长度或接受 SLA 违约。需寻找满足 >20 tok/s 的替代方案。

## Evidence

先验知识/题面给定，逻辑校验通过：13.2 * 0.7 ≈ 9.24，9.2 < 20，推导自洽
