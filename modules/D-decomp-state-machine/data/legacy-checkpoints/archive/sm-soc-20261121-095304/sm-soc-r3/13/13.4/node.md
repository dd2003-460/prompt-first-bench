# N209: 算法惩罚假设下的替代分布参数 μ_penalty：假设算法惩罚导致曝光权重乘以 (1-β_suppress)，则 μ_penalty = μ_theoretic

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

算法惩罚假设下的替代分布参数 μ_penalty：假设算法惩罚导致曝光权重乘以 (1-β_suppress)，则 μ_penalty = μ_theoretical * (1-β_suppress)，需结合 N35 中的 β_suppress 范围 (0.2-0.4) 计算 μ_penalty 的具体区间，以构建备择假设的对数似然值 ln(L_alt)。

## Corrected Claim

算法惩罚假设下的替代分布参数 μ_penalty：假设算法惩罚导致曝光权重乘以 (1-β_suppress)，则 μ_penalty = μ_theoretical * (1-β_suppress)，需结合 N35 中的 β_suppress 范围 (0.2-0.4) 计算 μ_penalty 的具体区间，以构建备择假设的对数似然值 ln(L_alt)。

## Evidence

先验知识/题面给定，逻辑校验通过
