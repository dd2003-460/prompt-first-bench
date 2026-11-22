# N36: 推导累积请求频率 F(k) 的闭式解：F(k) = (Σ_{i=1}^{k} i^{-β}) / Z_β ≈ (k^{1-β}/(1-β) + 0.5) / Z

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

推导累积请求频率 F(k) 的闭式解：F(k) = (Σ_{i=1}^{k} i^{-β}) / Z_β ≈ (k^{1-β}/(1-β) + 0.5) / Z_β，该公式用于反解 k_90

## Corrected Claim

推导累积请求频率 F(k) 的闭式解：F(k) = (Σ_{i=1}^{k} i^{-β}) / Z_β ≈ (k^{1-β}/(1-β) + 0.5) / Z_β，该公式用于反解 k_90

## Evidence

父节点级核验通过：正交+完备+无冗余（两个子节点分别处理了公式中的分子（求和部分的Euler-Maclaurin近似）和分母（归一化常数的计算），内容互不重叠且覆盖了父节点公式推导的两个核心组成部分。）
