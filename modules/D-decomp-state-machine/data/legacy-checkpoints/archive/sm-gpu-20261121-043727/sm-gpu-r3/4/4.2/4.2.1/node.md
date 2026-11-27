# N65: 修正 N23 中 T_prefill 公式的分子项：对于 Transformer 自注意力模型，Prefill 阶段（处理 P 个 prompt tokens）

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

修正 N23 中 T_prefill 公式的分子项：对于 Transformer 自注意力模型，Prefill 阶段（处理 P 个 prompt tokens）的总计算量 FLOPs = P * (2 * L_params + Attention_FLOPs)，其中 Attention_FLOPs ≈ 4 * P * d_model * n_layers，需将 L=27B 替换为具体的参数量 27.2e9 并补充注意力项，原公式漏掉了 QKV 投影及 Attention 矩阵乘法的计算量

## Corrected Claim

修正 N23 中 T_prefill 公式的分子项：对于 Transformer 自注意力模型，Prefill 阶段（处理 P 个 prompt tokens）的总计算量 FLOPs = P * (2 * L_params + Attention_FLOPs)，其中 Attention_FLOPs ≈ 4 * P * d_model * n_layers，需将 L=27B 替换为具体的参数量 27.2e9 并补充注意力项，原公式漏掉了 QKV 投影及 Attention 矩阵乘法的计算量

## Evidence

父节点级核验失败（LLM 错误）：Expecting value: line 6 column 19 (char 944)

## Search Query

Transformer prefill FLOPs calculation formula attention matrix multiplication
