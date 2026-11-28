# N106: 多卡方案的通信开销惩罚因子 (Communication_Overhead_Factor) 可建模为：T_total = T_compute + α * (Mo

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

多卡方案的通信开销惩罚因子 (Communication_Overhead_Factor) 可建模为：T_total = T_compute + α * (Model_Size / Bandwidth_effective)，其中 α 为协议开销系数 (0.5-1.0)，Bandwidth_effective 为有效互联带宽。在 PCIe 4.0 下，该因子使总延迟增加 15%-30%；在 NVLink 下，增加 <5% [待核验]。

## Corrected Claim

多卡方案的通信开销惩罚因子 (Communication_Overhead_Factor) 可建模为：T_total = T_compute + α * (Model_Size / Bandwidth_effective)，其中 α 为协议开销系数 (0.5-1.0)，Bandwidth_effective 为有效互联带宽。在 PCIe 4.0 下，该因子使总延迟增加 15%-30%；在 NVLink 下，增加 <5% [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

multi-GPU inference communication overhead factor model size bandwidth
