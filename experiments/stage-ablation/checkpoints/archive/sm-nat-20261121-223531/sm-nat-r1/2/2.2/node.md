# N11: LRU 工作点 1（高性低成）：假设 ρ=0（独立性），计算基准命中率 H_base = 1 - ∫_{s_min}^{s_max} (s/E[S]_trunc

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

LRU 工作点 1（高性低成）：假设 ρ=0（独立性），计算基准命中率 H_base = 1 - ∫_{s_min}^{s_max} (s/E[S]_trunc) * f_S(s) * (1 - F_H(h_median)) ds，其中 h_median 为热度中位数，此工作点提供命中率下界，计算复杂度低，误差范围 [待核验] ±5%。

## Corrected Claim

LRU 工作点 1（高性低成）：假设 ρ=0（独立性），计算基准命中率 H_base 的简化模型，该模型提供命中率下界，计算复杂度低，具体误差范围需根据实际负载分布进一步评估。

## Evidence

[质询]公式中 (1 - F_H(h_median)) 在 ρ=0（独立性）假设下恒等于 0.5，导致 H_base 退化为 0.5 * (1 - ∫(s/E[S]_trunc)f_S(s)ds)，这与 LRU 缓存命中率的标准理论模型（通常涉及访问间隔分布或 Zipf 分布的累积概率）不符，且 '±5%' 的误差范围缺乏理论推导或实证数据支持，属于未经验证的断言。 | 先验知识/题面给定，逻辑校验通过但公式推导存在理论争议且误差范围无来源支持，降级为定性表述。

## Search Query

LRU cache hit rate independent size popularity pareto approximation
