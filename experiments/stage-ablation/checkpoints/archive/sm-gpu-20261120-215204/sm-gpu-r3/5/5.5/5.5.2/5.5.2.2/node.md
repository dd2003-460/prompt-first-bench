# N369: 工作点 B (FlashAttention-2 优化)：启用 FlashAttention 后，Prefill 阶段显存访问减少 50%，计算 FLOPs 不变

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N132

## Claim

工作点 B (FlashAttention-2 优化)：启用 FlashAttention 后，Prefill 阶段显存访问减少 50%，计算 FLOPs 不变，但有效 MFU 提升至 60%，TTFT ≈ 25.7s * (0.5/0.6) ≈ 21.4s；约束：仍高于 15s 阈值，需结合 Chunked Prefill 进一步降低。

## Corrected Claim

工作点 B (FlashAttention-2 优化)：启用 FlashAttention 后，Prefill 阶段显存访问减少 50%，计算 FLOPs 不变，但有效 MFU 提升至 60%，TTFT ≈ 25.7s * (0.5/0.6) ≈ 21.4s；约束：仍高于 15s 阈值，需结合 Chunked Prefill 进一步降低。

## Evidence

先验知识/题面给定，逻辑校验通过：FlashAttention 通过减少显存访问提升计算效率（MFU），在 FLOPs 不变的前提下，时间近似与 MFU 成反比，25.7 * (0.5/0.6) ≈ 21.4 计算正确，且符合 FlashAttention-2 优化原理。
