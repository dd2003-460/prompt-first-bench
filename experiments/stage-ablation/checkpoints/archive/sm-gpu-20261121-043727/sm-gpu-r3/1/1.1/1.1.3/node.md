# N41: W4 (INT4) 量化在 Qwen3-27B 上的实际存储开销计算：通常采用 GPTQ/AWQ 等算法，每 64 或 128 个参数共享一个 16-bit 或

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

W4 (INT4) 量化在 Qwen3-27B 上的实际存储开销计算：通常采用 GPTQ/AWQ 等算法，每 64 或 128 个参数共享一个 16-bit 或 8-bit scale/zero-point。若 block_size=64 且 scale=16bit，平均字节数/参数 = (4/8 + 16/(64*8)) = 0.53125 bytes/param。需对比纯 4-bit 无 scale (0.5 bytes/param) 的差异。

## Corrected Claim

W4 (INT4) 量化在 Qwen3-27B 上的实际存储开销计算：通常采用 GPTQ/AWQ 等算法，每 64 或 128 个参数共享一个 16-bit 或 8-bit scale/zero-point。若 block_size=64 且 scale=16bit，平均字节数/参数 = (4/8 + 16/(64*8)) = 0.53125 bytes/param。需对比纯 4-bit 无 scale (0.5 bytes/param) 的差异。

## Evidence

先验知识/题面给定，逻辑校验通过：INT4量化基础开销0.5 bytes/param，Block size 64下每64个参数共享1个16-bit scale（2 bytes），额外开销为 2/(64*8) = 0.03125 bytes/param，总和0.53125 bytes/param，计算无误。

## Search Query

AWQ GPTQ int4 quantization block size scale factor memory overhead calculation
