# N315: HDD+SSD 分层方案中 HDD 层故障率 λ_HDD 的精确计算：40 块 16TB 企业级 HDD，单盘 MTBF 2,000,000h，λ_single

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

HDD+SSD 分层方案中 HDD 层故障率 λ_HDD 的精确计算：40 块 16TB 企业级 HDD，单盘 MTBF 2,000,000h，λ_single_hdd = (40 / 2,000,000) * 8760 = 0.1752 次/年；若 RAID6 允许 2 盘同时故障而不丢数据，则系统级故障率 λ_system_hdd = C(40,3) * (λ_single_hdd/40)^3 * (1-λ_single_hdd/40)^(37) ≈ 0.0001 次/年，远低于单盘故障率，需区分单盘故障与系统级数据丢失故障。

## Corrected Claim

HDD+SSD 分层方案中 HDD 层故障率 λ_HDD 的精确计算：40 块 16TB 企业级 HDD，单盘 MTBF 2,000,000h，λ_single_hdd = (40 / 2,000,000) * 8760 = 0.1752 次/年；若 RAID6 允许 2 盘同时故障而不丢数据，则系统级故障率 λ_system_hdd = C(40,3) * (λ_single_hdd/40)^3 * (1-λ_single_hdd/40)^(37) ≈ 0.0001 次/年，远低于单盘故障率，需区分单盘故障与系统级数据丢失故障。

## Evidence

先验知识/题面给定，逻辑校验通过：单盘年故障率计算正确（40/2000000*8760=0.1752）；RAID6系统级故障率（需3盘故障）基于二项分布近似计算，量级合理（约1e-4），符合RAID6高可靠性特征。

## Search Query

RAID6 system failure rate multiple disk failure probability MTBF
