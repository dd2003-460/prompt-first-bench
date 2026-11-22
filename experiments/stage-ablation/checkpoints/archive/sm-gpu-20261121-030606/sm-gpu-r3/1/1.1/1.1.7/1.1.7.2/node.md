# N206: RTX 4090 FP8 计算瓶颈修正项：纯带宽受限假设忽略了计算延迟，RTX 4090 FP8 稠密算力约 330 TFLOPS（FP16 的 2 倍，N16

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N86

## Claim

RTX 4090 FP8 计算瓶颈修正项：纯带宽受限假设忽略了计算延迟，RTX 4090 FP8 稠密算力约 330 TFLOPS（FP16 的 2 倍，N160 支持），Qwen3-27B 每 token 计算量约 54 GFLOPs，计算时间 = 54e9 / (330e12 * 0.8 效率) ≈ 0.2ms，远小于带宽时间 31ms，因此带宽确实是主要瓶颈，但需扣除 5-10% 的 kernel launch 开销，实际吞吐量修正为 32.4 * 0.9 ≈ 29.2 tokens/s。

## Corrected Claim

RTX 4090 FP8 计算瓶颈修正项：纯带宽受限假设忽略了计算延迟，RTX 4090 FP8 稠密算力约 330 TFLOPS（FP16 的 2 倍，N160 支持），Qwen3-27B 每 token 计算量约 54 GFLOPs，计算时间 = 54e9 / (330e12 * 0.8 效率) ≈ 0.2ms，远小于带宽时间 31ms，因此带宽确实是主要瓶颈，但需扣除 5-10% 的 kernel launch 开销，实际吞吐量修正为 32.4 * 0.9 ≈ 29.2 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 FP8算力约330 TFLOPS符合硬件规格（FP16 165 TFLOPS的2倍），Qwen3-27B每token计算量约54 GFLOPs（2*27e9）合理，计算时间0.2ms远小于带宽时间31ms，带宽瓶颈判断正确，kernel launch开销修正逻辑自洽
