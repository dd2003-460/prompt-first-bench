# N65: 最小可检测效应量 (MDE) 公式：MDE = (Z_{α/2} + Z_{β}) * σ / √n，其中 α=0.05 (Z=1.96), β=0.80 (Z

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

最小可检测效应量 (MDE) 公式：MDE = (Z_{α/2} + Z_{β}) * σ / √n，其中 α=0.05 (Z=1.96), β=0.80 (Z=0.84), σ 为结果变量标准差, n 为样本量；若观测效应 < MDE，则统计功效不足，置信度标记为 [待核验]。

## Corrected Claim

最小可检测效应量 (MDE) 公式：MDE = (Z_{α/2} + Z_{β}) * σ / √n，其中 α=0.05 (Z=1.96), β=0.80 (Z=0.84), σ 为结果变量标准差, n 为样本量；若观测效应 < MDE，则统计功效不足，置信度标记为 [待核验]。

## Evidence

父节点级核验未通过：不完备（子节点覆盖了公式中的关键变量 σ 和 n，但遗漏了 Z 值（显著性水平和统计功效）的设定依据及潜在调整（如单尾/双尾检验），导致对父节点中参数定义的覆盖不完备。）

## Search Query

Minimum detectable effect MDE formula power analysis
