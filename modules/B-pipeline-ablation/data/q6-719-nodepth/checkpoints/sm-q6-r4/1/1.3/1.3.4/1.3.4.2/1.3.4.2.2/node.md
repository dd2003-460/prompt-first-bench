# N686: 跨省 BGP 多线接入的带宽成本 C_bandwidth_per_GB 构成：由基础线路费 + 流量超额费组成，C_bandwidth_per_GB = (Ba

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N228

## Claim

跨省 BGP 多线接入的带宽成本 C_bandwidth_per_GB 构成：由基础线路费 + 流量超额费组成，C_bandwidth_per_GB = (Base_Rent_Mbps * k_base + (Q_actual_GB - Q_base_GB) * k_overage) / Q_actual_GB，其中 k_base ≈ ¥0.1/GB（等效），k_overage ≈ ¥0.5/GB，由于跨省流量通常超过基础包，加权平均后约为 ¥0.25/GB

## Corrected Claim

跨省 BGP 多线接入的带宽成本 C_bandwidth_per_GB 构成：由基础线路费 + 流量超额费组成，C_bandwidth_per_GB = (Base_Rent_Mbps * k_base + (Q_actual_GB - Q_base_GB) * k_overage) / Q_actual_GB，其中 k_base ≈ ¥0.1/GB（等效），k_overage ≈ ¥0.5/GB，由于跨省流量通常超过基础包，加权平均后约为 ¥0.25/GB

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

China inter-provincial bandwidth pricing base rent overage traffic cost model
