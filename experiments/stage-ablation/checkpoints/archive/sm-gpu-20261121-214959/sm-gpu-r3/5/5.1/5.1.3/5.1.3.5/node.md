# N270: llama.cpp 默认连续内存分配在 batch_size=1, context_len=32k 下的有效带宽利用率修正系数 η_llama = 0.82 (

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N98, N99, N100

## Claim

llama.cpp 默认连续内存分配在 batch_size=1, context_len=32k 下的有效带宽利用率修正系数 η_llama = 0.82 (基于碎片率 15-20% 的中值假设)，实际 Decode 吞吐 = 理论带宽 * η_llama / 模型大小。

## Corrected Claim

llama.cpp 在典型配置（batch_size=1, context_len=32k）下的有效带宽利用率修正系数 η_llama 通常在 0.7-0.85 区间波动（具体取决于硬件与实现细节），实际 Decode 吞吐 ≈ 理论带宽 * η_llama / 模型大小。

## Evidence

[质询]数值 0.82 及碎片率 15-20% 属于特定硬件与实现版本下的经验测量值，并非 llama.cpp 的固定理论常数；不同 GPU 架构、内存带宽及 llama.cpp 版本（如是否启用 Flash Attention、KV Cache 量化等）会导致该系数显著波动，将其作为通用默认值缺乏普适性。 | 先验知识/题面给定，逻辑校验通过（量纲与量级合理），但作为经验事实缺乏外部来源直接支持，且数值具有高度情境依赖性，故降级。

## Search Query

llama.cpp continuous memory allocation fragmentation performance impact long context
