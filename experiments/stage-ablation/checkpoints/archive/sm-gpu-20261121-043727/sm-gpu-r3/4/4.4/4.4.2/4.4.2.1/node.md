# N187: RTX 4090 在 W4 量化下运行 Qwen3-27B 时的最大序列长度计算：剩余显存 8 GB，若 KV Cache 使用 FP16 (128 KB/To

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

RTX 4090 在 W4 量化下运行 Qwen3-27B 时的最大序列长度计算：剩余显存 8 GB，若 KV Cache 使用 FP16 (128 KB/Token)，则 Max_Tokens = 8e9 bytes / (128 * 1024 bytes) ≈ 65,536 Tokens；若使用 FP8 (64 KB/Token)，则 Max_Tokens ≈ 131,072 Tokens，远超 32K 需求

## Corrected Claim

RTX 4090 在 W4 量化下运行 Qwen3-27B 时的最大序列长度计算：剩余显存 8 GB，若 KV Cache 使用 FP16 (128 KB/Token)，则 Max_Tokens = 8e9 bytes / (128 * 1024 bytes) ≈ 65,536 Tokens；若使用 FP8 (64 KB/Token)，则 Max_Tokens ≈ 131,072 Tokens，远超 32K 需求

## Evidence

先验知识/题面给定，逻辑校验通过：8GB显存除以128KB/Token确实约为65536 Tokens，除以64KB/Token约为131072 Tokens，计算无误且量级合理。
