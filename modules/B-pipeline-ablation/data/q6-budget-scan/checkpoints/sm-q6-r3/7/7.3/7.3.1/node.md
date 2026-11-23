# N293: 硬件故障率分层模型：总年故障率 λ_total = λ_cpu + λ_disk + λ_ram + λ_psu，其中λ_disk（NVMe SSD）通常主导，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94, N95, N96

## Claim

硬件故障率分层模型：总年故障率 λ_total = λ_cpu + λ_disk + λ_ram + λ_psu，其中λ_disk（NVMe SSD）通常主导，典型值为0.5-2%/年/盘，λ_cpu/ram/psu各约0.1-0.5%/年，需按部件独立估算后求和

## Corrected Claim

硬件故障率分层模型：总年故障率 λ_total = λ_cpu + λ_disk + λ_ram + λ_psu，其中λ_disk（NVMe SSD）通常主导，典型值为0.5-2%/年/盘，λ_cpu/ram/psu各约0.1-0.5%/年，需按部件独立估算后求和

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

server component failure rate cpu ram nvme psu annual percentage
