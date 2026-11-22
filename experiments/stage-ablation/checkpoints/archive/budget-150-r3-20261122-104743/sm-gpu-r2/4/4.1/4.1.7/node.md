# N130: INT8 精度下 Qwen3-27B 的 KV Cache 单 token 显存占用为 2 × n_layers × n_kv_heads × head_dim

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19, N20, N21

## Claim

INT8 精度下 Qwen3-27B 的 KV Cache 单 token 显存占用为 2 × n_layers × n_kv_heads × head_dim × 1 byte = 65,536 bytes/token (64 KB/token)

## Corrected Claim

INT8 精度下 Qwen3-27B 的 KV Cache 单 token 显存占用为 2 × n_layers × n_kv_heads × head_dim × 1 byte = 65,536 bytes/token (64 KB/token)

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（n_layers=64, n_kv_heads=8, head_dim=128）代入公式 2*64*8*128*1 = 65536 bytes，计算无误且符合 GQA 模型 KV Cache 显存占用标准估算逻辑。
