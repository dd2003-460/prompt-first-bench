# N80: 净现值 (NPV) 平衡点的计算公式：NPV = Σ [ (ΔR_platform_t - ΔR_Trust_t) / (1 + r)^t ]，其中 ΔR_Tr

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

净现值 (NPV) 平衡点的计算公式：NPV = Σ [ (ΔR_platform_t - ΔR_Trust_t) / (1 + r)^t ]，其中 ΔR_Trust_t 为第 t 期因留存率提升带来的额外佣金收入，r 为折现率（通常取 10%-15%），平衡点即 NPV = 0 时的时间 T_break_even，需迭代求解 T_break_even。

## Corrected Claim

净现值 (NPV) 平衡点的计算公式：NPV = Σ [ (ΔR_platform_t - ΔR_Trust_t) / (1 + r)^t ]，其中 ΔR_Trust_t 为第 t 期因留存率提升带来的额外佣金收入，r 为折现率（通常取 10%-15%），平衡点即 NPV = 0 时的时间 T_break_even，需迭代求解 T_break_even。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NPV break-even point platform intervention commission loss trust gain
