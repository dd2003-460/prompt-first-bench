# N20: TTFT（首字延迟）计算模型：TTFT ≈ T_prefill / (Batch_Size * GPU_Mem_BW) + T_kv_cache_alloc，其

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

TTFT（首字延迟）计算模型：TTFT ≈ T_prefill / (Batch_Size * GPU_Mem_BW) + T_kv_cache_alloc，其中 T_prefill = (2 * N_params * Seq_Len) / Effective_FLOPs，需根据 Qwen3-27B 的 N_params ≈ 27e9 和 Seq_Len=32K 进行具体数值代入。

## Corrected Claim

TTFT（首字延迟）计算模型：TTFT ≈ T_prefill / (Batch_Size * GPU_Mem_BW) + T_kv_cache_alloc，其中 T_prefill = (2 * N_params * Seq_Len) / Effective_FLOPs，需根据 Qwen3-27B 的 N_params ≈ 27e9 和 Seq_Len=32K 进行具体数值代入。

## Evidence

先验知识/题面给定，逻辑校验通过：TTFT主要由Prefill阶段决定，计算量公式2*N*L符合Transformer标准，延迟估算逻辑自洽。
