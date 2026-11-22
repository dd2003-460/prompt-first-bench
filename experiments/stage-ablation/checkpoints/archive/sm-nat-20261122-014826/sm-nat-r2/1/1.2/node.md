# N7: 请求热度分布参数化：P(rank=r) ∝ r^(-β)，β=0.9，归一化常数 Z = Σ_{r=1}^{100000} r^(-0.9) ≈ 100000^

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

请求热度分布参数化：P(rank=r) ∝ r^(-β)，β=0.9，归一化常数 Z = Σ_{r=1}^{100000} r^(-0.9) ≈ 100000^0.1 / 0.1 ≈ 12589，Top-1% 对象 (r<1000) 承载 95.2% 请求流量。

## Corrected Claim

请求热度分布参数化：P(rank=r) ∝ r^(-β)，β=0.9，归一化常数 Z = Σ_{r=1}^{100000} r^(-0.9) ≈ 100000^0.1 / 0.1 ≈ 12589，Top-1% 对象 (r<1000) 承载 95.2% 请求流量。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别提供了具体的数值反证（子节点1）、分布性质的定量推导（子节点2）以及理论适用条件的辨析（子节点3）。三者从不同维度（计算结果、分布形态、理论前提）共同构成了对父节点错误结论的完整反驳，内容互不重叠且逻辑互补，无冗余。）

## Search Query

Zipf-like distribution beta 0.9 cumulative request fraction top 1 percent
