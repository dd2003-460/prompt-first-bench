# N132: 在容量充足假设下，ΔH_bytes 积分的分子 [P_LFU_keep(s) - P_LRU_keep(s)] 恒为 0，导致积分结果为 0，即 LFU 增益为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

在容量充足假设下，ΔH_bytes 积分的分子 [P_LFU_keep(s) - P_LRU_keep(s)] 恒为 0，导致积分结果为 0，即 LFU 增益为 0%

## Corrected Claim

在容量充足假设下，ΔH_bytes 积分的分子 [P_LFU_keep(s) - P_LRU_keep(s)] 恒为 0，导致积分结果为 0，即 LFU 增益为 0%

## Evidence

先验知识/题面给定，逻辑校验通过：在容量充足（无驱逐）假设下，LFU与LRU均保留所有访问过的对象，保留概率均为1，差值为0，积分结果为0。
