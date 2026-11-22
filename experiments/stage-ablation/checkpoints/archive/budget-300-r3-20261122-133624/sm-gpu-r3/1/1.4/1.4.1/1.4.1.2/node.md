# N202: BF16 精度下 KV Cache 显存占用的完整推导：C_kv = 2 (K+V) * N_layers * N_kv_heads * d_head * L_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

BF16 精度下 KV Cache 显存占用的完整推导：C_kv = 2 (K+V) * N_layers * N_kv_heads * d_head * L_ctx * sizeof(float16)。对于 Qwen3-27B (N_layers=32, N_kv_heads=8, d_head=128, L_ctx=32768, sizeof=2 bytes)，计算得 2 * 32 * 8 * 128 * 32768 * 2 = 4,294,967,296 bytes = 4.0 GB。此值不包含任何量化压缩，若使用 INT8 KV Cache，则减半至 2.0 GB，显著影响单卡部署可行性。

## Corrected Claim

BF16 精度下 KV Cache 显存占用的完整推导：C_kv = 2 (K+V) * N_layers * N_kv_heads * d_head * L_ctx * sizeof(float16)。对于 Qwen3-27B (N_layers=32, N_kv_heads=8, d_head=128, L_ctx=32768, sizeof=2 bytes)，计算得 2 * 32 * 8 * 128 * 32768 * 2 = 4,294,967,296 bytes = 4.0 GB。此值不包含任何量化压缩，若使用 INT8 KV Cache，则减半至 2.0 GB，显著影响单卡部署可行性。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，数值计算准确（2*32*8*128*32768*2 = 4,294,967,296 bytes = 4.0 GB），符合BF16精度下KV Cache显存占用的标准计算逻辑。
