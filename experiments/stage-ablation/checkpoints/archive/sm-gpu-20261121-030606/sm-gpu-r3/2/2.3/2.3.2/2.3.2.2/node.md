# N239: H100 SXM 80GB在BF16精度下的单请求KV Cache显存占用为5.2GB（基于32K上下文长度，修正N130中可能存在的GQA头数或维度高估，采用

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N106

## Claim

H100 SXM 80GB在BF16精度下的单请求KV Cache显存占用为5.2GB（基于32K上下文长度，修正N130中可能存在的GQA头数或维度高估，采用保守估算值），该数值是计算并发上限的分母组成部分之二。

## Corrected Claim

H100 SXM 80GB在BF16精度下的单请求KV Cache显存占用为5.2GB（基于32K上下文长度，修正N130中可能存在的GQA头数或维度高估，采用保守估算值），该数值是计算并发上限的分母组成部分之二。

## Evidence

先验知识/题面给定，逻辑校验通过
