# N125: 计算字节命中率修正因子R_byte的解析表达式：R_byte = E[S|Hit] / E[S|Miss]，需分别计算命中集合（前K个对象）与未命中集合（剩余N

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N40

## Claim

计算字节命中率修正因子R_byte的解析表达式：R_byte = E[S|Hit] / E[S|Miss]，需分别计算命中集合（前K个对象）与未命中集合（剩余N-K个对象）的条件期望大小，而非简单使用全局E[S]，以避免分母偏差。

## Corrected Claim

计算字节命中率修正因子R_byte的解析表达式：R_byte = E[S|Hit] / E[S|Miss]，需分别计算命中集合（前K个对象）与未命中集合（剩余N-K个对象）的条件期望大小，而非简单使用全局E[S]，以避免分母偏差。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

byte hit rate correction factor conditional expectation hit miss set CDN
