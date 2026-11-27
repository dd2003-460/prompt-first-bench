# N186: NVFP4 推理下 KV Cache 的精度策略对显存的影响：若 KV Cache 保持 BF16 (2 bytes)，占用 13.11 GB (同 N45)；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

NVFP4 推理下 KV Cache 的精度策略对显存的影响：若 KV Cache 保持 BF16 (2 bytes)，占用 13.11 GB (同 N45)；若 KV Cache 量化为 FP8/INT8 (1 byte)，占用降至 6.55 GB。

## Corrected Claim

NVFP4 推理下 KV Cache 的精度策略对显存的影响：若 KV Cache 保持 BF16 (2 bytes)，占用 13.11 GB (同 N45)；若 KV Cache 量化为 FP8/INT8 (1 byte)，占用降至 6.55 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：13.11 GB 与 6.55 GB 的比值约为 2:1，符合 BF16 (2 bytes) 与 FP8/INT8 (1 byte) 的位宽比例关系，数值量级自洽。
