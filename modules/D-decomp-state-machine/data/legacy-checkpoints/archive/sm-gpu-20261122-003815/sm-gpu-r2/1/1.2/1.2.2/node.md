# N49: H100 80GB 相比 A100 80GB 在 Qwen3-27B 推理上的性能增益：显存带宽 3350 GB/s vs 2039 GB/s (提升 64%)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

H100 80GB 相比 A100 80GB 在 Qwen3-27B 推理上的性能增益：显存带宽 3350 GB/s vs 2039 GB/s (提升 64%)，FP16 算力 989 TFLOPS vs 312 TFLOPS (提升 217%)，Decode 阶段吞吐预计提升 ~60%，Prefill 阶段提升 ~200%。

## Corrected Claim

H100 80GB 相比 A100 80GB 在 Qwen3-27B 推理上的性能增益：显存带宽 3350 GB/s vs 2039 GB/s (提升 64%)，FP16 算力 989 TFLOPS vs 312 TFLOPS (提升 217%)，Decode 阶段吞吐预计提升 ~60%，Prefill 阶段提升 ~200%。

## Evidence

先验知识/题面给定，逻辑校验通过：H100与A100的显存带宽及FP16算力数值符合官方规格，基于Roofline模型推导的Decode（带宽受限）和Prefill（算力受限）阶段性能增益比例在逻辑上自洽且量级合理。

## Search Query

H100 vs A100 LLM inference throughput benchmark
