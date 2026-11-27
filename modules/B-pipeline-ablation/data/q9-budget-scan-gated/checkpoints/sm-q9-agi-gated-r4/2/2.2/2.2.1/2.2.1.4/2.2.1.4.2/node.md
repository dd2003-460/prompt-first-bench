# N137: 总Prefill延迟的闭式解推导：基于等差数列求和公式，Σ_{i=1}^{k} c*(2k + (i-1)*1.5k) = c * [2k*k + 1.5k *

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

总Prefill延迟的闭式解推导：基于等差数列求和公式，Σ_{i=1}^{k} c*(2k + (i-1)*1.5k) = c * [2k*k + 1.5k * k(k-1)/2] = c * k * (2k + 0.75k(k-1))，代入E[k]=4.6可得具体数值倍数关系。

## Corrected Claim

总Prefill延迟的闭式解推导：基于等差数列求和公式，Σ_{i=1}^{k} c*(2k + (i-1)*1.5k) = c * [2k*k + 1.5k * k(k-1)/2] = c * k * (2k + 0.75k(k-1))，代入E[k]=4.6可得具体数值倍数关系。

## Evidence

先验知识/题面给定，逻辑校验通过：代数推导 Σ_{i=1}^{k} c(2k + 1.5k(i-1)) = c[2k^2 + 1.5k * k(k-1)/2] = ck(2k + 0.75k(k-1)) 正确，量纲与系数符合等差数列求和公式。
