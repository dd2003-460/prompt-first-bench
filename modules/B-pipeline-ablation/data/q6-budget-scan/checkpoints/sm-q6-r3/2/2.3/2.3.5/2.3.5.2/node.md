# N192: 预留带宽 $B_{reserved, self}$ 的最优配置策略：为避免 $\rho_{self} > 0.8$ 导致的排队延迟激增，预留带宽应设为峰值回源带

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

预留带宽 $B_{reserved, self}$ 的最优配置策略：为避免 $\rho_{self} > 0.8$ 导致的排队延迟激增，预留带宽应设为峰值回源带宽的 1.5-2 倍，即 $B_{reserved, self} = (1-H) \times B_{peak} \times 1.5$，在 $H=90\%, B_{peak}=30\text{Gbps}$ 下，$B_{reserved, self} \approx 4.5\text{Gbps}$，对应 $\rho_{self} \approx 0.67$。

## Corrected Claim

预留带宽 $B_{reserved, self}$ 的最优配置策略：为避免 $\rho_{self} > 0.8$ 导致的排队延迟激增，预留带宽应设为峰值回源带宽的 1.5-2 倍，即 $B_{reserved, self} = (1-H) \times B_{peak} \times 1.5$，在 $H=90\%, B_{peak}=30\text{Gbps}$ 下，$B_{reserved, self} \approx 4.5\text{Gbps}$，对应 $\rho_{self} \approx 0.67$。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (1-0.9)*30*1.5=4.5 Gbps 正确，负载率 4.5/6.75=0.67 符合 M/M/1 队列理论中避免高延迟的合理区间（通常建议 <0.7-0.8），数值量级与工程直觉一致。
