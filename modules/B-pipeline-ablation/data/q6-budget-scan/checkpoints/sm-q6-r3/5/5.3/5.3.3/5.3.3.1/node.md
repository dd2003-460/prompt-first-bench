# N315: 延迟惩罚低代价工作点（同省回源）：Origin 与 POP 点位于同一省份或相邻省份，T_origin_RTT ≈ 30-50ms，T_edge_RTT ≈ 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

延迟惩罚低代价工作点（同省回源）：Origin 与 POP 点位于同一省份或相邻省份，T_origin_RTT ≈ 30-50ms，T_edge_RTT ≈ 10-20ms，延迟增加量 ΔLatency ≈ 20-30ms，P99 劣化幅度小，但要求 Origin 具备高带宽冗余。

## Corrected Claim

延迟惩罚低代价工作点（同省回源）：Origin 与 POP 点位于同一省份或相邻省份，T_origin_RTT ≈ 30-50ms，T_edge_RTT ≈ 10-20ms，延迟增加量 ΔLatency ≈ 20-30ms，P99 劣化幅度小，但要求 Origin 具备高带宽冗余。

## Evidence

先验知识/题面给定，逻辑校验通过：同省/相邻省份光纤传输延迟通常在10-50ms量级，边缘节点到源站的RTT差值20-30ms符合物理直觉与工程经验，且source为knowledge，无需外部来源支持。
