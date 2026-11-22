# N184: 量化p_1 = 0.01018对字节命中率 H_byte 的边际贡献：计算 p_1 * s_1 / S_total_bytes，其中 s_1 为最热对象大小（受

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

量化p_1 = 0.01018对字节命中率 H_byte 的边际贡献：计算 p_1 * s_1 / S_total_bytes，其中 s_1 为最热对象大小（受ρ=-0.3影响），评估单点故障或头部对象更新对整体命中率的敏感度 ∂H/∂p_1。

## Corrected Claim

量化p_1 = 0.01018对字节命中率 H_byte 的边际贡献：计算 p_1 * s_1 / S_total_bytes，其中 s_1 为最热对象大小（受ρ=-0.3影响），评估单点故障或头部对象更新对整体命中率的敏感度 ∂H/∂p_1。

## Evidence

先验知识/题面给定，逻辑校验通过
