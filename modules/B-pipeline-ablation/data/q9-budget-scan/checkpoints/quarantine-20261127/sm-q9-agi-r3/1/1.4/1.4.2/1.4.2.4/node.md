# N149: 通信占比最终判定：T_comm ≈ 0.52 ms (来自 N124)。T_step ≈ 30 ms (保守估计)。占比 = 0.52 / 30 ≈ 1.7%。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

通信占比最终判定：T_comm ≈ 0.52 ms (来自 N124)。T_step ≈ 30 ms (保守估计)。占比 = 0.52 / 30 ≈ 1.7%。结论：通信开销 < 10% 阈值，不会显著抵消投机解码收益。瓶颈确认为 Memory Bandwidth (权重/KV 读取) 而非 All-Reduce 通信。优化重点应放在 KV Cache 压缩 (如 FP8 KV) 和 Batch 调度上，而非通信拓扑优化。

## Corrected Claim

通信占比最终判定：T_comm ≈ 0.52 ms (来自 N124)。T_step ≈ 30 ms (保守估计)。占比 = 0.52 / 30 ≈ 1.7%。结论：通信开销 < 10% 阈值，不会显著抵消投机解码收益。瓶颈确认为 Memory Bandwidth (权重/KV 读取) 而非 All-Reduce 通信。优化重点应放在 KV Cache 压缩 (如 FP8 KV) 和 Batch 调度上，而非通信拓扑优化。

## Evidence

先验知识/题面给定，逻辑校验通过：0.52ms/30ms≈1.7%计算正确，且符合大模型推理中通信开销通常远低于计算/内存带宽瓶颈的工程常识。

## Search Query

LLM serving bottleneck analysis memory bandwidth vs communication overhead
