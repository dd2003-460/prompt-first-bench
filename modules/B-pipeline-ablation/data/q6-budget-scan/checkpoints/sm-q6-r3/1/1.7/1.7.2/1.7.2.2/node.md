# N163: 骨干网排队延迟 t_queue 与链路利用率 ρ 成正比，t_queue = t_base * (ρ / (1-ρ))，其中 ρ = B_used / B_ca

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

骨干网排队延迟 t_queue 与链路利用率 ρ 成正比，t_queue = t_base * (ρ / (1-ρ))，其中 ρ = B_used / B_capacity，当 ρ > 0.8 时排队延迟显著增加，需监控 P95 利用率以评估实际 t_backbone

## Corrected Claim

骨干网排队延迟 t_queue 与链路利用率 ρ 成正比，t_queue = t_base * (ρ / (1-ρ))，其中 ρ = B_used / B_capacity，当 ρ > 0.8 时排队延迟显著增加，需监控 P95 利用率以评估实际 t_backbone

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合M/M/1排队论中平均等待时间与利用率的关系（Wq ∝ ρ/(1-ρ)），且ρ>0.8时延迟激增符合网络工程常识。

## Search Query

network queueing delay M/M/1 model utilization factor
