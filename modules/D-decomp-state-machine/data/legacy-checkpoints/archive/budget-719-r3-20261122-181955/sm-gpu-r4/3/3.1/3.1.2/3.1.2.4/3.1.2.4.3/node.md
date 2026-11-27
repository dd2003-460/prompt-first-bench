# N778: Batch_Size 对 Decode 吞吐量的边际效益递减阈值可通过显存约束方程求解：Batch_Max = floor((VRAM_Total - Weig

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N277

## Claim

Batch_Size 对 Decode 吞吐量的边际效益递减阈值可通过显存约束方程求解：Batch_Max = floor((VRAM_Total - Weights_Size - Overhead) / KV_Cache_Per_Request)，其中 KV_Cache_Per_Request = KV_Cache_Per_Token * Seq_Len；当 Batch_Max < 2 时，边际效益为零，此时应优先优化单请求延迟而非吞吐量。

## Corrected Claim

Batch_Size 对 Decode 吞吐量的边际效益递减阈值可通过显存约束方程求解：Batch_Max = floor((VRAM_Total - Weights_Size - Overhead) / KV_Cache_Per_Request)，其中 KV_Cache_Per_Request = KV_Cache_Per_Token * Seq_Len；当 Batch_Max < 2 时，边际效益为零，此时应优先优化单请求延迟而非吞吐量。

## Evidence

先验知识/题面给定，逻辑校验通过
