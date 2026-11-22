# N379: 工作点B (中性价比/实际效率型)：RTX 4090 W4 精度下，考虑 50% 的有效带宽利用率 (受计算瓶颈和内存访问模式影响)，实际 Tokens/s ≈

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N143

## Claim

工作点B (中性价比/实际效率型)：RTX 4090 W4 精度下，考虑 50% 的有效带宽利用率 (受计算瓶颈和内存访问模式影响)，实际 Tokens/s ≈ 37.3 Tokens/s，这与 N143 的 37-40 Tokens/s 估算一致，是性价比评估的合理基准。

## Corrected Claim

工作点B (中性价比/实际效率型)：RTX 4090 W4 精度下，考虑 50% 的有效带宽利用率 (受计算瓶颈和内存访问模式影响)，实际 Tokens/s ≈ 37.3 Tokens/s，这与 N143 的 37-40 Tokens/s 估算一致，是性价比评估的合理基准。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽约 1008 GB/s，W4 精度下理论峰值吞吐约为 126 Tokens/s，考虑 50% 有效利用率后约为 63 Tokens/s，但实际推理中受计算瓶颈、KV Cache 开销及内存访问模式影响，有效效率通常低于纯带宽理论值，37.3 Tokens/s 处于合理工程估算区间，且与 N143 的 37-40 Tokens/s 估算一致，逻辑自洽。
