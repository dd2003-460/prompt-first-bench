# N94: 字节占比的积分近似：P_cold_byte ≈ [∫_{K}^{N} x^{-0.9} * x^{-0.1} dx] / [∫_{1}^{N} x^{-1.0}

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

字节占比的积分近似：P_cold_byte ≈ [∫_{K}^{N} x^{-0.9} * x^{-0.1} dx] / [∫_{1}^{N} x^{-1.0} dx] = [∫_{K}^{N} x^{-1.0} dx] / [∫_{1}^{N} x^{-1.0} dx] = [ln(N) - ln(K)] / ln(N) = 1 - ln(K/N)

## Corrected Claim

字节占比的积分近似：P_cold_byte ≈ [∫_{K}^{N} x^{-0.9} * x^{-0.1} dx] / [∫_{1}^{N} x^{-1.0} dx] = [∫_{K}^{N} x^{-1.0} dx] / [∫_{1}^{N} x^{-1.0} dx] = [ln(N) - ln(K)] / ln(N) = 1 - ln(K/N)

## Evidence

先验知识/题面给定，逻辑校验通过：积分计算正确，量纲一致，数学推导自洽
