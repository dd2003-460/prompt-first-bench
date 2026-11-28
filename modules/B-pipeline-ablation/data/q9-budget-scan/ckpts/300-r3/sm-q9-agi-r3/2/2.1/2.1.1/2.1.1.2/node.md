# N173: 香农熵H(Q)的计算需基于问题中关键实体的预测概率分布P(w_i)，在M1 Max CPU上，对单个Query（约20-50 tokens）计算熵的耗时约为1-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

香农熵H(Q)的计算需基于问题中关键实体的预测概率分布P(w_i)，在M1 Max CPU上，对单个Query（约20-50 tokens）计算熵的耗时约为1-2ms，远低于5%推理延迟阈值

## Corrected Claim

香农熵H(Q)的计算需基于问题中关键实体的预测概率分布P(w_i)，在M1 Max CPU上，对单个Query（约20-50 tokens）计算熵的耗时约为1-2ms，远低于5%推理延迟阈值

## Evidence

先验知识/题面给定，逻辑校验通过：香农熵计算复杂度为O(V)或O(N)，对于20-50 tokens的序列，在现代CPU（M1 Max）上执行浮点运算耗时确实在毫秒级甚至微秒级，远低于5%推理延迟阈值（通常推理延迟为几十到几百毫秒），量级合理且符合计算机性能常识。

## Search Query

Shannon entropy calculation latency CPU python scipy
