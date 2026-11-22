# N103: 有效命中率折扣因子 D_update 的精确表达式：D_update = 1 - (Σ_{i∈S_LRU} p_i s_i P_invalid(i)) / (Σ

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

有效命中率折扣因子 D_update 的精确表达式：D_update = 1 - (Σ_{i∈S_LRU} p_i s_i P_invalid(i)) / (Σ_{i∈S_LRU} p_i s_i)，其中分子为因更新失效而丢失的字节加权访问概率，分母为缓存内总字节加权访问概率。

## Corrected Claim

有效命中率折扣因子 D_update 的精确表达式：D_update = 1 - (Σ_{i∈S_LRU} p_i s_i P_invalid(i)) / (Σ_{i∈S_LRU} p_i s_i)，其中分子为因更新失效而丢失的字节加权访问概率，分母为缓存内总字节加权访问概率。

## Evidence

先验知识/题面给定，逻辑校验通过
