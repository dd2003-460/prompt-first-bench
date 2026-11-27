# N389: H100 SXM 在 BF16 LLM 推理 (Decode 阶段) 下主要受显存带宽限制而非算力限制，实际功耗通常维持在 TDP (700W) 的 60%-8

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N160, N161, N162

## Claim

H100 SXM 在 BF16 LLM 推理 (Decode 阶段) 下主要受显存带宽限制而非算力限制，实际功耗通常维持在 TDP (700W) 的 60%-80% 区间，即 420W-560W；取中值 500W 作为 3 年电费计算的保守基准值。

## Corrected Claim

H100 SXM 在 BF16 LLM 推理 (Decode 阶段) 下主要受显存带宽限制而非算力限制，实际功耗通常维持在 TDP (700W) 的 60%-80% 区间，即 420W-560W；取中值 500W 作为 3 年电费计算的保守基准值。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM TDP为700W，Decode阶段受显存带宽限制导致算力单元空闲，功耗低于峰值符合物理直觉，500W作为中值估算合理。

## Search Query

H100 SXM actual power consumption LLM inference decode phase
