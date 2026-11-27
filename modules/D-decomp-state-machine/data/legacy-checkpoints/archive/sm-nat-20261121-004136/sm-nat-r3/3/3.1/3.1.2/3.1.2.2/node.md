# N115: B_total 的边界条件验证：若假设热度与大小独立（ρ=0），则 B_total = R_daily * E[S] = 50,000,000 * 9.35KB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

B_total 的边界条件验证：若假设热度与大小独立（ρ=0），则 B_total = R_daily * E[S] = 50,000,000 * 9.35KB ≈ 467.5 TB/天。此值作为分母的上界参考。在负相关场景下，实际 B_total 低于此值，导致命中率分母减小，可能部分抵消分子减小带来的命中率下降，需联合 N76 和 N77 评估净效应。

## Corrected Claim

B_total 的边界条件验证：若假设热度与大小独立（ρ=0），则 B_total = R_daily * E[S] = 50,000,000 * 9.35KB ≈ 467.5 TB/天。此值作为分母的上界参考。在负相关场景下，实际 B_total 低于此值，导致命中率分母减小，可能部分抵消分子减小带来的命中率下降，需联合 N76 和 N77 评估净效应。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 50,000,000 * 9.35KB ≈ 467.5TB 准确，且基于独立性假设推导上界的逻辑自洽。
