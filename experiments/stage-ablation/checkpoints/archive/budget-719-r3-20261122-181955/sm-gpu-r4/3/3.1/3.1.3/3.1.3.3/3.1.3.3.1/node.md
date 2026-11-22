# N783: Prefill 阶段线性层（FFN + QKV 投影）的 FLOPs 计算项为 2 * Params * Seq_Len；对于 Qwen3-27B (Param

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N280

## Claim

Prefill 阶段线性层（FFN + QKV 投影）的 FLOPs 计算项为 2 * Params * Seq_Len；对于 Qwen3-27B (Params=27e9)，在 32K (32768) 序列长度下，该项计算量为 2 * 27e9 * 32768 = 1.77e15 FLOPs (1.77 PFLOPs)。

## Corrected Claim

Prefill 阶段线性层（FFN + QKV 投影）的 FLOPs 计算项为 2 * Params * Seq_Len；对于 Qwen3-27B (Params=27e9)，在 32K (32768) 序列长度下，该项计算量为 2 * 27e9 * 32768 = 1.77e15 FLOPs (1.77 PFLOPs)。

## Evidence

先验知识/题面给定，逻辑校验通过：2 * 27e9 * 32768 = 1.769472e15 ≈ 1.77e15，计算无误且符合大模型Prefill阶段FLOPs估算公式。

## Search Query

LLM prefill FLOPs calculation linear layers
