# N239: 约束失效的临界阈值：若 R_base ≥ 1.0%，则任何正向 ΔR 都会导致 R_new > 1%，约束极难满足。此时需采用分阶段干预，先监控 ΔR，再逐步调

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

约束失效的临界阈值：若 R_base ≥ 1.0%，则任何正向 ΔR 都会导致 R_new > 1%，约束极难满足。此时需采用分阶段干预，先监控 ΔR，再逐步调整 β_exposure。

## Corrected Claim

约束失效的临界阈值：若 R_base ≥ 1.0%，则任何正向 ΔR 都会导致 R_new > 1%，约束极难满足。此时需采用分阶段干预，先监控 ΔR，再逐步调整 β_exposure。

## Evidence

先验知识/题面给定，逻辑校验通过：若 R_base ≥ 1.0% 且 ΔR > 0，则 R_new = R_base + ΔR > 1.0%，数学推导成立，约束确实极难满足，分阶段干预策略符合逻辑。

## Search Query

complaint rate constraint threshold phased intervention
