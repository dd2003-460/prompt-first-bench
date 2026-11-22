# N15: LFU 理论上限公式：H_byte_LFU_max = 1 - (Σ_{i∉Cache_LFU} p_i · s_i) / (Σ_{all} p_i · s_i

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LFU 理论上限公式：H_byte_LFU_max = 1 - (Σ_{i∉Cache_LFU} p_i · s_i) / (Σ_{all} p_i · s_i)，其中 Cache_LFU 为 LFU 保留的对象集合，需确定 LFU 在长尾负载下的保留策略。

## Corrected Claim

LFU 理论上限公式：H_byte_LFU_max = 1 - (Σ_{i∉Cache_LFU} p_i · s_i) / (Σ_{all} p_i · s_i)，其中 Cache_LFU 为 LFU 保留的对象集合，需确定 LFU 在长尾负载下的保留策略。

## Evidence

先验知识/题面给定，逻辑校验通过
