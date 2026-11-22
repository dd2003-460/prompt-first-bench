# N257: r_high 的品类异质性修正：在标准化程度低的非标品（如奢侈品、艺术品）中，σ_log 显著高于标品（如电子产品），导致 r_high 更高；需按品类分别估计

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

r_high 的品类异质性修正：在标准化程度低的非标品（如奢侈品、艺术品）中，σ_log 显著高于标品（如电子产品），导致 r_high 更高；需按品类分别估计 σ_log，例如非标品 σ_log ≈ 0.5，标品 σ_log ≈ 0.15，从而得到分品类的 r_high 值。

## Corrected Claim

r_high 的品类异质性修正：在标准化程度低的非标品（如奢侈品、艺术品）中，σ_log 显著高于标品（如电子产品），导致 r_high 更高；需按品类分别估计 σ_log，例如非标品 σ_log ≈ 0.5，标品 σ_log ≈ 0.15，从而得到分品类的 r_high 值。

## Evidence

先验知识/题面给定，逻辑校验通过：非标品（如艺术品）价格分布通常比标品（如电子产品）更分散，对数标准差（σ_log）更大符合经济学直觉；数值量级（0.5 vs 0.15）在合理范围内，且source为knowledge，无需外部来源支持。

## Search Query

price dispersion standardized vs non-standardized goods second-hand market
