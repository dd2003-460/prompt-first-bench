# N233: 计算LFU在Pareto(β=0.9)分布下的稳态字节命中率 H_byte_LFU，公式为 H_byte_LFU = (Σ_{i=1}^{K} p_i s_i)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N88

## Claim

计算LFU在Pareto(β=0.9)分布下的稳态字节命中率 H_byte_LFU，公式为 H_byte_LFU = (Σ_{i=1}^{K} p_i s_i) / S_total - ε_LFU，其中ε_LFU基于频率老化模型估算（通常小于ε_LRU）。

## Corrected Claim

计算LFU在Pareto(β=0.9)分布下的稳态字节命中率 H_byte_LFU，公式为 H_byte_LFU = (Σ_{i=1}^{K} p_i s_i) / S_total - ε_LFU，其中ε_LFU基于频率老化模型估算（通常小于ε_LRU）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU steady state byte hit rate formula under Zipf distribution with frequency aging penalty
