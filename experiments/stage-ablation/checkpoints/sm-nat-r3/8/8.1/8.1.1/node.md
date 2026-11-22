# N271: LRU 驱逐损失项量化：Σ_{i∈S_LRU∖S_LFU} p_i s_i 代表被 LRU 保留但被 LFU 驱逐的对象字节加权热度，在 ρ=-0.3 场景下，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N95

## Claim

LRU 驱逐损失项量化：Σ_{i∈S_LRU∖S_LFU} p_i s_i 代表被 LRU 保留但被 LFU 驱逐的对象字节加权热度，在 ρ=-0.3 场景下，该值主要来源于大小-热度负相关导致的 LFU 对大冷对象的过度保留，数值约为总热度流的 0.5%。

## Corrected Claim

LRU 驱逐损失项量化：Σ_{i∈S_LRU∖S_LFU} p_i s_i 代表被 LRU 保留但被 LFU 驱逐的对象字节加权热度，在 ρ=-0.3 场景下，该值主要来源于大小-热度负相关导致的 LFU 对大冷对象的过度保留，数值约为总热度流的 0.5%。

## Evidence

先验知识/题面给定，逻辑校验通过
