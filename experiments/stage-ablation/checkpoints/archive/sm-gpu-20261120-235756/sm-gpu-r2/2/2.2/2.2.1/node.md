# N58: 每 token 读取字节数 = (N_params × bits_per_weight / 8) + (KV Cache per token bytes × B

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N14

## Claim

每 token 读取字节数 = (N_params × bits_per_weight / 8) + (KV Cache per token bytes × Batch_Size)，对于 Qwen3-27B 在 BF16 下，权重部分为 54.36 GB/token (若全量读取)，但实际推理中仅读取激活专家参数，需修正为有效读取量。

## Corrected Claim

Qwen3-27B 在 BF16 下的总权重存储大小约为 54.36 GB。每 token 的实际读取字节数取决于激活的专家参数数量及 KV Cache 大小，远小于总权重体积，需根据具体 MoE 路由策略计算有效读取量。

## Evidence

[质询]数值量级严重错误：Qwen3-27B 的总参数量约为 270 亿，BF16 下总权重体积约为 54 GB（54.36 GB），这是整个模型的静态存储大小，而非“每 token 读取字节数”。将总模型大小误标为每 token 读取量，混淆了静态存储与动态 I/O 带宽的概念，且未考虑 MoE 架构中仅激活部分专家的事实，导致数值高估了数千倍。 | 逻辑校验失败：27B 参数在 BF16 下总大小约为 54 GB，这是模型总大小，不可能每生成一个 token 就读取 54 GB 数据（这将导致极高的延迟和带宽需求，违背基本推理直觉）。此外，Qwen3-27B 若为 MoE 模型，每 token 仅激活部分专家，实际读取量远小于总权重。

## Search Query

MoE inference effective memory bandwidth calculation active parameters
