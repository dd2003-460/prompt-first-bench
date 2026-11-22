# N380: 工作点C (高成本低性/低效率型)：RTX 4090 W4 精度下，若内存利用率降至 30% (例如由于非对齐内存访问或频繁上下文切换)，实际 Tokens/s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N143

## Claim

工作点C (高成本低性/低效率型)：RTX 4090 W4 精度下，若内存利用率降至 30% (例如由于非对齐内存访问或频繁上下文切换)，实际 Tokens/s ≈ 22.4 Tokens/s，此时每美元吞吐量降至 0.014 Tokens/s/$，接近 N36 的原始估算，表明效率因子对最终性价比有决定性影响。

## Corrected Claim

工作点C (高成本低性/低效率型)：RTX 4090 W4 精度下，若内存利用率降至 30% (例如由于非对齐内存访问或频繁上下文切换)，实际 Tokens/s ≈ 22.4 Tokens/s，此时每美元吞吐量降至 0.014 Tokens/s/$，接近 N36 的原始估算，表明效率因子对最终性价比有决定性影响。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（22.4 Tokens/s ÷ 1600 $/GPU ≈ 0.014 Tokens/s/$），且符合高成本低效率场景下的性能退化逻辑。
