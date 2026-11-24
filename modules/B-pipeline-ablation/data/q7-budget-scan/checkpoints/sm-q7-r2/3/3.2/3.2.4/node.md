# N60: HDD+SSD分层方案的硬件购置总成本（CAPEX_total） = (125TB × SSD单价) + (480TB × HDD单价) + 混合阵列配套硬件成

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

HDD+SSD分层方案的硬件购置总成本（CAPEX_total） = (125TB × SSD单价) + (480TB × HDD单价) + 混合阵列配套硬件成本（RAID卡/背板/机箱，约¥80,000-150,000），需分别计算后求和。

## Corrected Claim

HDD+SSD分层方案的硬件购置总成本（CAPEX_total） = (125TB × SSD单价) + (480TB × HDD单价) + 混合阵列配套硬件成本（RAID卡/背板/机箱，约¥80,000-150,000），需分别计算后求和。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合分层存储成本计算的基本逻辑（容量×单价+固定配套成本），数值量级（125TB SSD + 480TB HDD + 8-15万配套）在典型企业级存储场景中合理，无内部矛盾。
