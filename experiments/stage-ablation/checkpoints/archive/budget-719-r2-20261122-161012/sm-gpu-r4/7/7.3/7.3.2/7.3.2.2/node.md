# N657: H100 SXM 的 HBM3 实际带宽利用率在 LLM 推理 Decode 阶段通常为 70%-85%（受限于 kernel launch overhead 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N271

## Claim

H100 SXM 的 HBM3 实际带宽利用率在 LLM 推理 Decode 阶段通常为 70%-85%（受限于 kernel launch overhead 和 memory access pattern），因此实际吞吐上限 = 3350 GB/s * 0.75 / 27.5 GB ≈ 91.4 tokens/s，而非理论峰值 121.8 tokens/s

## Corrected Claim

H100 SXM 的 HBM3 实际带宽利用率在 LLM 推理 Decode 阶段通常为 70%-85%（受限于 kernel launch overhead 和 memory access pattern），因此实际吞吐上限 = 3350 GB/s * 0.75 / 27.5 GB ≈ 91.4 tokens/s，而非理论峰值 121.8 tokens/s

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM HBM3 理论带宽 3.35 TB/s，Decode 阶段受内存带宽限制，70%-85% 利用率符合工程经验，计算 3350 * 0.75 / 27.5 ≈ 91.4 正确。

## Search Query

H100 SXM HBM3 bandwidth utilization LLM inference decode phase
