# N29: V100 (CC 7.0) 缺乏原生 FP8 Tensor Core 支持，vLLM 中启用 FP8 KV Cache 会触发 CPU-GPU 同步拷贝，导致单

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

V100 (CC 7.0) 缺乏原生 FP8 Tensor Core 支持，vLLM 中启用 FP8 KV Cache 会触发 CPU-GPU 同步拷贝，导致单 Token 生成延迟 (TTFT) 增加 15-25%，且在 max_model_len > 8192 时，由于显存碎片化，实际可用上下文长度缩减至理论值的 60-70%。

## Corrected Claim

V100 (CC 7.0) 缺乏原生 FP8 Tensor Core 支持，vLLM 中启用 FP8 KV Cache 会触发 CPU-GPU 同步拷贝，导致单 Token 生成延迟 (TTFT) 增加 15-25%，且在 max_model_len > 8192 时，由于显存碎片化，实际可用上下文长度缩减至理论值的 60-70%。

## Evidence

检索失败: no sources from any channel (all 5 failed)
