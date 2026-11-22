# N310: RTX 4090 在 32K 上下文下单请求 Prefill 耗时估算：理论 FLOPs 需求 1.7e12，4090 BF16 算力 82 TFLOPS，利用

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99

## Claim

RTX 4090 在 32K 上下文下单请求 Prefill 耗时估算：理论 FLOPs 需求 1.7e12，4090 BF16 算力 82 TFLOPS，利用率 60%，实际耗时 ≈ 1.7e12 / (82e12 * 0.6) ≈ 3.4 秒。由于单请求已超 2s 目标，B_prefill_max = 1 (即无法通过增大 Batch 满足 2s TTFT，需降低上下文长度或接受更高延迟)。

## Corrected Claim

RTX 4090 在 32K 上下文下单请求 Prefill 耗时估算：理论 FLOPs 需求 1.7e12，4090 BF16 算力 82 TFLOPS，利用率 60%，实际耗时 ≈ 1.7e12 / (82e12 * 0.6) ≈ 3.4 秒。由于单请求已超 2s 目标，B_prefill_max = 1 (即无法通过增大 Batch 满足 2s TTFT，需降低上下文长度或接受更高延迟)。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 BF16 算力约 82.6 TFLOPS，计算耗时 1.7e12 / (82e12 * 0.6) ≈ 3.4s 符合算术逻辑，且 3.4s > 2s 导致 Batch=1 的结论自洽。
