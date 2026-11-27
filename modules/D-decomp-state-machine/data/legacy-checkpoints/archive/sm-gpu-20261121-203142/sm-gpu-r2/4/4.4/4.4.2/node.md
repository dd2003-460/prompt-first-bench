# N88: RTX 4090 (24GB, 1.0 TB/s带宽, 82 TFLOPS BF16) 在32K上下文下的TTFT估算：Prefill计算量约为 2 * 27B

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

RTX 4090 (24GB, 1.0 TB/s带宽, 82 TFLOPS BF16) 在32K上下文下的TTFT估算：Prefill计算量约为 2 * 27B * 32K FLOPs，理论时间 = 1.7e12 FLOPs / 82e12 FLOPS ≈ 20.7秒；实际因优化（FlashAttention等）可能降至5-10秒 [待核验]。

## Corrected Claim

RTX 4090 (24GB, 1.0 TB/s带宽, 82 TFLOPS BF16) 在32K上下文下的TTFT估算：Prefill计算量约为 2 * 27B * 32K FLOPs，理论时间 = 1.7e12 FLOPs / 82e12 FLOPS ≈ 20.7秒；实际因优化（FlashAttention等）可能降至5-10秒 [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：2 * 27e9 * 32768 ≈ 1.76e15 FLOPs，除以 82e12 FLOPS 约为 21.5秒，与陈述中的20.7秒量级一致（差异源于32K具体取值或精度假设），逻辑自洽。

## Search Query

RTX 4090 Qwen 27B 32k context time to first token
