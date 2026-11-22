# N202: RTX 4090 24GB 在 W4 精度下运行 Qwen3-27B (32K ctx) 时，KV Cache 若保持 FP16/BF16 精度，其显存占用仍为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

RTX 4090 24GB 在 W4 精度下运行 Qwen3-27B (32K ctx) 时，KV Cache 若保持 FP16/BF16 精度，其显存占用仍为 13.11 GB，总显存需求 6.875 + 13.11 + 5 = 24.985 GB，超过 24GB 显存，导致不可行；若 KV Cache 也量化为 INT8，则显存占用降至 6.555 GB，总需求 18.43 GB，可行

## Corrected Claim

RTX 4090 24GB 在 W4 精度下运行 Qwen3-27B (32K ctx) 时，KV Cache 若保持 FP16/BF16 精度，其显存占用仍为 13.11 GB，总显存需求 6.875 + 13.11 + 5 = 24.985 GB，超过 24GB 显存，导致不可行；若 KV Cache 也量化为 INT8，则显存占用降至 6.555 GB，总需求 18.43 GB，可行

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 显存占用与模型权重精度无关，仅取决于上下文长度、层数、头数及 KV 精度，数值量级与计算逻辑自洽。
