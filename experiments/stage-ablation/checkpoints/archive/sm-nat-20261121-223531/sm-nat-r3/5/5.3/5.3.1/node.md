# N67: 在忽略大小-热度相关性（ρ=0）的独立性假设下，LRU字节命中率下界 $H_{LRU, base}$ 的计算公式为 $1 - \frac{\sum_{i \in

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

在忽略大小-热度相关性（ρ=0）的独立性假设下，LRU字节命中率下界 $H_{LRU, base}$ 的计算公式为 $1 - \frac{\sum_{i \in \text{evicted}} S_i}{\sum_{j=1}^{N} S_j \cdot H_j}$，其中 $S_i$ 为对象大小，$H_j$ 为对象热度权重，该模型作为保守估计的下界，具体数值需基于N22确定的缓存容量和N23确定的热度分布进行数值积分求解。

## Corrected Claim

在忽略大小-热度相关性（ρ=0）的独立性假设下，LRU字节命中率下界 $H_{LRU, base}$ 的计算公式为 $1 - \frac{\sum_{i \in \text{evicted}} S_i}{\sum_{j=1}^{N} S_j \cdot H_j}$，其中 $S_i$ 为对象大小，$H_j$ 为对象热度权重，该模型作为保守估计的下界，具体数值需基于N22确定的缓存容量和N23确定的热度分布进行数值积分求解。

## Evidence

父节点级核验失败（LLM 错误）：Invalid \escape: line 5 column 173 (char 239)
