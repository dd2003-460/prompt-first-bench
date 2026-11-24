# N153: 拥塞抖动 σ_congestion 与链路利用率 ρ 的定量关系：σ_congestion ≈ σ_base × (1 / (1 - ρ))，其中 σ_base

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N43

## Claim

拥塞抖动 σ_congestion 与链路利用率 ρ 的定量关系：σ_congestion ≈ σ_base × (1 / (1 - ρ))，其中 σ_base 为低负载（ρ<20%）下的基础抖动（典型值 1-2ms），ρ 为当前链路带宽利用率。

## Corrected Claim

拥塞抖动 σ_congestion 与链路利用率 ρ 的定量关系：σ_congestion ≈ σ_base × (1 / (1 - ρ))，其中 σ_base 为低负载（ρ<20%）下的基础抖动（典型值 1-2ms），ρ 为当前链路带宽利用率。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

queueing theory delay variance utilization relationship M/M/1
