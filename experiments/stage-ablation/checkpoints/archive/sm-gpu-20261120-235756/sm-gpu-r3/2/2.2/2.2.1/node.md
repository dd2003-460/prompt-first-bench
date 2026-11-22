# N58: 每 token 读取字节数 = (N_params × bits_per_weight / 8) + (KV Cache per token bytes × B

- **status**: pending
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

父节点级核验未通过：不完备, 有冗余（子节点实质上是同一公式在不同参数（精度、Batch Size）下的具体数值实例，存在高度冗余；且父节点强调的核心逻辑是‘全量读取需修正为有效读取量’，子节点直接给出了修正后的具体数值（如6.6GB），却未拆解‘如何从全量54.36GB推导/修正得到有效读取量’这一关键机制，导致对父节点核心定义的覆盖不完整。）

## Search Query

MoE inference effective memory bandwidth calculation active parameters
