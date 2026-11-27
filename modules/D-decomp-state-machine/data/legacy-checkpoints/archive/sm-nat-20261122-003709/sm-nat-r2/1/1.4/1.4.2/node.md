# N36: 推导累积请求频率 F(k) 的闭式解：F(k) = (Σ_{i=1}^{k} i^{-β}) / Z_β ≈ (k^{1-β}/(1-β) + 0.5) / Z

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

推导累积请求频率 F(k) 的闭式解：F(k) = (Σ_{i=1}^{k} i^{-β}) / Z_β ≈ (k^{1-β}/(1-β) + 0.5) / Z_β，该公式用于反解 k_90

## Corrected Claim

推导累积请求频率 F(k) 的闭式解：F(k) = (Σ_{i=1}^{k} i^{-β}) / Z_β ≈ (k^{1-β}/(1-β) + 0.5) / Z_β，该公式用于反解 k_90

## Evidence

先验知识/题面给定，逻辑校验通过：基于欧拉-麦克劳林公式（Euler-Maclaurin summation），当 β > 1 时，Σ_{i=1}^{k} i^{-β} 的渐近展开确实为 k^{1-β}/(1-β) + 1/2 + O(k^{-β})，公式推导符合数学原理。
