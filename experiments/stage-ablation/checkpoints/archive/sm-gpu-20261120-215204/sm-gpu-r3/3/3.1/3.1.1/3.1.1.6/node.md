# N241: N84 中声称的 'FP8 KV Cache 10GB' 错误源于同样未考虑 GQA。基于 GQA (8 KV Heads) 的 FP8 (1 byte) KV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82, N83, N84

## Claim

N84 中声称的 'FP8 KV Cache 10GB' 错误源于同样未考虑 GQA。基于 GQA (8 KV Heads) 的 FP8 (1 byte) KV Cache 占用应为 2 * 64 * 8 * 128 * 32768 * 1 = 4.29 GB (32K, Batch=1)。因此 N84 的总显存 29GB 估算错误，实际为 13.5 (W4) + 4.3 (FP8 KV) + 2.0 (Overhead) = 19.8GB < 24GB。结论修正：单卡 RTX 4090 在 W4A16 + FP8 KV 下完全可行，N84 的 '不可行' 结论不成立，前提错误。

## Corrected Claim

N84 中声称的 'FP8 KV Cache 10GB' 错误源于同样未考虑 GQA。基于 GQA (8 KV Heads) 的 FP8 (1 byte) KV Cache 占用应为 2 * 64 * 8 * 128 * 32768 * 1 = 4.29 GB (32K, Batch=1)。因此 N84 的总显存 29GB 估算错误，实际为 13.5 (W4) + 4.3 (FP8 KV) + 2.0 (Overhead) = 19.8GB < 24GB。结论修正：单卡 RTX 4090 在 W4A16 + FP8 KV 下完全可行，N84 的 '不可行' 结论不成立，前提错误。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算公式 2 * 64 * 8 * 128 * 32768 * 1 字节 = 4,294,967,296 字节 ≈ 4.29 GB，数值量级与逻辑推导正确；总显存估算 13.5 + 4.3 + 2.0 = 19.8 GB < 24 GB 符合 RTX 4090 显存限制，结论自洽。

## Search Query

FP8 KV cache memory footprint calculation GQA LLM inference
