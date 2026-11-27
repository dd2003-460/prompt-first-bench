# N30: 低频大对象带宽占比 B_tail 的计算：B_tail = (Σ_{i: f_i < f_threshold, S_i > C/K} f_i * S_i) / 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

低频大对象带宽占比 B_tail 的计算：B_tail = (Σ_{i: f_i < f_threshold, S_i > C/K} f_i * S_i) / (Σ_{all} f_i * S_i)；该值代表 LRU 因驱逐这些对象而损失的潜在命中率，是 ΔH_max 的上界来源之一；f_threshold 定义为使得累计请求频率达到 95% 的倒数排名对应的频率值。

## Corrected Claim

低频大对象带宽占比 B_tail 的计算：B_tail = (Σ_{i: f_i < f_threshold, S_i > C/K} f_i * S_i) / (Σ_{all} f_i * S_i)；该值代表 LRU 因驱逐这些对象而损失的潜在命中率，是 ΔH_max 的上界来源之一；f_threshold 定义为使得累计请求频率达到 95% 的倒数排名对应的频率值。

## Evidence

先验知识/题面给定，逻辑校验通过
