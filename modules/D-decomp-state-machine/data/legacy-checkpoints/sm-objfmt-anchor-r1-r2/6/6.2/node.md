# N103: FP8 KV Cache 导致的注意力分数误差主要通过改变 Softmax 分布体现，其对最终生成 PPL 的影响机制是：量化噪声 δ 注入到 Attentio

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

FP8 KV Cache 导致的注意力分数误差主要通过改变 Softmax 分布体现，其对最终生成 PPL 的影响机制是：量化噪声 δ 注入到 Attention Score S，导致 Probability P = exp(S+δ)/Σexp(S'+δ') 偏离，进而影响 Next-Token Prediction Loss；该效应随 Seq_Len 增加呈亚线性增长，但在 32K 范围内 PPL 增量通常 < 0.1 的前提是使用了 Scale 因子校准。

## Corrected Claim

FP8 KV Cache 导致的注意力分数误差主要通过改变 Softmax 分布体现，其对最终生成 PPL 的影响机制是：量化噪声 δ 注入到 Attention Score S，导致 Probability P = exp(S+δ)/Σexp(S'+δ') 偏离，进而影响 Next-Token Prediction Loss；该效应随 Seq_Len 增加呈亚线性增长，但在 32K 范围内 PPL 增量通常 < 0.1 的前提是使用了 Scale 因子校准。

## Evidence

先验知识/题面给定，逻辑校验通过
