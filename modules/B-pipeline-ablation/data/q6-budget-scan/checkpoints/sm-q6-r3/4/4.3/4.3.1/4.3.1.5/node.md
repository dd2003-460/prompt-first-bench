# N250: 带宽冗余系数 $K_{redundancy}$：为应对链路故障，通常需预留 1.5-2 倍于峰值需求的带宽容量，实际采购带宽 $B_{procured} = K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85, N86, N87

## Claim

带宽冗余系数 $K_{redundancy}$：为应对链路故障，通常需预留 1.5-2 倍于峰值需求的带宽容量，实际采购带宽 $B_{procured} = K_{redundancy} \times B_{peak}$，这将导致固定带宽成本增加 50%-100%。

## Corrected Claim

带宽冗余系数 $K_{redundancy}$：为应对链路故障，通常需预留 1.5-2 倍于峰值需求的带宽容量，实际采购带宽 $B_{procured} = K_{redundancy} \times B_{peak}$，这将导致固定带宽成本增加 50%-100%。

## Evidence

先验知识/题面给定，逻辑校验通过：1.5-2倍冗余系数对应50%-100%成本增加，数学关系自洽，符合网络工程常见经验值。

## Search Query

network redundancy bandwidth oversubscription factor edge nodes
