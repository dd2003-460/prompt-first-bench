# N785: 在 32K 上下文下，注意力计算量占比 = Attention_FLOPs / (Linear_FLOPs + Attention_FLOPs) = 22.5e

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N280

## Claim

在 32K 上下文下，注意力计算量占比 = Attention_FLOPs / (Linear_FLOPs + Attention_FLOPs) = 22.5e15 / (1.77e15 + 22.5e15) ≈ 92.7%；这表明长上下文下计算瓶颈完全由 O(N^2) 注意力主导，原 N280 中 '30-50%' 的估计严重低估了长序列下的注意力占比，导致基于线性层算力的理论吞吐量估算失效。

## Corrected Claim

在 32K 上下文下，注意力计算量占比 = Attention_FLOPs / (Linear_FLOPs + Attention_FLOPs) = 22.5e15 / (1.77e15 + 22.5e15) ≈ 92.7%；这表明长上下文下计算瓶颈完全由 O(N^2) 注意力主导，原 N280 中 '30-50%' 的估计严重低估了长序列下的注意力占比，导致基于线性层算力的理论吞吐量估算失效。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 22.5/(1.77+22.5) ≈ 0.927 正确，且符合长序列下注意力计算量随 N^2 增长而主导总 FLOPs 的理论预期。

## Search Query

attention FLOPs ratio long context LLM inference
