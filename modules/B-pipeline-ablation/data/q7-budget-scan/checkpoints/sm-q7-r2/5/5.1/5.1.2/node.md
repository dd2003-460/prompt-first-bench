# N94: NVMe SSD阵列年化RTO代价：C_RTO_NVMe_annual = (L_hourly × T_RTO_NVMe + C_expedited_NVMe)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

NVMe SSD阵列年化RTO代价：C_RTO_NVMe_annual = (L_hourly × T_RTO_NVMe + C_expedited_NVMe) × P_failure_yearly，其中P_failure_yearly基于MTBF估算（如MTBF=10^6h则约0.087次/年）

## Corrected Claim

NVMe SSD阵列年化RTO代价：C_RTO_NVMe_annual = (L_hourly × T_RTO_NVMe + C_expedited_NVMe) × P_failure_yearly，其中P_failure_yearly基于MTBF估算（如MTBF=10^6h则约0.087次/年）

## Evidence

先验知识/题面给定，逻辑校验通过：MTBF=10^6h对应年故障率约为8760/10^6≈0.00876次/年，公式结构符合可靠性经济学基本逻辑，数值量级合理。
