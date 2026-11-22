# N126: 边界对象集合 $S_{boundary}$ 的字节流量占比 $R_{boundary}$ 计算公式：$R_{boundary} = \frac{\sum_{i 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

边界对象集合 $S_{boundary}$ 的字节流量占比 $R_{boundary}$ 计算公式：$R_{boundary} = \frac{\sum_{i \in S_{boundary}} S_i \times H_i}{\sum_{j=1}^{N} S_j \times H_j}$。在Pareto(β=0.9)分布下，若缓存容量 $C_{obj}$ 接近工作集大小，该比例通常落在 5%-10% 区间，具体数值取决于 $S_i$ 和 $H_i$ 的联合分布尾部特征。

## Corrected Claim

边界对象集合 $S_{boundary}$ 的字节流量占比 $R_{boundary}$ 计算公式：$R_{boundary} = \frac{\sum_{i \in S_{boundary}} S_i \times H_i}{\sum_{j=1}^{N} S_j \times H_j}$。在Pareto(β=0.9)分布下，若缓存容量 $C_{obj}$ 接近工作集大小，该比例通常落在 5%-10% 区间，具体数值取决于 $S_i$ 和 $H_i$ 的联合分布尾部特征。

## Evidence

先验知识/题面给定，逻辑校验通过
