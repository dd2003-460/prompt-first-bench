# N332: MTTR (T_fault) 的分解：T_fault = T_detect + T_dispatch + T_repair；对于自建POP，T_detect≈1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

MTTR (T_fault) 的分解：T_fault = T_detect + T_dispatch + T_repair；对于自建POP，T_detect≈15min（监控告警），T_dispatch≈30min（工程师响应），T_repair≈135min（硬件更换/链路切换），总计约4小时；公有云CDN通常T_fault<15min（自动故障转移），需对比两种策略的T_fault差异。

## Corrected Claim

MTTR (T_fault) 的分解：T_fault = T_detect + T_dispatch + T_repair；对于自建POP，T_detect≈15min（监控告警），T_dispatch≈30min（工程师响应），T_repair≈135min（硬件更换/链路切换），总计约4小时；公有云CDN通常T_fault<15min（自动故障转移），需对比两种策略的T_fault差异。

## Evidence

先验知识/题面给定，逻辑校验通过
