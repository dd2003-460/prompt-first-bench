# N11: 硬件架构对LLM推理的关键性能指标：显存带宽 (GB/s) 决定 decode 速度，算力 (TFLOPS) 决定 prefill 速度。RTX 4090: 1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

硬件架构对LLM推理的关键性能指标：显存带宽 (GB/s) 决定 decode 速度，算力 (TFLOPS) 决定 prefill 速度。RTX 4090: 1008 GB/s, 82.6 TFLOPS (FP16); A100 80GB: 2039 GB/s, 312 TFLOPS (FP16); H100: 3350 GB/s, 989 TFLOPS (FP16); M3 Ultra: ~800 GB/s (统一内存)。

## Corrected Claim

硬件架构对LLM推理的关键性能指标：显存带宽 (GB/s) 决定 decode 速度，算力 (TFLOPS) 决定 prefill 速度。RTX 4090: 1008 GB/s, 82.6 TFLOPS (FP16); A100 80GB: 2039 GB/s, 312 TFLOPS (FP16); H100: 3350 GB/s, 989 TFLOPS (FP16); M3 Ultra: ~800 GB/s (统一内存)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RTX 4090 memory bandwidth GB/s A100 H100 memory bandwidth M3 Ultra memory bandwidth
