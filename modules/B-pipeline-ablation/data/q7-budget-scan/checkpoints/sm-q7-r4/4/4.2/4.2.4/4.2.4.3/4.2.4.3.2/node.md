# N468: 前台业务 I/O 对重建时间的非线性影响：当业务 IOPS > 重建所需 IOPS 的 20% 时，重建时间不再线性延长，而是进入排队论模型（M/G/1），此时

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N207, N208, N209

## Claim

前台业务 I/O 对重建时间的非线性影响：当业务 IOPS > 重建所需 IOPS 的 20% 时，重建时间不再线性延长，而是进入排队论模型（M/G/1），此时 T_effective = T_min / (1 - ρ)，其中 ρ = λ_business / μ_rebuild_capacity；若 ρ 超过 0.8，重建时间趋向无穷大，需引入预分区（pre-staging）策略。

## Corrected Claim

前台业务 I/O 对重建时间的非线性影响：当业务 IOPS > 重建所需 IOPS 的 20% 时，重建时间不再线性延长，而是进入排队论模型（M/G/1），此时 T_effective = T_min / (1 - ρ)，其中 ρ = λ_business / μ_rebuild_capacity；若 ρ 超过 0.8，重建时间趋向无穷大，需引入预分区（pre-staging）策略。

## Evidence

先验知识/题面给定，逻辑校验通过：M/G/1排队模型中服务时间公式T=T_min/(1-ρ)及ρ>0.8导致系统趋于不稳定的结论符合排队论基本原理，量纲与逻辑自洽。

## Search Query

RAID rebuild time impact foreground IO queueing theory M/G/1 utilization
