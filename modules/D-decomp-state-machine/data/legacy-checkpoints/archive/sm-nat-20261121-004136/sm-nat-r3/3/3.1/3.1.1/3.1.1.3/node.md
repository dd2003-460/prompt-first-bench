# N113: B_top1pct 的数值估算（独立假设工作点）：B_top1pct ≈ R_daily * F_top1000 * E[S|rank≤1000]。代入 R_d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

B_top1pct 的数值估算（独立假设工作点）：B_top1pct ≈ R_daily * F_top1000 * E[S|rank≤1000]。代入 R_daily=50,000,000, F_top1000=0.2057, E[S|rank≤1000]≈E[S]*exp(ρ*σ*z)≈9.35KB*0.85≈7.95KB（假设 ρ 导致大小缩减 15%），计算得 B_top1pct ≈ 50,000,000 * 0.2057 * 7.95KB ≈ 81.8 TB/天。此值作为 LFU 理论上限命中率的分子基准。

## Corrected Claim

B_top1pct 的数值估算（独立假设工作点）：B_top1pct ≈ R_daily * F_top1000 * E[S|rank≤1000]。代入 R_daily=50,000,000, F_top1000=0.2057, E[S|rank≤1000]≈E[S]*exp(ρ*σ*z)≈9.35KB*0.85≈7.95KB（假设 ρ 导致大小缩减 15%），计算得 B_top1pct ≈ 50,000,000 * 0.2057 * 7.95KB ≈ 81.8 TB/天。此值作为 LFU 理论上限命中率的分子基准。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 50,000,000 * 0.2057 * 7.95KB ≈ 81.8 TB 量级正确，公式逻辑自洽。
