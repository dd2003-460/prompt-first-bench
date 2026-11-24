# N94: NVMe SSD阵列年化RTO代价：C_RTO_NVMe_annual = (L_hourly × T_RTO_NVMe + C_expedited_NVMe)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

NVMe SSD阵列年化RTO代价：C_RTO_NVMe_annual = (L_hourly × T_RTO_NVMe + C_expedited_NVMe) × P_failure_yearly，其中P_failure_yearly基于MTBF估算（如MTBF=10^6h则约0.087次/年）

## Corrected Claim

NVMe SSD阵列年化RTO代价：C_RTO_NVMe_annual = (L_hourly × T_RTO_NVMe + C_expedited_NVMe) × P_failure_yearly，其中P_failure_yearly基于MTBF估算（如MTBF=10^6h则约0.087次/年）

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点公式中的 P_failure_yearly、L_hourly 和 C_expedited_NVMe 三个独立变量，彼此之间无重叠或矛盾。虽然 P_failure_yearly 的计算提供了两种口径（单盘故障 vs 数据丢失），但这属于同一变量在不同语义下的定义澄清，并未引入新的独立维度，因此不构成冗余。所有关键组成部分均已覆盖。）
