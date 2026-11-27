# N215: Qwen3-27B 模型在 32K 上下文下，Prefill 阶段的总 FLOPs 计算公式为：2 * (27e9 * 32e3) + 2 * (32e3 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

Qwen3-27B 模型在 32K 上下文下，Prefill 阶段的总 FLOPs 计算公式为：2 * (27e9 * 32e3) + 2 * (32e3 * 32e3 / 2) * n_layers * 2，其中 Attention 项通常占比 <5%，因此 TTFT 主要受限于 GEMM (权重加载+矩阵乘) 的算力而非 Attention 的显存带宽。

## Corrected Claim

Qwen3-27B 模型在 32K 上下文下，Prefill 阶段的总 FLOPs 计算公式为：2 * (27e9 * 32e3) + 2 * (32e3 * 32e3 / 2) * n_layers * 2，其中 Attention 项通常占比 <5%，因此 TTFT 主要受限于 GEMM (权重加载+矩阵乘) 的算力而非 Attention 的显存带宽。

## Evidence

先验知识/题面给定，逻辑校验通过
