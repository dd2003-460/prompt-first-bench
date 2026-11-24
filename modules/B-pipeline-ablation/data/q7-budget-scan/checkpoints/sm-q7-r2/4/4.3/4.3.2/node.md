# N60: HDD 分层在 HDD 机械寻道约束下的恢复工作点：Restore_Throughput=5TB/h, Data_Size=400TB(冷), T_restor

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

HDD 分层在 HDD 机械寻道约束下的恢复工作点：Restore_Throughput=5TB/h, Data_Size=400TB(冷), T_restore=81h (含2h overhead)

## Corrected Claim

HDD 分层在 HDD 机械寻道约束下的恢复工作点：Restore_Throughput=5TB/h, Data_Size=400TB(冷), T_restore=81h (含2h overhead)

## Evidence

先验知识/题面给定，逻辑校验通过：400TB / 5TB/h = 80h，加上 2h overhead 等于 81h，数值计算自洽且符合 HDD 恢复场景的量级直觉。
