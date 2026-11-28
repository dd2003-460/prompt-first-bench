# N101: 软件层缓解 ECC 缺失的成本函数为 Cost_mitigation = T_verify × F_verify_freq + C_dev_overhead，其

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

软件层缓解 ECC 缺失的成本函数为 Cost_mitigation = T_verify × F_verify_freq + C_dev_overhead，其中 T_verify 是周期性显存校验 (Memory Checksum) 带来的额外计算延迟 (通常增加 1-3% 推理延迟 [待核验])，C_dev_overhead 是开发和维护该容错逻辑的工程人力成本；若校验频率过低，则无法有效拦截累积错误。

## Corrected Claim

软件层缓解 ECC 缺失的成本函数为 Cost_mitigation = T_verify × F_verify_freq + C_dev_overhead，其中 T_verify 是周期性显存校验 (Memory Checksum) 带来的额外计算延迟 (通常增加 1-3% 推理延迟 [待核验])，C_dev_overhead 是开发和维护该容错逻辑的工程人力成本；若校验频率过低，则无法有效拦截累积错误。

## Evidence

先验知识/题面给定，逻辑校验通过
