# N454: RTO时间构成的完整性检查：T_RTO = T_detect + T_restore + T_verify + T_switch_back。题目仅计算了 T_r

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N152

## Claim

RTO时间构成的完整性检查：T_RTO = T_detect + T_restore + T_verify + T_switch_back。题目仅计算了 T_restore (1.1h)。需补充：T_detect（故障检测时间，假设5min），T_verify（数据一致性校验，假设恢复量的10%读取，T_verify ≈ 0.1 * 1.1h = 0.11h），T_switch_back（应用切换回存储，假设0.5h）。总 T_RTO_corrected = 0.08 + 1.1 + 0.11 + 0.5 ≈ 1.79h。这将改变N153的成本计算。

## Corrected Claim

RTO时间构成的完整性检查：T_RTO = T_detect + T_restore + T_verify + T_switch_back。题目仅计算了 T_restore (1.1h)。需补充：T_detect（故障检测时间，假设5min），T_verify（数据一致性校验，假设恢复量的10%读取，T_verify ≈ 0.1 * 1.1h = 0.11h），T_switch_back（应用切换回存储，假设0.5h）。总 T_RTO_corrected = 0.08 + 1.1 + 0.11 + 0.5 ≈ 1.79h。这将改变N153的成本计算。

## Evidence

先验知识/题面给定，逻辑校验通过：RTO构成符合标准定义，数值量级合理，算术正确

## Search Query

cloud disaster recovery RTO components detection restore verification switchover time
