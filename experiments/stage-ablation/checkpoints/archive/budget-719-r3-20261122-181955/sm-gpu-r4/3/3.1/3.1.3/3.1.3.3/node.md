# N280: Prefill 阶段的 FLOPs 计算公式需修正为 FLOPs = 2 * Params * Seq_Len + 4 * Seq_Len^2 * n_head

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

Prefill 阶段的 FLOPs 计算公式需修正为 FLOPs = 2 * Params * Seq_Len + 4 * Seq_Len^2 * n_heads * head_dim，其中第二项为注意力机制的 O(N^2) 计算复杂度，在 32K 上下文下，注意力计算量占比可达 30-50%，导致实际吞吐量低于仅基于权重矩阵乘法的理论值。

## Corrected Claim

Prefill 阶段的 FLOPs 计算公式需修正为 FLOPs = 2 * Params * Seq_Len + 4 * Seq_Len^2 * n_heads * head_dim，其中第二项为注意力机制的 O(N^2) 计算复杂度，在 32K 上下文下，注意力计算量占比可达 30-50%，导致实际吞吐量低于仅基于权重矩阵乘法的理论值。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 5 column 13 (char 79)

## Search Query

LLM prefill FLOPs calculation attention quadratic complexity 32K context
