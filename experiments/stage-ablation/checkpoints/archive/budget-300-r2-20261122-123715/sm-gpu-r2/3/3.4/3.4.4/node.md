# N79: 多卡方案 (2x RTX 4090) 的系统级故障率修正：由于存在两个独立故障源，系统 MTBF_sys = MTBF_single / 2 (假设独立故障)，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

多卡方案 (2x RTX 4090) 的系统级故障率修正：由于存在两个独立故障源，系统 MTBF_sys = MTBF_single / 2 (假设独立故障)，需计算双卡同时或任一卡故障导致推理中断的概率，以及 PCIe 链路故障的额外风险系数。

## Corrected Claim

多卡方案 (2x RTX 4090) 的系统级故障率修正：由于存在两个独立故障源，系统 MTBF_sys = MTBF_single / 2 (假设独立故障)，需计算双卡同时或任一卡故障导致推理中断的概率，以及 PCIe 链路故障的额外风险系数。

## Evidence

先验知识/题面给定，逻辑校验通过：基于独立故障假设，系统MTBF为单卡MTBF除以故障源数量（2），符合可靠性工程基本定律。
