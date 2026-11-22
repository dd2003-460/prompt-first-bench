# N70: 加权均价 Σ(w_i * P_i) 中权重 w_i 的确定方法：w_i 应基于商品相似度（如品牌、型号、成色）和近期成交频率，需定义相似度度量函数 sim(i,

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

加权均价 Σ(w_i * P_i) 中权重 w_i 的确定方法：w_i 应基于商品相似度（如品牌、型号、成色）和近期成交频率，需定义相似度度量函数 sim(i, j) 及 w_i = sim(i, j) / Σ_k sim(i, k) 的具体形式。

## Corrected Claim

加权均价 Σ(w_i * P_i) 中权重 w_i 的确定方法：w_i 应基于商品相似度（如品牌、型号、成色）和近期成交频率，需定义相似度度量函数 sim(i, j) 及 w_i = sim(i, j) / Σ_k sim(i, k) 的具体形式。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

weighted average price calculation method for similar items in marketplace pricing algorithm
