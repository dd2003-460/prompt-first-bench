# N376: 高信号卖家溢价率分布：该群体平均溢价率 > 20% 的断言需分解为均值与方差。若溢价率标准差 σ_premium > 10%，则存在部分高信号卖家溢价率 < 1

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N120

## Claim

高信号卖家溢价率分布：该群体平均溢价率 > 20% 的断言需分解为均值与方差。若溢价率标准差 σ_premium > 10%，则存在部分高信号卖家溢价率 < 15%，需进一步分析这部分卖家的行为是否与低信号卖家无显著差异（t-test p-value < 0.05）。

## Corrected Claim

高信号卖家溢价率分布分析：若该群体平均溢价率显著高于基准（如 > 20%），需分解为均值与方差。若溢价率标准差较大（如 σ > 10%），则可能存在部分高信号卖家溢价率较低（如 < 15%），建议进一步通过统计检验（如 t-test）分析这部分卖家的行为是否与低信号卖家存在显著差异。

## Evidence

[质询]该陈述包含具体的统计阈值（σ > 10%, p < 0.05）和群体特征断言（平均溢价率 > 20%），属于经验事实。在无外部来源支持的情况下，无法验证这些具体数值是否真实反映了“高信号卖家”的实际分布情况，存在将假设性分析框架误当作已验证事实的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

premium rate distribution high signal sellers second hand market variance standard deviation
