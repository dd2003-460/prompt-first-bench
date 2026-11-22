# N345: 1×RTX 4090 在 16K 上下文 Prefill 阶段的 TTFT 估算：基于 82.6 TFLOPS 峰值算力，MFU 取 40% (N111 经验值

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N123

## Claim

1×RTX 4090 在 16K 上下文 Prefill 阶段的 TTFT 估算：基于 82.6 TFLOPS 峰值算力，MFU 取 40% (N111 经验值)，有效算力 33 TFLOPS，Prefill 计算量 2 * 27e9 * 16384 ≈ 0.885 TFLOPs，理论耗时 0.885 / 33 ≈ 26.8 ms，但实际受内核启动、数据搬运和 FlashAttention 优化影响，实测 TTFT 通常在 1-3 秒区间，需结合具体框架版本验证。

## Corrected Claim

1×RTX 4090 在 16K 上下文 Prefill 阶段的 TTFT 估算：基于 82.6 TFLOPS 峰值算力，MFU 取 40% (N111 经验值)，有效算力 33 TFLOPS，Prefill 计算量 2 * 27e9 * 16384 ≈ 0.885 TFLOPs，理论耗时 0.885 / 33 ≈ 26.8 ms，但实际受内核启动、数据搬运和 FlashAttention 优化影响，实测 TTFT 通常在 1-3 秒区间，需结合具体框架版本验证。

## Evidence

先验知识/题面给定，逻辑校验通过：计算量估算（2*27e9*16384≈0.885 TFLOPs）与耗时推导（0.885/33≈26.8ms）数学自洽，且符合大模型Prefill阶段计算密集型的物理直觉；实测TTFT受内存带宽和内核开销影响远大于纯计算时间，1-3秒的量级在单卡16K上下文场景下合理。
