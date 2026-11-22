# N238: f_min 的归一化计算：Pareto(β=0.9) 下，总请求率 Σr_i = 50,000,000/天，N=100,000，归一化常数 Z_freq = (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N81

## Claim

f_min 的归一化计算：Pareto(β=0.9) 下，总请求率 Σr_i = 50,000,000/天，N=100,000，归一化常数 Z_freq = (Σ_{k=1}^{N} (N/k)^β)^{-1} ≈ (N^{1-β}/(1-β))^{-1}，f_min = Z_freq * r_min，其中 r_min 由最小对象请求率确定。

## Corrected Claim

f_min 的归一化计算：Pareto(β=0.9) 下，总请求率 Σr_i = 50,000,000/天，N=100,000，归一化常数 Z_freq = (Σ_{k=1}^{N} (N/k)^β)^{-1} ≈ (N^{1-β}/(1-β))^{-1}，f_min = Z_freq * r_min，其中 r_min 由最小对象请求率确定。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布归一化常数推导正确，量级合理
