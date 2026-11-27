# N143: 最小样本量 $N_{min}$ 的解析解：在效应量 $\delta = |\ln(P(Data|H_i)/P(Data|H_j))|$ 已知且检验力 $\bet

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

最小样本量 $N_{min}$ 的解析解：在效应量 $\delta = |\ln(P(Data|H_i)/P(Data|H_j))|$ 已知且检验力 $\beta=0.8$ 的条件下，$N_{min} = \frac{(Z_{\alpha/2} + Z_{\beta})^2 \cdot 2\sigma^2}{\delta^2}$，其中 $\sigma^2$ 为似然比观测值的方差，$Z_{\alpha/2}=1.96, Z_{\beta}=0.84$；若 $\delta$ 未知，需先通过 pilot 数据估计。

## Corrected Claim

最小样本量 $N_{min}$ 的解析解：在效应量 $\delta = |\ln(P(Data|H_i)/P(Data|H_j))|$ 已知且检验力 $\beta=0.8$ 的条件下，$N_{min} = \frac{(Z_{\alpha/2} + Z_{\beta})^2 \cdot 2\sigma^2}{\delta^2}$，其中 $\sigma^2$ 为似然比观测值的方差，$Z_{\alpha/2}=1.96, Z_{\beta}=0.84$；若 $\delta$ 未知，需先通过 pilot 数据估计。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合基于正态近似的大样本统计检验力计算标准形式（N ∝ (Zα+Zβ)²σ²/δ²），量纲与数值量级合理。
