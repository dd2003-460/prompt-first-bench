# N344: 自建10 POP传输延迟 T_transmission 的具体数值：T_transmission = s / B_eff，其中 s=1MB, B_eff=10G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

自建10 POP传输延迟 T_transmission 的具体数值：T_transmission = s / B_eff，其中 s=1MB, B_eff=10Gbps/8=1.25GB/s，故 T_transmission ≈ 0.8ms，需考虑TCP窗口限制修正

## Corrected Claim

自建10 POP传输延迟 T_transmission 的具体数值：T_transmission = s / B_eff，其中 s=1MB, B_eff=10Gbps/8=1.25GB/s，故 T_transmission ≈ 0.8ms，需考虑TCP窗口限制修正

## Evidence

先验知识/题面给定，逻辑校验通过：1MB / 1.25GB/s = 0.8ms，计算正确且量级合理
