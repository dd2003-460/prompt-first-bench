# N92: Prefill 阶段吞吐量理论上限公式为 Throughput_prefill = (Compute_FLOPS / (2 * Params * Seq_Len

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

Prefill 阶段吞吐量理论上限公式为 Throughput_prefill = (Compute_FLOPS / (2 * Params * Seq_Len)) * Batch_Size；对于单请求 (Batch=1, Seq_Len=32K)，RTX 4090 (BF16) 的理论 Prefill 上限约为 82.6e12 / (2 * 27e9 * 32768) ≈ 46.9 tokens/s，A100 80GB 约为 312e12 / (2 * 27e9 * 32768) ≈ 177 tokens/s，实测受内存带宽影响通常低于此值。

## Corrected Claim

Prefill 阶段吞吐量理论上限公式为 Throughput_prefill = (Compute_FLOPS / (2 * Params * Seq_Len)) * Batch_Size；对于单请求 (Batch=1, Seq_Len=32K)，RTX 4090 (BF16) 的理论 Prefill 上限约为 82.6e12 / (2 * 27e9 * 32768) ≈ 46.9 tokens/s，A100 80GB 约为 312e12 / (2 * 27e9 * 32768) ≈ 177 tokens/s，实测受内存带宽影响通常低于此值。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合计算密集型Prefill阶段的算术强度理论上限（FLOPS / (2*Params*SeqLen)），数值量级与RTX 4090及A100的BF16算力规格匹配，且正确指出了实际受内存带宽限制低于理论值。
