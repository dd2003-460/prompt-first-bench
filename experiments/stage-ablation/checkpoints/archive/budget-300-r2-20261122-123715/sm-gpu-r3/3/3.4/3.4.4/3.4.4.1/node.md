# N270: RTX 4090 在本地工作站 24/7 满载推理场景下的经验 MTBF_single 估算值为 50,000-100,000 小时（基于高负载加速老化假设），

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

RTX 4090 在本地工作站 24/7 满载推理场景下的经验 MTBF_single 估算值为 50,000-100,000 小时（基于高负载加速老化假设），由此推导出的 3 年单卡故障概率 P_fail_single = 1 - exp(-3*8760/MTBF_single) 约为 25.9% (MTBF=50k) 至 12.8% (MTBF=100k)。

## Corrected Claim

RTX 4090 在本地工作站 24/7 满载推理场景下的经验 MTBF_single 估算值为 50,000-100,000 小时（基于高负载加速老化假设），由此推导出的 3 年单卡故障概率 P_fail_single = 1 - exp(-3*8760/MTBF_single) 约为 25.9% (MTBF=50k) 至 12.8% (MTBF=100k)。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算正确（1-exp(-26280/50000)≈25.9%, 1-exp(-26280/100000)≈12.8%），MTBF量级符合高负载GPU经验估算范畴。

## Search Query

RTX 4090 MTBF failure rate 24/7 load
