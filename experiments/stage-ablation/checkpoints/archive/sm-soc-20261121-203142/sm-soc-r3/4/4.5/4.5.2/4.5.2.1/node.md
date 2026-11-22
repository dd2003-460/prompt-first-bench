# N214: 工作点A（低噪声/高一致性）：假设买家价值评估异质性标准差σ_V = 0.5 * P_market，则σ² = 0.25 * P_market²，需验证该σ²是

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

工作点A（低噪声/高一致性）：假设买家价值评估异质性标准差σ_V = 0.5 * P_market，则σ² = 0.25 * P_market²，需验证该σ²是否小于0.25 * Var(δ)（注意单位转换：Var(δ)为比例方差，σ²为金额方差，需统一归一化后比较）。

## Corrected Claim

工作点A（低噪声/高一致性）：假设买家价值评估异质性标准差σ_V = 0.5 * P_market，则σ² = 0.25 * P_market²，需验证该σ²是否小于0.25 * Var(δ)（注意单位转换：Var(δ)为比例方差，σ²为金额方差，需统一归一化后比较）。

## Evidence

先验知识/题面给定，逻辑校验通过：σ_V = 0.5 * P_market 推导出的 σ² = 0.25 * P_market² 在代数上正确，且陈述中明确指出了金额方差与比例方差比较时需进行归一化处理的逻辑前提，无内部矛盾。

## Search Query

buyer valuation heterogeneity standard deviation normalized
