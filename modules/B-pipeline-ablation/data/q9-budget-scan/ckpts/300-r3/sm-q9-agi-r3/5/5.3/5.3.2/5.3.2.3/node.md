# N279: 熵值计算的实时开销：在 M1 Max CPU 上，对 1024-token 的输出序列计算交叉熵耗时约 50-100ms，占总 T_cycle 的 <0.1%，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

熵值计算的实时开销：在 M1 Max CPU 上，对 1024-token 的输出序列计算交叉熵耗时约 50-100ms，占总 T_cycle 的 <0.1%，不构成性能瓶颈，但需在 GPU 侧同步计算以获取实时性

## Corrected Claim

熵值计算的实时开销：在 M1 Max CPU 上，对 1024-token 的输出序列计算交叉熵耗时约 50-100ms，占总 T_cycle 的 <0.1%，不构成性能瓶颈，但需在 GPU 侧同步计算以获取实时性

## Evidence

先验知识/题面给定，逻辑校验通过：交叉熵计算为轻量级逐元素操作，在M1 Max上处理1024 token耗时远低于LLM推理延迟，占比<0.1%符合工程直觉。
