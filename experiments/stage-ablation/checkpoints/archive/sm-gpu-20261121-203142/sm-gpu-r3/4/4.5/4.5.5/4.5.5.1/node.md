# N295: 量化精度对 KV Cache 显存占用及带宽压力的修正项：在 FP8/INT4 量化权重下，KV Cache 通常保持 FP16/BF16 以保证注意力计算精度

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

量化精度对 KV Cache 显存占用及带宽压力的修正项：在 FP8/INT4 量化权重下，KV Cache 通常保持 FP16/BF16 以保证注意力计算精度，导致总读取字节数 W_total = W_weights_quantized + W_KV_cache_fp16，这使得 INT4 权重的实际 TPS 提升倍数低于理论 4 倍（因 KV 部分未减半/四分之一）。

## Corrected Claim

量化精度对 KV Cache 显存占用及带宽压力的修正项：在 FP8/INT4 量化权重下，KV Cache 通常保持 FP16/BF16 以保证注意力计算精度，导致总读取字节数 W_total = W_weights_quantized + W_KV_cache_fp16，这使得 INT4 权重的实际 TPS 提升倍数低于理论 4 倍（因 KV 部分未减半/四分之一）。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache通常保持高精度（FP16/BF16）以维持注意力计算稳定性，而权重量化（如INT4）仅减少权重部分显存，因此总读取字节数中KV部分未随权重量化比例缩减，导致实际TPS提升低于理论权重量化倍数，符合工程实践与逻辑推导。
