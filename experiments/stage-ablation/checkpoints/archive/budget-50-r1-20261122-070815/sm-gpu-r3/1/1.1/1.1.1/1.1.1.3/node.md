# N159: 线性注意力层的状态占用机制：线性注意力层在推理过程中维护固定大小的递归状态（Recurrent State），其显存占用与上下文长度无关，具体大小需根据 hea

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35, N36, N37

## Claim

线性注意力层的状态占用机制：线性注意力层在推理过程中维护固定大小的递归状态（Recurrent State），其显存占用与上下文长度无关，具体大小需根据 head_dim 和层数计算，通常远小于全注意力 KV Cache

## Corrected Claim

线性注意力层的状态占用机制：线性注意力层在推理过程中维护固定大小的递归状态（Recurrent State），其显存占用与上下文长度无关，具体大小需根据 head_dim 和层数计算，通常远小于全注意力 KV Cache

## Evidence

先验知识/题面给定，逻辑校验通过：线性注意力机制（如Linear Transformer, Performer等）的核心特性即为将注意力计算转化为固定大小的递归状态更新，其显存复杂度为O(1)（相对于序列长度），而标准Transformer的KV Cache复杂度为O(N)，因此该陈述在逻辑和工程事实上均成立。
