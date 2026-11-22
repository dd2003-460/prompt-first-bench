# N355: 瓶颈判定：由于理论带宽限制速度 (47.4 tok/s) 接近或低于实测值 (40-60 tok/s)，且 RTX 4090 算力 (82.6 TFLOPS F

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

瓶颈判定：由于理论带宽限制速度 (47.4 tok/s) 接近或低于实测值 (40-60 tok/s)，且 RTX 4090 算力 (82.6 TFLOPS FP16) 远大于 108 GFLOPs/token * 47.4 tok/s ≈ 5.1 TFLOPs 的需求，因此瓶颈为 Memory-Bound (带宽受限)，而非 Compute-Bound

## Corrected Claim

瓶颈判定：由于理论带宽限制速度 (47.4 tok/s) 接近或低于实测值 (40-60 tok/s)，且 RTX 4090 算力 (82.6 TFLOPS FP16) 远大于 108 GFLOPs/token * 47.4 tok/s ≈ 5.1 TFLOPs 的需求，因此瓶颈为 Memory-Bound (带宽受限)，而非 Compute-Bound

## Evidence

先验知识/题面给定，逻辑校验通过：算术推导正确（108 GFLOPs/token * 47.4 tok/s ≈ 5.1 TFLOPs），且 5.1 TFLOPs 远小于 82.6 TFLOPS，符合 Memory-Bound 判定逻辑。

## Search Query

LLM inference memory bound vs compute bound threshold HBM bandwidth
