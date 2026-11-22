# N252: 计算修正因子 R_byte = E[S|Hit]/E[S]：代入 N97 和 N98 数值，R_byte = 8.5KB / 10KB = 0.85。该因子表明

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

计算修正因子 R_byte = E[S|Hit]/E[S]：代入 N97 和 N98 数值，R_byte = 8.5KB / 10KB = 0.85。该因子表明字节命中率比对象命中率高出约 17.6%（1/0.85 - 1），因为命中的对象更小，单位请求消耗的缓存字节更少。

## Corrected Claim

计算修正因子 R_byte = E[S|Hit]/E[S]：代入 N97 和 N98 数值，R_byte = 8.5KB / 10KB = 0.85。该因子表明字节命中率比对象命中率高出约 17.6%（1/0.85 - 1），因为命中的对象更小，单位请求消耗的缓存字节更少。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 8.5/10=0.85 正确，相对提升 (1/0.85-1)≈17.6% 正确，逻辑推导自洽。
