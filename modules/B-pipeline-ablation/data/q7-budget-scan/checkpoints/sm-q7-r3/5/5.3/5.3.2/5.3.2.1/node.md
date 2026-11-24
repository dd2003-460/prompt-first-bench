# N238: 3.84TB NVMe SSD方案下的年化RTO代价变化：因物理盘数从471块减半至236块，单盘故障概率不变导致系统年故障次数P_failure_yearly

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

3.84TB NVMe SSD方案下的年化RTO代价变化：因物理盘数从471块减半至236块，单盘故障概率不变导致系统年故障次数P_failure_yearly减半（从~0.087降至~0.044），结合RTO时间因重建带宽提升而缩短，C_RTO_NVMe_annual将降低约50%-60%。

## Corrected Claim

3.84TB NVMe SSD方案下的年化RTO代价变化：因物理盘数从471块减半至236块，单盘故障概率不变导致系统年故障次数P_failure_yearly减半（从~0.087降至~0.044），结合RTO时间因重建带宽提升而缩短，C_RTO_NVMe_annual将降低约50%-60%。

## Evidence

先验知识/题面给定，逻辑校验通过：物理盘数减半直接导致系统年故障率减半（线性关系），叠加RTO时间缩短，总代价降低50%-60%符合逻辑推导。
