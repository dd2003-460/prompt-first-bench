# N234: 计算LRU在Pareto(β=0.9)分布下的稳态字节命中率 H_byte_LRU，公式为 H_byte_LRU = (Σ_{i=1}^{K} p_i s_i)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N88

## Claim

计算LRU在Pareto(β=0.9)分布下的稳态字节命中率 H_byte_LRU，公式为 H_byte_LRU = (Σ_{i=1}^{K} p_i s_i) / S_total - ε_LRU，其中ε_LRU基于时间局部性损失估算（通常2-5%）。

## Corrected Claim

计算LRU在Pareto(β=0.9)分布下的稳态字节命中率 H_byte_LRU，公式为 H_byte_LRU = (Σ_{i=1}^{K} p_i s_i) / S_total - ε_LRU，其中ε_LRU基于时间局部性损失估算（通常2-5%）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU steady state byte hit rate formula under Zipf distribution with temporal locality penalty
