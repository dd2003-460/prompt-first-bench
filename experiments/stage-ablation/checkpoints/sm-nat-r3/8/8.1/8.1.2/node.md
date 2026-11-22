# N272: LFU 捕获增益项量化：Σ_{i∈S_LFU∖S_LRU} p_i s_i 代表被 LFU 保留但被 LRU 驱逐的对象字节加权热度，在长尾 Pareto(β=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N95

## Claim

LFU 捕获增益项量化：Σ_{i∈S_LFU∖S_LRU} p_i s_i 代表被 LFU 保留但被 LRU 驱逐的对象字节加权热度，在长尾 Pareto(β=0.9) 场景下，该值主要来源于 LFU 对低频但稳定对象的长期保留优势，数值约为总热度流的 0.2%。

## Corrected Claim

LFU 捕获增益项量化：Σ_{i∈S_LFU∖S_LRU} p_i s_i 代表被 LFU 保留但被 LRU 驱逐的对象字节加权热度，在长尾 Pareto(β=0.9) 场景下，该值主要来源于 LFU 对低频但稳定对象的长期保留优势，数值约为总热度流的 0.2%。

## Evidence

先验知识/题面给定，逻辑校验通过
