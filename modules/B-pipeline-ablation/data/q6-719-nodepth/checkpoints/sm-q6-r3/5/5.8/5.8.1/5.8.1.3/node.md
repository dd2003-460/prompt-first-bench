# N347: 单POP故障恢复时间 Recovery_Time 的量化分解：Recovery_Time = T_Detection + T_Switch + T_Verifi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N120

## Claim

单POP故障恢复时间 Recovery_Time 的量化分解：Recovery_Time = T_Detection + T_Switch + T_Verification。基于SOP标准，T_Detection（监控告警）≈ 5 min，T_Switch（流量切换至备用POP）≈ 10 min（DNS TTL限制），T_Verification（业务验证）≈ 5 min，合计 Recovery_Time ≈ 20 min = 1/3 hour。

## Corrected Claim

单POP故障恢复时间 Recovery_Time 的量化分解：Recovery_Time = T_Detection + T_Switch + T_Verification。基于SOP标准，T_Detection（监控告警）≈ 5 min，T_Switch（流量切换至备用POP）≈ 10 min（DNS TTL限制），T_Verification（业务验证）≈ 5 min，合计 Recovery_Time ≈ 20 min = 1/3 hour。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN failover time DNS TTL detection switching verification minutes
