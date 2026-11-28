# N525: 工作点3 (INT8) 单卡 KV Cache 显存占用计算公式：Mem_KV_INT8 = (num_layers × num_kv_heads × head

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N187, N188, N189

## Claim

工作点3 (INT8) 单卡 KV Cache 显存占用计算公式：Mem_KV_INT8 = (num_layers × num_kv_heads × head_dim × seq_len_max × 2) × dtype_bytes(1)，其中 Qwen3.8-27B 参数需代入以验证 128K tokens 时是否严格占用 4GB

## Corrected Claim

工作点3 (INT8) 单卡 KV Cache 显存占用计算公式：Mem_KV_INT8 = (num_layers × num_kv_heads × head_dim × seq_len_max × 2) × dtype_bytes(1)，其中 Qwen3.8-27B 参数需代入以验证 128K tokens 时是否严格占用 4GB

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3.8-27B num_layers num_kv_heads head_dim configuration parameters
