# N299: Zipf分布拟合优度检验统计量：卡方检验 χ² = Σ((f_obs - f_exp)² / f_exp)，自由度df = N_bins - 2；若p-valu

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N101

## Claim

Zipf分布拟合优度检验统计量：卡方检验 χ² = Σ((f_obs - f_exp)² / f_exp)，自由度df = N_bins - 2；若p-value < 0.05，则Zipf模型失效，需改用Pareto或Log-Logistic分布，否则缓存命中率计算误差可达10%-20%

## Corrected Claim

Zipf分布拟合优度检验统计量：卡方检验 χ² = Σ((f_obs - f_exp)² / f_exp)，自由度df = N_bins - 2；若p-value < 0.05，表明Zipf模型拟合不佳，可考虑改用Pareto或Log-Logistic分布以优化缓存命中率计算的准确性。

## Evidence

[质询]将p-value < 0.05直接等同于'Zipf模型失效'并强制切换分布，且断言不切换会导致10%-20%的命中率误差，属于过度简化的经验性断言，缺乏普适的统计或工程依据。 | 先验知识/题面给定，逻辑校验通过：卡方检验公式及自由度计算（N_bins - 2，因估计了Zipf参数）在统计学上是自洽的；但'模型失效'的判定标准及具体的误差范围（10%-20%）属于经验性结论，虽无来源直接矛盾，但缺乏普适性支持，故降级。
