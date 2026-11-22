# N138: 在理想无开销工作点下，Cache 包含全部对象，分子项 Σ_{i∉Cache} p_i · s_i = 0，LRU 字节命中率 H_byte_LRU = 1 -

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

在理想无开销工作点下，Cache 包含全部对象，分子项 Σ_{i∉Cache} p_i · s_i = 0，LRU 字节命中率 H_byte_LRU = 1 - 0/E[S] = 100%。

## Corrected Claim

在理想无开销工作点下，Cache 包含全部对象，分子项 Σ_{i∉Cache} p_i · s_i = 0，LRU 字节命中率 H_byte_LRU = 1 - 0/E[S] = 100%。

## Evidence

先验知识/题面给定，逻辑校验通过：若Cache包含全部对象，则未命中集合为空，未命中字节数为0，命中率公式 1 - 0/E[S] 逻辑上必然等于100%。
