# N17: 请求热度Pareto参数β=0.9对应的Zipf-like分布归一化常数C_β = 1 / (Σ_{i=1}^{N} i^{-β})，由于β<1，该和式近似为N

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

请求热度Pareto参数β=0.9对应的Zipf-like分布归一化常数C_β = 1 / (Σ_{i=1}^{N} i^{-β})，由于β<1，该和式近似为N^{1-β}/(1-β)，因此第i热门对象的请求概率p_i ≈ (1-β) * i^{-β} * N^{β-1}，该公式是计算LRU稳态命中率的理论基线。

## Corrected Claim

请求热度Pareto参数β=0.9对应的Zipf-like分布归一化常数C_β = 1 / (Σ_{i=1}^{N} i^{-β})，由于β<1，该和式近似为N^{1-β}/(1-β)，因此第i热门对象的请求概率p_i ≈ (1-β) * i^{-β} * N^{β-1}，该公式是计算LRU稳态命中率的理论基线。

## Evidence

先验知识/题面给定，逻辑校验通过：Zipf分布归一化常数推导及LRU稳态命中率理论基线符合数学定义与缓存理论常识。
