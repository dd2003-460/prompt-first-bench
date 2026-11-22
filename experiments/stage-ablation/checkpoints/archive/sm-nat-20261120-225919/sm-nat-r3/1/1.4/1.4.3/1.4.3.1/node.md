# N127: S_cumulative(k) 的近似公式 S_min * k^α/(α-1) 仅在对象大小独立于热度（ρ=0）时成立；当 ρ=-0.3 时，前 k 个最热对象

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

S_cumulative(k) 的近似公式 S_min * k^α/(α-1) 仅在对象大小独立于热度（ρ=0）时成立；当 ρ=-0.3 时，前 k 个最热对象的平均大小显著小于总体平均，需引入修正因子 C_corr < 1 以降低累积大小。

## Corrected Claim

S_cumulative(k) 的近似公式 S_min * k^α/(α-1) 仅在对象大小独立于热度（ρ=0）时成立；当 ρ=-0.3 时，前 k 个最热对象的平均大小显著小于总体平均，需引入修正因子 C_corr < 1 以降低累积大小。

## Evidence

先验知识/题面给定，逻辑校验通过：当对象大小与热度负相关（ρ<0）时，高热度对象倾向于较小，导致前k个最热对象的累积大小小于独立假设下的理论值，因此修正因子C_corr<1符合直觉与数学逻辑。
