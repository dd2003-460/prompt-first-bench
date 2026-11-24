# N377: 生命周期转换触发次数 N_transitions 的估算：假设数据从 Standard 转为 IA 需 30 天无访问，转为 Archive 需 90 天；若每

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N128

## Claim

生命周期转换触发次数 N_transitions 的估算：假设数据从 Standard 转为 IA 需 30 天无访问，转为 Archive 需 90 天；若每年数据热度变化导致 10% 的对象发生状态变更，则 N_transitions = Total_Objects * 10%；对于 500M 对象，N_transitions = 50,000,000 次/年。

## Corrected Claim

生命周期转换触发次数 N_transitions 的估算：假设数据从 Standard 转为 IA 需 30 天无访问，转为 Archive 需 90 天；若每年数据热度变化导致 10% 的对象发生状态变更，则 N_transitions = Total_Objects * 10%；对于 500M 对象，N_transitions = 50,000,000 次/年。

## Evidence

先验知识/题面给定，逻辑校验通过：500,000,000 * 10% = 50,000,000，计算无误，假设条件明确。
